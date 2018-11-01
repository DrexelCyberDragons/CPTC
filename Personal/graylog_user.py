import pymongo
import argparse
from pprint import pprint
import json
import bson

"""
User Added:
    username : Ben
    password : testtest

Simple python script to add user to graylog mongodb store.
Need to version lock the dependencies above and have command here for install them
!!!!!
    pip install pymongo
!!!!!

"""

# Change these based on graylog configs
id = "5bdb71e51e1f82033a02576c"
role_1 = "5bda2c531e1f8278bcb8dad8"
role_2 = "5bda2c531e1f8278bcb8dad9"


def main():
    parser = argparse.ArgumentParser(description='Add user to graylog.')
    parser.add_argument('host', type=str, help='location of mongo server')
    parser.add_argument('port', type=str, help='port of mongo server')
    parser.add_argument('insert', type=str, help='to insert a user') # hopefully this is clear text

    args = parser.parse_args()

    print("Connecting to mongodb://{}:{}/".format(args.host, args.port))
    myclient = pymongo.MongoClient("mongodb://{}:{}/".format(args.host, args.port))
    print("Connected")
    print("Using database...")
    mydb = myclient["graylog"]
    print("Database used")
    print("choosing collection...")
    mycol = mydb["users"]
    print("Chose collection")

    mylist = [
        {
            u'_id': bson.objectid.ObjectId(id),
            u'email': u'ben@face.com',
            u'full_name': u'Benjamin',
            u'password': u'{bcrypt}$2a$10$xTgmA8asmpRwNDyJ9eiCEuM4b61bwot89dQ3xhn3q7/PzdCC8gBEq{salt}$2a$10$xTgmA8asmpRwNDyJ9eiCEu',
            u'permissions': [],
            u'roles': [ bson.objectid.ObjectId(role_1), bson.objectid.ObjectId(role_2) ],
            u'session_timeout_ms': 180000000,
            u'timezone': u'America/New_York',
            u'username': u'Ben'
        }
    ]

    if args.insert  != 'True':
        cursor = mycol.find({})
        for document in cursor: 
            pprint(document)
    else:
        print("Adding user ({}:{})...".format("Ben", "testtest"))
        x = mycol.insert_many(mylist)
        print("Added user with id" + str(x.inserted_ids))

if __name__ == '__main__':
    main()
        