# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

def disemvowel(string):
    nova_string = ''
    for x in string:
        if x != 'a' and x != 'A' and x != 'e' and x != 'E' and x != 'i' and x != 'I' and x != 'o' and x != 'O' and x != 'u' and 'U':
            nova_string = nova_string + x
    return nova_string
