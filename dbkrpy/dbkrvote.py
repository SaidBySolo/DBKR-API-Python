import aiohttp
import asyncio
from .dbkrapiurl import PostURL

class CheckVote:

    def __init__(self, response):
        self.check = self.checkvote(response)

    @staticmethod
    async def get_response(token, user_id):
        URL = f'{PostURL["dbkrvote"]}{user_id}'
        headers = {"token":token,"content-type":"application/json"}
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL,headers=headers) as r:
                response = await r.json()
                if response['code'] == 200:
                    return response
                else:
                    raise Exception(f"{response}")

    def checkvote(self, response):
            return response['voted']

            
