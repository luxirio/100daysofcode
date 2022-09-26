#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#Open the names and store it in a variable:
names_file = open("./Input/Names/invited_names.txt", mode = "r")
names_list = names_file.readlines()

#Stripping the \n of each name
names_list_stripped = []
for name in names_list:
    names_list_stripped.append(name.strip("\n"))


#Openning the model of the letter to be sent
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    content = starting_letter.readlines()

#Substituting the [name] for each of the names:
for name in names_list_stripped:
    f = open(f"./Output/{name}.txt", mode= "w")
    f.write(content[0].replace("[name]", name))
    for lines in content[1:]:
        f.write(lines)