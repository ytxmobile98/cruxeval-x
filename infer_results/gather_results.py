from argparse import ArgumentParser
import json
from os import walk
from os.path import abspath, basename, dirname, exists, join
import re


def gather_results_from_single_file(file: str):
    results = {
        "passed": 0,  # "res": true
        "failed": 0,  # "res": false
        "no_input": 0,  # "res": 0 (no input data in cruxeval-x dataset)
        "pass_rate": 0.0,
    }

    if not exists(file):
        return results

    with open(file) as f:
        data: list[dict] = json.load(f)

    for item in data:
        res = item["res"]
        if res is True:
            results["passed"] += 1
        elif res is False:
            results["failed"] += 1
        elif res == 0:
            results["no_input"] += 1

    total_cases = results["passed"] + results["failed"]
    results["pass_rate"] = results["passed"] / total_cases \
        if total_cases > 0 else 0

    return results


def gather_results(dir: str):
    results = {}

    def add_results(lang: str, task_type: str, file_results: dict):
        if lang not in results:
            results[lang] = {
                "input": {},
                "output": {},
            }
        results[lang][task_type] = file_results

    regex = re.compile('([^_]+)_(input|output).json')
    for _, _, files in walk(dir):
        for file in files:
            m = regex.match(file)
            if m:
                lang = m[1]
                task_type = m[2]
                file_results = gather_results_from_single_file(
                    join(dir, file))
                add_results(lang, task_type, file_results)

    return results


def save_results_as_json(results: dict, file: str):
    with open(file, 'w') as f:
        json.dump(results, f, indent=4, sort_keys=True)


def save_results_as_tsv(results: dict, file: str):
    LINE_SEP = '\n'
    COL_SEP = '\t'
    TASK_TYPES = ("input", "output")
    METRICS = ("passed", "failed", "no_input", "pass_rate")

    langs = sorted(results.keys())
    headers = [
        '任务类型',
        '指标',
        *langs,
    ]

    with open(file, 'w') as f:
        # write headers
        f.write(COL_SEP.join(headers))
        f.write(LINE_SEP)

        # write all data lines
        for task_type in TASK_TYPES:
            for metric in METRICS:
                line = [task_type, metric]
                for lang in langs:
                    line.append(str(results[lang][task_type][metric]))
                f.write(COL_SEP.join(line))
                f.write(LINE_SEP)


def main():
    parser = ArgumentParser()
    parser.add_argument("--dir", type=str, required=True)
    args = parser.parse_args()

    results = gather_results(args.dir)

    # save as json
    json_save_path = abspath(join(dirname(__file__),
                                  f"{basename(args.dir)}.json"))
    save_results_as_json(results, json_save_path)
    print(f"Saved JSON results to: \"{json_save_path}\"")

    # save as csv
    tsv_save_path = abspath(join(dirname(__file__),
                                 f"{basename(args.dir)}.tsv"))
    save_results_as_tsv(results, tsv_save_path)
    print(f"Saved TSV results to: \"{tsv_save_path}\"")


if __name__ == "__main__":
    main()
