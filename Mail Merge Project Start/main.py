#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as data:
    names_list = data.readlines()
    # print(name_lists)


with open("./Input/Letters/starting_letter.txt", "r") as original_letter:
    contents = original_letter.read()

    for name in names_list:
        stripped_name = name.strip()
        replaced_text = contents.replace(PLACEHOLDER, stripped_name)

        # print(replaced_text)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as ready_to_send:
            ready_to_send.write(replaced_text)


