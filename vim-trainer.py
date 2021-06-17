#!/usr/bin/python3
#Written by omega808
#A test to ask the user to use various VIM shortcuts
#Chosen from a randomized list
from random import *
import time

shortcuts = [ 'Jump to end of file ', 'Jump to the 5th line', 'Go to end of line', 'Go to beginning of line', 'Delete current line', 'Delete current character and enter insert mode', 'delete to end of line', 'Patse line at cursor']

#Get length of list for random generator
cnt = len(shortcuts)
loop_len = cnt * 2 #To run thorugh double the length of list
x = 0 #COunter for loop

print ( "Vim Trainer!")
print ( "Run this on a split tmux screen, with file to edit on the other panel")
time.sleep(4)


#Iterate through the length of the shortcuts list
while ( x < loop_len ):

    rand = randrange(cnt)

    print (shortcuts[rand]) 

    time.sleep(4) #Give time for user to enter data
    x += 1

exit(0)
