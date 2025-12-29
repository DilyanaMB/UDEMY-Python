# FileNotFound
try:
    file = open('a_file.text')
    a_dictionary = {'key': 'value'}
    print(a_dictionary['not_existing_key'])

# always create a specific exception, so other exceptions in the try block not to be omitted, e.g.
# do not use only 'except:' even though it's possible
except FileNotFoundError:
    # if the file cannot open, then simply create a new one
    file = open('a_file.text', 'w')
    file.write("Hello World")

# I can have as many exception as needed.
# also can hold of the original error if you use 'except TypeError as sth'
except KeyError as error_message:
    print(f'The key {error_message} does not exist')

# else is executed ONLY if TRY succeed
else:
    content = file.read()
    print(content)

# run regardless of what happens
finally:
    file.close()
    print('File was closed')
