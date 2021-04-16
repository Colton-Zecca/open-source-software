from pymongo import MongoClient
import pprint
client = MongoClient()

if __name__ == '__main__':
    db = client.mongo_db_lab
    definitions = db.definitions

    print("\n------------Insert A New Record------------")
    new_definition = {
        "word": "SGS",
        "definition": "n. The Student Government Suite, one of the many places to pull an All-Nighter studying for an exam."
    }
    definition_id = definitions.insert_one(new_definition).inserted_id
    print(f"> Entry inserted with ID: {definition_id}")
    
    print("\n------------Fetch All Records------------")
    for definition in definitions.find():
        pprint.pprint(definition)

    print("\n------------Fetch One Record------------")
    pprint.pprint(definitions.find_one())

    print("\n------------Fetch A Specific Record------------")
    pprint.pprint(definitions.find_one({"word": "Zamboni"}))

    print("\n------------Fetch A Record By Object ID------------")
    pprint.pprint(definitions.find_one({"_id": definition_id}))

    print("\n------------Cleanup (Delete Record)------------")
    deleted_count = definitions.delete_one({"word": "SGS"}).deleted_count
    print(f"> {deleted_count} entry deleted")
    