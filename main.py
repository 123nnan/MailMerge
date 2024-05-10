#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt') as data:
    name = data.readlines()

with open('./Input/Letters/starting_letter.txt') as file:
    letter = file.read()
    for names in name:
        stripped_names = names.strip()
        new_letter = letter.replace('[name]', stripped_names)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_names}.txt', mode='w') as final_letter:
            final_letter.write(new_letter)