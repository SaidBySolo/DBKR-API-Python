import aiohttp
import asyncio

class CheckVote:

    def __init__(self, response):
        self.check = self.checkvote(response)

    @classmethod
    async def get_response(cls, token, user_id):
        URL = f'https://api.koreanbots.cf/bots/voted/{user_id}'
        headers = {"token":token,"content-type":"application/json"}
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL,headers=headers) as r:
                response = await r.json()
                return response

    def checkvote(self, response):
        if response['code'] == 200:
            return response['voted']
        else:
            return response
            
