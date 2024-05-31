import sys

from . import parse_tree
from .serve import serve

if __name__ == "__main__":
    cmds = sys.argv[1:]
    if "serve" in cmds:
        serve()
    else:
        parse_tree()
