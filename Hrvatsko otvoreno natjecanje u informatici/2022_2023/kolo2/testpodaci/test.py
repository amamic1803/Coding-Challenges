import subprocess
import sys
import os
import unittest


class TestKolo2(unittest.TestCase):
    def test_euro(self):
        test_task("euro")

    def test_rezultat(self):
        test_task("rezultat")

    def test_tramvaji(self):
        test_task("tramvaji")

    def test_prijateljice(self):
        test_task("prijateljice")


def test_task(task: str):
    for input_file in os.listdir(task):
        if ".in." in input_file:
            with open(f"{task}/{input_file}", encoding="UTF-8") as file:
                input_text = file.read()
            with open(f"{task}/{input_file.replace('.in.', '.out.')}", encoding="UTF-8") as file:
                output_text = file.read()
            proc = subprocess.run(
                ["python", f"../{task}.py"],
                input=input_text,
                text=True,
                encoding="UTF-8",
                capture_output=True,
                check=True
            )
            if proc.stdout != output_text:
                print(f"Test {task}/{input_file} failed!", file=sys.stderr)
                assert proc.stdout == output_text


if __name__ == '__main__':
    unittest.main()
