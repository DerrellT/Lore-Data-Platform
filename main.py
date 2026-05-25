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
def search_lore(name, lore_data):
    results = [] # created list to be added onto
    for character in lore_data["characters"]:
        if name in character["name"].lower():
            results.append(( "Character", character)) #goes through and adds all partial matches to a resutl list
    for region in lore_data["regions"]:
        if name in region["name"].lower():
            results.append(("Region", region))
    return results #collects the list that has been made

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
        for ppl in datap:
            print(f"- {ppl}")


def display_search_results(result):
    for index, (result_type, result_data) in enumerate(result): #loops through result to return a list of things individually 
        print(index, result_type)
        if result_type == "Character":
            display_character(result_data)
        elif result_type == "Region":
            display_region(result_data)
    
    
def display_world(lore_data):
    print("------Characters------ ") #helps user see then seperated sections

    for character in lore_data["characters"]: #goes through each character
        print(character.get("name")) #searches chars and gets each key value which is the names

    print("------Regions-------- ")    
    for region in lore_data["regions"]: #goes through each character
        print(region.get("name")) #


def display_help():
    print("      Available commands:     ") #helps user see then seperated sections         
    print("      quit   ") #helps user see then seperated sections
    print("      'list' see Characters and Regions   ") #helps user see then seperated sections
    print("      'help' show command list   ") #helps user see then seperated sections

    


#Controls program flow: loads data, displays available characters, and handles user search loop.
def main():
    lore_data = check_json_files()
    if lore_data is None:
        print("Data missing. Check correct files. Exiting.")
        return 
    display_help()
    while True:
        
        user_input = input("Enter a Character or Region: ").strip().lower() 
        if not user_input:
            print("Not Found")
            print("Try again.")
            continue 
        if user_input == "quit": #added the choice to exit before searching through data
            print("Search ended")
            break
        if user_input == "list": #added the choice to exit before searching through data
           display_world(lore_data)
           continue
        if user_input == "help":
            display_help()
            continue
           
        result = search_lore(user_input, lore_data) #checks character data first if result is none goes to next function, passes chars
        if not result: #checks if results is empty
            print("Not Found")
            print("Try again.")
            continue
        display_search_results(result)       

        

         

main()