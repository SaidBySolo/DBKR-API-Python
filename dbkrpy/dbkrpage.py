import aiohttp
import asyncio

class Page:

    def __init__(self, response):
        self.idlist = self.sort_id(response)
        self.namelist = self.sort_name(response)
        self.serverslist = self.sort_servers(response)
        self.voteslist = self.sort_votes(response)
        self.introlist = self.sort_intro(response)
        self.avatarlist = self.sort_avatar(response)
        self.categorylist = self.sort_category(response)
        self.taglist = self.sort_tag(response)
        self.statelist = self.sort_state(response)

    @staticmethod
    async def get_response(page):
        URL = f'https://api.koreanbots.cf/bots/get?page={page}'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                response = await r.json()
                if response['code'] == 200:
                    return response
                else:
                    raise Exception(f"{response}")

    def sort_id(self,response):
            data = response['data']
            idlist = [i['id'] for i in data]
            return idlist

    def sort_name(self,response):
            data = response['data']
            namelist = [n['name'] for n in data]
            return namelist
            
    def sort_servers(self,response):
            data = response['data']
            serverslist = [s['servers'] for s in data]
            return serverslist

    def sort_votes(self,response):
            data = response['data']
            voteslist = [v['votes'] for v in data]
            return voteslist

    def sort_intro(self,response):
            data = response['data']
            introlist = [i['intro'] for i in data]
            return introlist

    def sort_avatar(self,response):
            data = response['data']
            avatarlist = [a['avatar'] for a in data]
            return avatarlist

    def sort_category(self,response):
            data = response['data']
            categorylist = [c['category'] for c in data]
            return categorylist

    def sort_tag(self,response):
            data = response['data']
            taglist = [t['tag'] for t in data]
            return taglist

    def sort_state(self,response):
            data = response['data']
            statelist = [s['state'] for s in data]
            return statelist