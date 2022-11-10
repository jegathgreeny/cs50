import sys

from main_explained import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
    # if print(hello(sys.argv[1])) is run then after doing the function's work
    # it will also print None, if the function returns nothing
    print(hello(sys.argv[1]))
