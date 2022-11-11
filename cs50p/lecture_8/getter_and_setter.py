class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return self.name

    # this is how you define a getter
    @property
    def name(self):
        return self._name

    # and this is how you define a setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing name')
        # the leading _ tells that it is different from the method name
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError('Invalid house')
        self._house = house


    # this is a class method to give in the input to the class
    @classmethod
    def get(cls):
        name = input('name: ')
        house = input('house: ')
        return cls(name, house)



def main():
    student = Student.get()
    print(student)


# this is not needed if classmethod is used to give the input
# def get_student():
#     name = input('name: ')
#     house = input('house: ')
#     return Student(name, house)


if __name__ == '__main__':
    main()
