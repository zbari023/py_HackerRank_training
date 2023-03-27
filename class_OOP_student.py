print('please Enter the Information of Student: ')

class Noteofstudent():
    def __init__(self):
        self.name = input('Enter the name of student : ')
        self.age = int(input(f'{self.name} age : '))
        self.ID = int(input(f'{self.name} ID : '))
        print(f'The Student {self.name} is {self.age} years old and have ID: {self.ID}')
    def listing_Notes(self):
        self.Note_list = []                # empty list
        print('Now you can enter his Notes and when you press 00 is to be end of your Notes :')
        while True:
            Note = float(input('Note: '))