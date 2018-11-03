# format
me = "girls"
sentence = f"hello, {me}"
print (sentence)

# list
numbers = [1,2,3]
""" or number = list([1,2,3]) """
print (numbers)
print (len(numbers))
print (numbers[1])
numbers.append(4)
print (numbers)

for number in numbers:
    print (number)

# dict
di = {}
di['who'] = 'CGC'
di['where'] = 'CCNU'
for key, value in di.items():
    print (f"{key} is: {value} ")

# method
class obj:
    __name__ = "MyName"
    def name(self):
        print(self.__name__)

OBJ = obj()
OBJ.name()
