"""
file is the file you will open at next

"r": read only
"w": write
"""
file = open("hello.txt", "r")
data = file.read()
try:
    file.write("something")
except:
    print ("SOMETHING WRONG")
file.close()

print(data)

"""
More safe: with ... as ...:

like: with open("hello.py", "r") as f:
          data = f.read()

(with ... as ...:) is a context manager,
if want to learn more, please read the book:
<< fluent python>> Chapter15: Context Manager
"""
