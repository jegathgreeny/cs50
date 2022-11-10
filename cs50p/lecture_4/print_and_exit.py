import sys

if len(sys.argv) > 2:
    # print the output and exit
    sys.exit('Too many arguments')
elif len(sys.argv) < 2:
    # print the output and exit
    sys.exit("To few arguments")

print(f'My name is, {sys.argv[1]}')
