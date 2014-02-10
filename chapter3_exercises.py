# Exercises for chapter 3:

# Name: Xuefeng Liu

#3.1 Answers: Name error: 
#  Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  NameError: name 'repeat_lyrics' is not defined

#3.2 Answers: runs normally
# I'm a lumberjack, and I'm okay.
#I sleep all night and I work all day.
#I'm a lumberjack, and I'm okay.
#I sleep all night and I work all day. 

#3.3 Answers: 
#
 def right_justify (string):
 print (' '* (70-len(string))+string)

 right_justify('allen')

#3.4 Answers
#1.
def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'
do_twice(print_spam)

#result: spam spam

#2. 
def do_twice(f,value):
	f(value)
	f(value) 
	
#3#  
def print_twice(st):
	print (st)
	print  (st)
	
#4
 do_twice(print_twice,'spam')
#result: spam
#        spam
#		spam
#		spam

#5 
def do_four(f,value):
	do_twice(f,value)
	do_twice(f,value)

	
