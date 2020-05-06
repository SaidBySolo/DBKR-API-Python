# DBKR-API-Python

[![PyPI - Downloads](https://img.shields.io/pypi/dm/dbkrpy)](https://pypi.org/project/dbkrpy/)

## 사용하시기 전에 제발 읽어주세요

* 자동으로 루프를 돕니다 task.loop를 안만드셔도됩니다. (30분)

* 길드수도 안에서 체크합니다. 따로 비교안하셔도됩니다.

* 따로 루프를 만드시고싶으시다면 클래스내에 post_guild_count 라는 함수가 있습니다.

  * 인자값은 길드수와 토큰을 받으니 이 함수를 사용하세요.

## 설치 방법

```sh
pip install dbkrpy
```

## 업데이트 방법

```sh
pip install --upgrade dbkrpy
```

## GetById

불러올수 있는 항목 입니다.

* id(봇 아이디)
* timestamp(정보 생성일)
* name(봇 이름)
* owner(봇 개발자)
* library(봇 사용 라이브러리)
* prefix(봇 접두사)
* votes(봇 하트수)
* servers(봇 서버수)
* intro(봇 간단설명)
* description(봇 설명)
* web(봇 웹사이트)
* git(봇 깃)
* url(봇 초대링크)
* discord(봇 서포트 디스코드)
* categories(봇 카테고리)
* status(봇 상태)
* avatar(봇 프로필사진)
* verified(봇 디스코드 인증여부)
* trusted(봇 신뢰 여부)
* state(봇 잠금여부)

봇개발자,카테고리는 리스트로 반환됩니다.

## CheckVote

해당유저의 투표여부를 bool형식(True,False)로 반환합니다.

## Page

불러올수 있는 항목 입니다.

* idlist
* namelist
* serverslist
* voteslist
* introlist
* avatarlist
* categorylist
* taglist
* statelist

전부 리스트로 반환됩니다.

## 예제

### Cogs

```py
#Auto Loop
import dbkrpy
import discord
from discord.ext import commands

class GuildCount(commands.Cog):

    def __init__(self, bot):
        bot = bot
        token = 'DBKR Token paste here'
        dbkrpy.UpdateGuild(bot,token)

def setup(bot):
    bot.add_cog(GuildCount(bot))

```

### Bot(class)

```py
#Auto Loop
import discord
from discord.ext import commands
import dbkrpy

token = "bot token here"
DBKR_token = "DBKR Token here"

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="Prefix here")

if __name__ == '__main__':
    bot = Bot()
    dbkrpy.UpdateGuild(bot,DBKR_token)
    bot.run(token)
```

### Bot(not using class)

```py
#Auto Loop
import discord
from discord.ext import commands

token = "bot token here"
DBKR_token = "DBKR Token here"

bot = commands.Bot(command_prefix="Prefix here")

dbkrpy.UpdateGuild(bot,DBKR_token)

bot.run(token)
```

### Client(on_message)

```py
#Auto Loop
import dbkrpy
import discord

token = "bot token here"
DBKR = "Korean Bot token"

client = discord.Client()

dbkrpy.UpdateGuild(client,DBKR)

client.run(token)
```

### Cogs(Page)

```py
import dbkrpy
import discord
from discord.ext import commands

class BotPage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def getpage():
        page = await dbkrpy.Page.get_response(1)
        pagelist = Page(page)
        await ctx.send(f"{''.join(pagelist.idlist)}")

def setup(bot):
    bot.add_cog(BotPage(bot))
```

### Cogs(CheckVote)

```py
import dbkrpy
import discord
from discord.ext import commands

class ChkVote(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def getvote(self, ctx):
        token = "DBKR API token"
        userid = "user id"
        info = await dbkrpy.CheckVote.get_response(token,userid)
        dbkr = dbkrpy.CheckVote(info)
        await ctx.send(dbkr)

def setup(bot):
    bot.add_cog(Chkvote(bot))
```

## Patch note

### 0.4.1

* get_reponse함수가 classmethod에서 staticmethod로 변경되었습니다.

### 0.4.0

* 봇 페이지 확인가능

* 약간의 최적화

### 0.3.0

* 클래스명 변경

* 로깅출력 여부 설정가능

* 투표 여부 확인가능

### 0.2.1

* 핫픽스:모듈 임포트 오류 수정

### 0.2.0

* GetById 엔드포인트추가

### 0.1.2

* 독스트링 추가

### 0.1.1

* 1만서버 이상일시 오류출력.

### 0.1.0

* 첫 배포 시작
