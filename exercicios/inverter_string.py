# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'

def inverter(string):
    string = ' '.join(string.split()) # desnecessário, mas legal!!!
    return string[::-1]

print(inverter('Hello World!'))
