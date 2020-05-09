import aiohttp
import asyncio
from .dbkrsort import Sort
from .dbkrapiurl import PostURL

class Page:

    def __init__(self, response):
        self.idlist = Sort.sort_id(response)
        self.namelist = Sort.sort_name(response)
        self.serverslist = Sort.sort_servers(response)
        self.voteslist = Sort.sort_votes(response)
        self.introlist = Sort.sort_intro(response)
        self.avatarlist = Sort.sort_avatar(response)
        self.categorylist = Sort.sort_category(response)
        self.taglist = Sort.sort_tag(response)
        self.statelist = Sort.sort_state(response)

    @staticmethod
    async def get_response(page=1):
        URL = f"{PostURL['dbkrget']}?page={page}"
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                response = await r.json()
                if response['code'] == 200:
                    return response
                else:
                    raise Exception(f"{response}")
