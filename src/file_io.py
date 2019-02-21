"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt', 'r') as x:
    print(x.read())
print(x.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# this won't create a file for me- maybe it deosn't work with WSL?
y = open('bar.txt', 'w+')
y.write("here is some text")
y.write("here is more text")
y.write("here is a third line of text")
print(y.read())
y.close()
print(y.closed)