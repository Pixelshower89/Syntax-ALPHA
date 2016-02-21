
print """\nHello, and welcome to Pixelshower89's Word Processor version ALPHA.
You will be prompted to give a phrase, and then a command.
Type 'help' when prompted to give a command to bring up a list of available commands (NOTE: You can only do this once).\n"""

phrase = raw_input("What is your phrase?   ")

command = raw_input("\nWhat is your command?   ")

def helprestart():
    phrase = raw_input("\nWhat is your phrase?   ")
    command = raw_input("\nWhat is your command?   ")
    if command == "strl":
        final = phrase.lower()
    elif command == "stru":
        final = phrase.upper()
    elif command == "strt":
        final = phrase.title()
    return final

    
help = ["\n'strl' Converts the whole phrase to lowercase", "'stru' Converts the whole phrase to uppercase", "'strt' Make the first letter of every word uppercase."]

if command == "strl":
    final = phrase.lower()
elif command == "stru":
    final = phrase.upper()
elif command == "strt":
    final = phrase.title()
elif command == "help":
    print help[0]
    print help[1]
    print help[2]
    final = helprestart()

print (final)