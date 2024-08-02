import os
import sys
import subprocess


def main():
	print("Testing: Hrvatsko otvoreno natjecanje u informatici\n")
	for dir1 in filter(lambda element: os.path.isdir(element), os.listdir(".")):
		for dir2 in filter(lambda element: os.path.isdir(element), map(lambda element: os.path.join(dir1, element), os.listdir(dir1))):
			directory = os.path.join(dir2, "testpodaci")
			if os.path.exists(directory):
				print(f"Running tests: {dir2}")
				ret_code = subprocess.run(["python", "-m", "unittest"], cwd=directory, stderr=subprocess.STDOUT).returncode
				if ret_code != 0:
					sys.exit(ret_code)
				print()


if __name__ == '__main__':
	main()
