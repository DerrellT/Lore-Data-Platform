#Simple CLI-based system for loading and searching character data from JSON.
import json

#Loads character dataset from JSON file and returns parsed data.
def check_json_files():
    chars = None
    try :
        with open('data/test.json') as f:
            chars = json.load(f)
            return chars
    except FileNotFoundError:
        print("Missing character")
        return None

#Searches character dataset for a matching name and returns the character if found.
def search_characters(name, chars):
    for character in chars["characters"]:
        if character["name"].lower() == name:
            return character 
    return None

#Formats and displays character information to the user.
def display_character(character): 
    print(f"Name: {character.get('name')}")    
    data = character.get("traits", "region", []) 
    if data:
        print("Traits: ")
        for trait in data:
            print(f"- {trait}")
        print("Region: ")
        for region in data:
            print(f"- {region}")



#Controls program flow: loads data, displays available characters, and handles user search loop.
def main():
    chars = check_json_files()
    if chars is None:
        print("Characters data missing. Exiting.")
        return
    
    print("------Characters------ ") #helps user see then seperated sections

    for character in chars["characters"]: #goes through each character
        print(character.get("name")) #searches chars and gets each key value which is the names

    print("------Regions-------- ")    
    for character in chars["characters"]: #goes through each character
        print(character.get("region")) #

    print("------'Quit' to exit program------ ") #helps user see then seperated sections

    while True:
        found = False 
        user_input = input("Enter a Character: ").strip().lower() #moved lower here 

        if user_input == "quit": #added the choice to exit before searching through data
            print("Search ended")
            break #stops program breaks loop

        result = search_characters(user_input, chars) #checks character data first if result is none goes to next function, passes chars
        if result:
            found = True 
            display_character(result) #goes to next function
        

        if not found: #prints below if found remains false
            print("Not Found.")
            print("Try again.")

         

main()