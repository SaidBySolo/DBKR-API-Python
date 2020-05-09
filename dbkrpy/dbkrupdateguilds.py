import aiohttp
import asyncio
from .dbkrapiurl import PostURL

class UpdateGuilds:
    def __init__(self, bot, token, log=True):
        """
        클래스 입니다.

        해당 클래스에 인자값을 주시면

        ``main_loop`` 함수가 봇이 꺼질때 까지 루프를 돌아서

        ``post_guild_count``함수를 이용해서 post 요청을 보냅니다.

        log는 로깅 여부입니다 기본값은 True입니다.
        """
        self.bot = bot
        self.token = token
        loop = asyncio.get_event_loop()
        loop.create_task(self.main_loop(bot, token, log))
    
    async def main_loop(self, bot, token, log):
        """
        메인 루프 함수입니다

        봇종료 전까지 30분마다 post_guild_count를 이용해서 post요청을합니다.
        
        서버수 동일,성공 요청이 아닐시 ``Exception``을 ``raise``합니다.
        """
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            guilds = len(self.bot.guilds)
            getres = await self.post_guild_count(token,guilds)
            code = getres['code']
            if code == 200:
                if log is True:
                    print(f"서버수를 성공적으로 갱신했어요! 현재 서버수는 {guilds}이네요.")
                    await asyncio.sleep(1800)
                else:
                    await asyncio.sleep(1800)
            else:
                msg = getres['message']
                try:
                    name = msg['name']
                except TypeError:
                    if msg.startswith('1'):
                        raise Exception(f"오류코드 : {code} | {msg}")
                    else:
                        if log is True:
                            print("서버수가 동일하네요. 잠시후에 다시요청할께요!")
                            await asyncio.sleep(1800)
                        else:
                            await asyncio.sleep(1800)
                else:
                    message = msg['message']
                    raise Exception(f"오류코드 : {code} | {name} : {message}")

    @staticmethod
    async def post_guild_count(token, guild_count):
        """
        post 요청 함수입니다.

        해당 함수를 직접 사용하실경우
        
        ``token``과 ``사용서버수``를 인자값으로 주셔야합니다.
        """
        URL = PostURL['dbkrpostguild']
        headers = {"token":token,"content-type":"application/json"}
        data = {'servers':guild_count}
        async with aiohttp.ClientSession() as cs:
            async with cs.post(URL, headers=headers, json=data) as r:
                response = await r.json()
                return response