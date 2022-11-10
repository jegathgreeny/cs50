def main():
    student = get_student()
    # function by default returns tuples when multiple values are returned
    # there is nothing wrong with returning tuples, but if want to change the values somehow
    # then that will raise an error, so tuples are suitable only for default values

    print(type(student))
    # this will raise an error, beacuse the tuples are being modified here
    # if student[0] == "Padma":
    #     student[1] = 'Ravenclaw'

    print(f'{student[0]} from {student[1]}')

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # you can override and return a list using the [] like this [name, house]
    # this will now return a list, which is mutable
    # return [name, house]
    return name, house


if __name__ == '__main__':
    main()
