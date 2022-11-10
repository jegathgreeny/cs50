def main():
    hello('world')
    goodbye('world')

def hello(name):
    print(f'hello, {name}')

def goodbye(name):
    print(f'goodbye, {name}')


# if main is simply run like this, then the main function will be run
# when you import this module to another program
# main()


# to avoid the above error this way of execution is used.
# so __name__ will have the value __main__ when the file is not imported into another program
# and the __name__ will have the value of the filename without the .py extension when imported into another program
print(__name__)
if __name__ == '__main__':
    main()
