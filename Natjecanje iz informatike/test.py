import os
import sys
import subprocess


def main():
	print("Testing: Natjecanje iz informatike\n")
	last_ret_code = 0
	for dir1 in filter(lambda element: os.path.isdir(element), os.listdir(".")):
		for dir2 in filter(lambda element: os.path.isdir(element), map(lambda element: os.path.join(dir1, element), os.listdir(dir1))):
			for dir3 in filter(lambda element: os.path.isdir(element), map(lambda element: os.path.join(dir2, element), os.listdir(dir2))):
				print(f"Running tests: {dir3}")
				ret_code = subprocess.run([sys.executable, "-m", "unittest", "-v"], cwd=dir3, stderr=subprocess.STDOUT).returncode
				if ret_code != 0:
					last_ret_code = ret_code
				print()
	sys.exit(last_ret_code)


if __name__ == '__main__':
	main()
