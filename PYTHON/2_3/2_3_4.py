"""
# while:
a = 0
while a <= 10:
    print (a)
    a = a + 1
    print (a <= 10)
"""

"""
# a crazy test:

while True:
    print ("IG NB")
# It while run forever...
"""

i = 1
while i <= 10:
    if i%2 == 1:
        i = i + 1
        continue
    if i == 8:
        print (" I will break now!")
        break
    print (i)
    i = i + 1
