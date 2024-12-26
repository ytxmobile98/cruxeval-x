from argparse import ArgumentParser
import json
from os import walk
from os.path import abspath, basename, dirname, exists, join
import re


def gather_results_from_single_file(file: str):
    results = {
        "true": 0,
        "false": 0,
        "0": 0,
    }

    if not exists(file):
        return results

    with open(file) as f:
        data: list[dict] = json.load(f)
    for item in data:
        res = item["res"]
        if res == True:
            results["true"] += 1
        elif res == False:
            results["false"] += 1
        elif res == 0:
            results["0"] += 1

    return results


def gather_results(dir: str):
    results = {}

    def add_results(lang: str, file_type: str, file_results: dict):
        if lang not in results:
            results[lang] = {}
        results[lang][file_type] = file_results

    regex = re.compile('([^_]+)_(input|output).json')
    for _, _, files in walk(dir):
        for file in files:
            m = regex.match(file)
            if m:
                lang = m[1]
                file_type = m[2]
                file_results = gather_results_from_single_file(
                    join(dir, file))
                add_results(lang, file_type, file_results)

    return results


def main():
    parser = ArgumentParser()
    parser.add_argument("--dir", type=str, required=True)
    args = parser.parse_args()

    results = gather_results(args.dir)
    json_save_path = abspath(join(dirname(__file__),
                                  f"{basename(args.dir)}.json"))
    with open(json_save_path, 'w') as f:
        json.dump(results, f, indent=4, sort_keys=True)
        print(f"Saved results to: \"{json_save_path}\"")


if __name__ == "__main__":
    main()
