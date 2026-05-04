# A tool to make errors in code much more evident

import ast
import sys

def check_syntax(filename):
    with open(filename, 'r') as file:
        code = file.read()

    try:
        ast.parse(code)
        print(f"{filename} has no syntax errors")
    except SyntaxError as e:
        print(f"Syntax error on line {e.lineno}: {e.msg}")
        print(f"Text: {e.text}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python yippie_err.py <filename>")
        sys.exit(1)

    check_syntax(sys.argv[1])