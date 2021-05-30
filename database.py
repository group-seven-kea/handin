from os import environ as env
from pymongo import MongoClient


def connect():
    return MongoClient(env.get("MONGODB_CONNECTION_STRING"))

