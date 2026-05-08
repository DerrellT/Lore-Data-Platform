import json

def check_json_files():
    try :
        with open('data/test.json') as f:
            data = json.load(f)
            print("Found stuff!")
            return data
    except FileNotFoundError:
        print("Missing character")
        return None


def main():
    check_json_files()
    return

main()