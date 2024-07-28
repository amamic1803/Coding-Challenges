import subprocess
import sys
import os
import unittest


class Test2023Skolsko(unittest.TestCase):
    def test_radnici(self):
        test_task("radnici", 2)

    def test_euro(self):
        test_task("euro", 2)

    def test_putovanje(self):
        test_task("putovanje", 2)


def test_task(task: str, kategorija: int):
    match kategorija:
        case 1:
            kategorija = "ss1"
        case 2:
            kategorija = "ss2"
        case _:
            raise ValueError("Invalid category!")

    for input_file in os.listdir(task):
        if "in" in input_file:
            with open(f"{task}/{input_file}", encoding="UTF-8") as file:
                input_text = file.read()
            with open(f"{task}/{input_file.replace('in', 'out')}", encoding="UTF-8") as file:
                output_text = file.read()
            proc = subprocess.run(
                ["python", f"../{kategorija}/{task}.py"],
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
