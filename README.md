# DBKR-API-Python

**__파이썬 공식 SDK가 나왔습니다. [링크](https://github.com/koreanbots/py-sdk) 공식지원되는 패키지를 다운받으세요__**   
**빌드 0.5.1 이후에는 아카이브로 돌릴것이며, 지원을 장담해드릴수 없습니다.**  
**중요 크래쉬 부분은 아카이브를 풀고 수정 할것이지만, 이후 기능업데이트는 거의 없을것입니다.**  


[![Build Status](https://travis-ci.com/SaidBySolo/DBKR-API-Python.svg?branch=master)](https://travis-ci.com/SaidBySolo/DBKR-API-Python)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/dbkrpy)](https://pypi.org/project/dbkrpy/)

## 목차

* [설치방법](#설치방법)
* [업데이트방법](#업데이트방법)
* [GetById](#GetById)
* [CheckVote](#CheckVote)
* [Page](#Page)
* [예제](#예제)
* [Patch note](#patch-note)

## 사용하시기 전에 제발 읽어주세요

### UpdateGuilds 관련

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
* intro(봇 소개)
* description(봇 설명)
* web(봇 웹사이트)
* git(봇 깃)
* url(봇 초대링크)
* discord(봇 지원 디스코드 서버)
* categories(봇 카테고리)
* status(봇 상태)
* avatar(봇 프로필사진)
* verified(봇 디스코드 인증여부)
* trusted(봇 신뢰 여부)
* state(봇 잠금여부)

봇 개발자,카테고리는 리스트로 반환됩니다.

## CheckVote

해당 유저의 투표 여부를 bool 형식(True, False)으로 반환합니다.

## Page

불러올수 있는 항목 입니다.

* idlist(해당 페이지의 봇 id 리스트)
* namelist(해당 페이지의 봇 이름 리스트)
* serverslist(해당 페이지의 봇 서버수 리스트)
* voteslist(해당 페이지의 봇 투표 리스트)
* introlist(해당 페이지의 봇 소개 리스트)
* avatarlist(해당 페이지의 봇 아바타 리스트)
* categorylist(해당 페이지의 봇 카테고리 리스트)
* taglist(해당 페이지의 봇 태그 리스트)
* statelist(해당 페이지의 봇 상태 리스트)

전부 투표수가 많은 순서대로 10개씩 리스트로 반환됩니다.

## 예제

### 예제 빠른이동

* [Cogs(UpdateGuild)](#Cogs(UpdateGuild))
* [Bot(Using class,UpdateGuilds](#botnot-using-classupdateguilds)
* [Bot(Not using class,UpdateGuilds)](#botnot-using-classupdateguilds)
* [Client(on_message,UpdateGuilds)](#clientonmessageupdateguilds)
* [Cogs(GetById)](#cogsgetbyid)
* [Cogs(Page)](#cogspage)
* [Cogs(CheckVote)](#cogscheckvote)

### Cogs(UpdateGuilds)

```py
#Auto Loop
import dbkrpy
import discord
from discord.ext import commands

class GuildCount(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = 'DBKR Token paste here'
        dbkrpy.UpdateGuilds(self.bot,self.token)

def setup(bot):
    bot.add_cog(GuildCount(bot))

```

### Bot(Using class,UpdateGuilds)

```py
#Auto Loop
import discord
from discord.ext import commands
import dbkrpy

token = "bot token here"
DBKR_token = "DBKR Token paste here"

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="Prefix here")

if __name__ == '__main__':
    bot = Bot()
    dbkrpy.UpdateGuilds(bot,DBKR_token)
    bot.run(token)
```

### Bot(Not using class,UpdateGuilds)

```py
#Auto Loop
import dbkrpy
import discord
from discord.ext import commands

token = "bot token here"
DBKR_token = "DBKR Token paste here"

bot = commands.Bot(command_prefix="Prefix here")

dbkrpy.UpdateGuilds(bot,DBKR_token)

bot.run(token)
```

### Client(on_message,UpdateGuilds)

```py
#Auto Loop
import dbkrpy
import discord

token = "bot token here"
DBKR_token = "DBKR Token paste here"

client = discord.Client()

dbkrpy.UpdateGuilds(client,DBKR_token)

client.run(token)
```

### Cogs(GetById)

```py
import dbkrpy
import discord
from discord.ext import commands

class DBKRinfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def getinfo(self, ctx):
        info = await dbkrpy.GetById.get_response(538659580855451648)
        dbkr = dbkrpy.DBKRGetById(info)
        await ctx.send(dbkr.id)

def setup(bot):
    bot.add_cog(DBKRinfo(bot))
```

### Cogs(Page)

```py
import dbkrpy
import discord
from discord.ext import commands

class DBKRPage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def getpage():
        page = await dbkrpy.Page.get_response(1)
        pagelist = Page(page)
        await ctx.send(f"{''.join(pagelist.idlist)}")

def setup(bot):
    bot.add_cog(DBKRPage(bot))
```

### Cogs(CheckVote)

```py
import dbkrpy
import discord
from discord.ext import commands

class DBKRChkVote(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def getvote(self, ctx):
        token = "DBKR API token"
        userid = "user id"
        info = await dbkrpy.CheckVote.get_response(token,userid)
        dbkr = dbkrpy.CheckVote(info)
        await ctx.send(dbkr.check)

def setup(bot):
    bot.add_cog(DBKRChkVote(bot))
```

## Patch note

### 0.5.2

* 파이썬 3.6지원

### 0.5.1

* API 주소변경(Thx to chaemoong)

### 0.5.0

* 카테고리 검색 엔드포인트 래핑

* 검색 엔드포인트 래핑

* 페이지는 지금부터 기본으로 1페이지로 검색됩니다.

* 파일 이름들이 변경되었습니다.

### 0.4.5

* 핫픽스:UpdateGuilds에 post_guild_count함수 staticmethod로 변경

### 0.4.4

* 핫픽스:패키지에서 클래스 이름 변경으로 UpdateGuilds가 임포트 되지않았던 문제

### 0.4.3

* api링크 dict로 분리

### 0.4.2

* UpdateGuild 클래스가 UpdateGuilds로 변경

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

* 핫픽스: 모듈 임포트 오류 수정

### 0.2.0

* GetById 엔드포인트추가

### 0.1.2

* 독스트링 추가

### 0.1.1

* 1만서버 이상일시 오류출력.

### 0.1.0

* 첫 배포 시작
