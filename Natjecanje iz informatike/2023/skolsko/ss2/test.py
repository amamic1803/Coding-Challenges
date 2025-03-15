import io
import os
import unittest
from unittest.mock import patch

import euro
import putovanje
import radnici


class Test2023SkolskoSS2(unittest.TestCase):
    def test_euro(self):
        test_task(self, "euro")

    def test_putovanje(self):
        test_task(self, "putovanje")

    def test_radnici(self):
        test_task(self, "radnici")


def test_task(test_class, task: str):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for input_file in os.listdir(os.path.join(base_dir, "test-data", task)):
        if ".in." in input_file:
            with open(os.path.join(base_dir, "test-data", task, input_file), encoding="UTF-8") as file:
                input_text = file.read()
            with open(os.path.join(base_dir, "test-data", task, input_file.replace('.in.', '.out.')), encoding="UTF-8") as file:
                output_text = file.read()

            with patch('sys.stdin', io.StringIO(input_text)), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                match task:
                    case "euro":
                        euro.main()
                    case "putovanje":
                        putovanje.main()
                    case "radnici":
                        radnici.main()
                    case _:
                        raise ValueError("Invalid task")
                actual_output = mock_stdout.getvalue()

            test_class.assertEqual(actual_output, output_text, f"Test {task} failed!\nEXPECTED STDOUT:\n{output_text}\nACTUAL_STDOUT:\n{actual_output}\nSTOPPING!")


if __name__ == '__main__':
    unittest.main()
