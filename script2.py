import random, string

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
letters = string.ascii_lowercase

letter_input_1 = input("What do you want? Enter 'v' for vowels, 'c' for constants, 'l' for any letter: ")
letter_input_2 = input("What do you want? Enter 'v' for vowels, 'c' for constants, 'l' for any letter: ")
letter_input_3 = input("What do you want? Enter 'v' for vowels, 'c' for constants, 'l' for any letter: ")

print(letter_input_1+letter_input_2+letter_input_3)


def generator():
    if letter_input_1 =='v':
        letter1 = random.choice(vowels)
    elif letter_input_1=='c':
        letter1 = random.choice(consonants)
    elif letter_input_1=='l':
        letter1 = random.choice(letters)
    else:
        letter1=letter_input_1




        

    letter3 = random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3
    return(name)

print(generator())
