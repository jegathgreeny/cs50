class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        '''initialize the attributes'''
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts


    def __str__(self):
        '''string representation of the vault'''
        return f'{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts'

    def __add__(self, other):
        '''overloads the + operator'''
        # self is the opearand on the left
        # other is the operand on the right
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# potter is self that is whatever is to the left of the + operator
# weasley is other that is whatever is to the right of the + operator
total = potter + weasley
print(total)
