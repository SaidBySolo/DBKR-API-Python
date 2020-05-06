import aiohttp
import asyncio

class Page:

    def __init__(self, response):
        self.idlist = self.sort_id(response)

    @staticmethod
    async def get_response(page):
        URL = f'https://api.koreanbots.cf/bots/get?page={page}'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                response = await r.json()
                return response

    def sort_id(self,response):
        if response['code'] == 200:
            data = response['data']
            idlist = [i for i in data]
            return idlist

    def sort_name(self,response):
        if response['code'] == 200:
            data = response['data']

    def sort_servers(self,response):
        if response['code'] == 200:
            data = response['data']

    def sort_votes(self,response):
        if response['code'] == 200:
            data = response['data']

    def sort_intro(self,response):
        if response['code'] == 200:
            data = response['data']

    def sort_avatar(self,response):
        if response['code'] == 200:
            data = response['data']

    def sort_category(self,response):
        if response['code'] == 200:
            data = response['data']

    def sort_tag(self,response):
        if response['code'] == 200:
            data = response['data']

    def sort_state(self,response):
        if response['code'] == 200:
            data = response['data']

