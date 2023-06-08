import os
import sys


def print_tree(startpath, filesonly=False, dirsonly=False):
    print(f"+ {os.path.basename(startpath)}")
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = "|   " * level
        print(f"{indent}+--{os.path.basename(root)}/")
        if filesonly:
            dirs.clear()  # Suppress the output of subdirectories
        elif dirsonly:
            files.clear()  # Suppress the output of files
        for file in files:
            subindent = "|   " * (level + 1)
            print(f"{subindent}+--{file}")
        for dir in dirs:
            subindent = "|   " * (level + 1)
            print(f"{subindent}+--{dir}/")


if __name__ == "__main__":
    theDir = "..\.."
    if len(sys.argv) > 1:
        theDir = sys.argv[1]

    print_tree(theDir, dirsonly=True)
    print("-" * 60)
    print_tree(theDir, filesonly=True)
    print("-" * 60)
    print_tree(theDir)
