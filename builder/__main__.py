import sys

from . import parse_tree
from .serve import serve

if __name__ == "__main__":
    cmds = sys.argv[1:]
    if "serve" in cmds:
        serve()
    elif "debug" in cmds:
        parse_tree(debug=True)
    else:
        parse_tree()
