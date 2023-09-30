from graphene import String, ObjectType
from graphene import ObjectType, List, String, Schema


class City(ObjectType):
    name = String(required=True)
    lat = String()
    long = String()
