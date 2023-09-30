from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema
# from graphql.execution.executors.asyncio import AsyncioExecutor

from starlette.graphql import GraphQLApp
from schemas import City
import json


class Query(ObjectType):
    course_list = None
    get_course = List(City)

    async def resolve_get_course(self, info):
        with open("./cities_data.json") as city:
            city_list = json.load(city)
        return city_list


app = FastAPI()
app.add_route("/", GraphQLApp(
    schema=Schema(query=Query),
    # executor_class=AsyncioExecutor

)

)
