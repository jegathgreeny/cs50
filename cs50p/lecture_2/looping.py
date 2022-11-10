# this is the same as the range function, but it's not a good practice
# as longer lists will have be really long to type in
# for i in [0, 1, 2]:
    # print(i)
    # print(meow)


# here we don't care about the i, we just need it to count.
# for i in range(3):
    # print('meow')

# here we can use the underscore instead, but it still assigns the value to the underscore
# it just more pythonic to use underscore where we don't use i or the looping value
# for _ in range(3):
    # print(_)
    # print('meow')


# or more simply we can use this
print('meow\n' * 3, end='')
