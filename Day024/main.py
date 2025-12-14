file = open('my_file.txt')
content = file.read()
print(content)

file.close()

with open('my_file.txt', mode='a') as f: # mode='w' set mode to also be able to write but override previous text,
    # by default mode is set to 'r' - read only, if you want to add text -set the mode to 'a' for append

    # if you give a name of the file that doesn't exist, it will be
    # automatically created upon running
    f.write('\nI have a handsome boyfriend, named Victor.')

with open('../../../Desktop/new_file.txt') as f:
    print(f.read())