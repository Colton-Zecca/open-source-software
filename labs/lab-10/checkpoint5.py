from pymongo import MongoClient
import pprint
import datetime
client = MongoClient()


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''

    db = client.mongo_db_lab
    definitions = db.definitions
    rand_def_cursor = definitions.aggregate([{"$sample": {"size": 1}}])

    # rand_def is the dictionary containing a random document from the mongo_db_lab database
    rand_def = (list(rand_def_cursor))[0]
    rand_def_id = rand_def["_id"]
    date_to_add = datetime.datetime.utcnow().isoformat()

    # print("\n> Before:")
    # pprint.pprint(definitions.find_one({"_id": rand_def_id}))

    if "dates" not in rand_def.keys():
        print("A: dates key DOES NOT exist, updating")
        definitions.update(
            {"_id": rand_def_id},
            {"$set": {"dates": [date_to_add]}}
        )
    else:
        print("A: dates key DOES exist, appending")
        definitions.update(
            {"_id": rand_def_id},
            {"$push": {"dates": date_to_add}}
        )

    # print("\n> After:")
    # pprint.pprint(definitions.find_one({"_id": rand_def_id}))

    # return {
    #     'word': rand_def['word'],
    #     'definition': rand_def['definition']
    # }
    return definitions.find_one({"_id": rand_def_id})


if __name__ == '__main__':
    print(random_word_requester())
