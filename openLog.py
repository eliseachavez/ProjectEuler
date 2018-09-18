#!/usr/bin/env python
#using python's "open" function, get a "file object"
#   file objects have methods and atrributes than can be used to collect info about the file opened. can also manipulate the file.
#       mode attribute tells you what mode the file was opened in.
#       name attribute tells name of file that the file object opened
#       a file and a file object are two entirely different things, tho related
#   in python, to be a file, it must be text or binary. (is a log file a text file or neither of these types?)
#       text files are a sequence of lines. a line is a sequence of characters -- the code or syntax
#       each line terminates with a special character-- usually a comma or newline character, backslash can be a new line for the code/syntax and not the actual text
#   modes:
#       r = read
#       w = write -- edit and write new info to file. exisint file w same name will be erased
#       a = append - adds new data to end, like new info
#       r+ = special read and write mode, handles both actions when working with a file
#       


#NOTE: in order to exectue, need to execute like "python openLog.py" or tell the top of the script where to exectue from with #!/usr/bin/env python
logCopy = open("pacmanlogCopy.log", "r")
print(logCopy)
