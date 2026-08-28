import os
import shutil
import subprocess


RESULTS_DIR = "allure-results"
REPORT_DIR = "allure-report"


def main():
    if os.path.exists(RESULTS_DIR):
        shutil.rmtree(RESULTS_DIR)


    pytest_result = subprocess.run([
        "pytest",
        "-v",
        "--alluredir", RESULTS_DIR,
    ])


    subprocess.run([
        "allure",
        "generate",
        RESULTS_DIR,
        "-o",
        REPORT_DIR,
        "--clean",
    ])


    subprocess.run([
        "allure",
        "open",
        REPORT_DIR,
    ])


    return pytest_result.returncode


if __name__ == "__main__":
    raise SystemExit(main())