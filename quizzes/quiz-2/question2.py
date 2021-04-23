from pymongo import MongoClient
import pprint
client = MongoClient()

if __name__ == '__main__':
    '''
    Write a simple python program using pymongo that reads both files and writes 
    the data to a mongo collection. Data w/the same IDENTIFIER should be merged 
    into the same document with IDENTIFIER as its unique document identifier. 
    Use database yankees and collection menu.
    '''
    # read in file 1 and file 2
    entries_dict = {}

    names_file = open("file1.txt")
    for line in names_file:
        _id, name = line.split()
        # print(f"{_id}: {name}\n")
        entries_dict[_id] = {
            "_id": _id,
            "name": name
        }

    drinks_file = open("file2.txt")
    for line in drinks_file:
        _id, drink = line.split()
        if _id in entries_dict:
            entries_dict[_id]["drink"] = drink
        else:
            entries_dict[_id] = {
            "_id": _id,
            "drink": drink
        }

    # for k, v in entries_dict.items():
    #     print(f"{k}: {v}\n")

    entries_list = list(entries_dict.values()) # convert entries_dict to a list
    # print(entries_list)
    
    menu = client.yankees.menu
    menu.insert_many(entries_list)
    