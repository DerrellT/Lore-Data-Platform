#Simple CLI-based system for loading and searching character data from JSON.
import json

#Loads character dataset from JSON file and returns parsed data.
def check_json_files():
    lore_data = None
    try :
        with open('data/lore_data.json') as f:
            lore_data = json.load(f)
            return lore_data
    except FileNotFoundError:
        print("Missing character")
        return None

#Searches character dataset for a matching name and returns the character if found.
def search_characters(name, lore_data):
    for character in lore_data["characters"]:
        if character["name"].lower() == name:
            return character 
    return None

def search_region(name, lore_data):
    for region in lore_data["regions"]:
        if region["name"].lower() == name:
            return region 
    return None

#Formats and displays character information to the user.
def display_character(character): 
    print(f"Name: {character.get('name')}")    
    data = character.get("traits", [])
    datar = character.get("region", [])
    if data:
        print("Traits: ")
        for trait in data:
            print(f"- {trait}")
    if datar:
        print("Region: ")
        for region in datar:
            print(f"- {region}")

def display_region(region): 
    print(f"Region: {region.get('name')}")    
    datareg = region.get("description", [])
    datap = region.get("people", [])

    if datareg:
        print("Description: ")
        for descr in datareg:
            print(f"- {descr}")
    if datap: 
        print("People: ")
        for descr in datap:
            print(f"- {descr}")

        



#Controls program flow: loads data, displays available characters, and handles user search loop.
def main():
    lore_data = check_json_files()
    if lore_data is None:
        print("Data missing. Check correct files. Exiting.")
        return
    
    
    print("------Characters------ ") #helps user see then seperated sections

    for character in lore_data["characters"]: #goes through each character
        print(character.get("name")) #searches chars and gets each key value which is the names

    print("------Regions-------- ")    
    for region in lore_data["regions"]: #goes through each character
        print(region.get("name")) #

    print("------'Quit' to exit program------ ") #helps user see then seperated sections

    while True:
        found = False 
        user_input = input("Enter a Character or Region: ").strip().lower() #moved lower here 

        if user_input == "quit": #added the choice to exit before searching through data
            print("Search ended")
            break #stops program breaks loop

        result = search_characters(user_input, lore_data) #checks character data first if result is none goes to next function, passes chars
        if result:
            found = True 
            display_character(result) #goes to next function
        
        result = search_region(user_input, lore_data)
        if result:
            found = True
            display_region(result)

        if not found: #prints below if found remains false
            print("Not Found.")
            print("Try again.")

         

main()