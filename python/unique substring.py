message = "how about now"

# A set can store only unique values.
the = set()

length = len(message)

for i in range(length):
    the.add(message[i])

    # To get out of the loop once their's a repetitive value.
    if i < len(the):
        continue
    else:
        break

print(the)
