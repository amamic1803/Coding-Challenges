import subprocess
import sys
import os
import unittest


class Test2021Skolsko(unittest.TestCase):
    def test_mjere(self):
        test_task(1, "mjere")

    def test_anagram(self):
        test_task(1, "anagram")

    def test_konj(self):
        test_task(1, "konj")


def test_task(podskupina: int, task: str):
    assert podskupina in [1, 2]
    for input_file in os.listdir(task):
        if ".in." in input_file:
            with open(f"{task}/{input_file}", encoding="UTF-8") as file:
                input_text = file.read()
            with open(f"{task}/{input_file.replace('.in.', '.out.')}", encoding="UTF-8") as file:
                output_text = file.read()
            proc = subprocess.run(
                ["python", f"../ss{podskupina}/{task}.py"],
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
