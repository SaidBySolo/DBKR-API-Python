import aiohttp
import asyncio


class DBKRPython:
    def __init__(self, bot, token):
        self.bot = bot
        self.token = token
        loop = asyncio.get_event_loop()
        loop.create_task(self.dbkrpy(bot,token))
    
    async def dbkrpy(self, bot, token):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            guilds = len(self.bot.guilds)
            getres = await self.post_guild_count(token,guilds)
            code = getres['code']
            if code == 200:
                print(f"서버수를 성공적으로 갱신했어요! 현재 서버수는 {guilds}네요.")
                await asyncio.sleep(1800)
            else:
                msg = getres['message']
                try:
                    name = msg['name']
                except TypeError:
                    if msg.startswith('1'):
                        raise Exception(f"오류코드 : {code} | {msg}")
                    else:
                        print("서버수가 동일하네요. 잠시후에 다시요청할께요!")
                        await asyncio.sleep(1800)
                else:
                    message = msg['message']
                    raise Exception(f"오류코드 : {code} | {name} : {message}")

    async def post_guild_count(self, token, guild_count):
        URL = 'https://api.koreanbots.cf/bots/servers'
        headers = {"token":token,"content-type":"application/json"}
        data = {'servers':guild_count}
        async with aiohttp.ClientSession() as cs:
            async with cs.post(URL, headers=headers, json=data) as r:
                response = await r.json()
                return response