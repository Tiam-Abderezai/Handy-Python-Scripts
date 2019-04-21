# Authored by Tiam Abderezai

# This snippet 1) reads from a text file called 'Source' 2) replaces the word 'CHEESE' with 'CAKE' into a new file called 'Destination'
# NOTE: you must already have 2 text files named 'Source' and 'Desitnation'

with open('Source', 'r') as fRead, open('Destination', 'w') as fWrite: # Reads from 'Source' and writes into 'Destination'
    for line in fRead: # Loops through 'Source' line by line
        if line.strip() == 'CHEESE': # Finds the word 'CHEESE'
            print('OK') # Prints 'OK' to verify previous code worked
            fWrite.write(line.strip().replace('CHEESE' ,'CAKE\n')) # Writes into 'Destination' and replaces 'CHEESE' with 'CAKE'
        else:
            fWrite.write(line.strip() + '\n') # Continues writing the rest of the lines from Source to Destination
