import aiohttp
import asyncio

class GetById:

    def __init__(self, response):
        self.id = self.bot_id(response)
        self.timestamp = self.bot_timestamp(response)
        self.name  = self.bot_name(response)
        self.owner = self.bot_owner(response)
        self.library = self.bot_library(response)
        self.prefix = self.bot_prefix(response)
        self.votes = self.bot_votes(response)
        self.servers = self.bot_servers(response)
        self.intro = self.bot_intro(response)
        self.description = self.bot_description(response)
        self.web = self.bot_web(response)
        self.git = self.bot_git(response)
        self.url = self.bot_URL(response)
        self.discord = self.bot_support_discord(response)
        self.categories = self.bot_category(response)
        self.status = self.bot_status(response)
        self.avatar = self.bot_avatar(response)
        self.verified = self.bot_verified(response)
        self.trusted = self.bot_trusted(response)
        self.state = self.bot_state(response)

    @staticmethod
    async def get_response(bot_id):
        URL = f'https://api.koreanbots.cf/bots/get/{bot_id}'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                response = await r.json()
                if response['code'] == 200:
                    return response
                else:
                    raise Exception(f"{response}")

    def bot_id(self, response):
        data = response['data']
        return data['id']

    def bot_timestamp(self, response):
        data = response['data']
        bot_timestamp = data['date']
        return bot_timestamp

    def bot_name(self, response):
        data = response['data']
        bot_name = data['name']
        return bot_name

    def bot_owner(self, response):
        data = response['data']
        owner = data['owners']
        return owner

    def bot_library(self, response):
        data = response['data']
        library = data['lib']
        return library

    def bot_prefix(self, response):
        data = response['data']
        prefix = data['prefix']
        return prefix

    def bot_votes(self, response):
        data = response['data']
        votes = data['votes']
        return votes

    def bot_servers(self, response):
        data = response['data']
        servers = data['servers']
        return servers

    def bot_intro(self, response):
        data = response['data']
        intro = data['intro']
        return intro

    def bot_description(self, response):
        data = response['data']
        description = data['desc']
        return description

    def bot_web(self, response):
        data = response['data']
        web = data['web']
        return web

    def bot_git(self, response):
        data = response['data']
        git = data['git']
        return git

    def bot_URL(self, response):
        data = response['data']
        URL = data['url']
        return URL
    
    def bot_support_discord(self, response):
        data = response['data']
        support_discord = data['discord']
        return support_discord

    def bot_category(self, response):
        data = response['data']
        category = data['category']
        return category

    def bot_status(self, response):
        data = response['data']
        status = data['status']
        return status

    def bot_avatar(self, response):
        data = response['data']
        avatar = data['avatar']
        return avatar

    def bot_verified(self, response):
        data = response['data']
        verified = data['verified']
        return verified

    def bot_trusted(self, response):
        data = response['data']
        trusted = data['trusted']
        return trusted

    def bot_state(self, response):
        data = response['data']
        state = data['state']
        return state