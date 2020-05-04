# DBKR-API-Python

## 설치 방법

```sh
pip install dbkrpy
```

## 업데이트 방법

```sh
pip install --upgrade dbkrpy
```

## 사용 예제

```py
#Auto Loop
import dbkrpy
import discord
from discord.ext import commands

class UpdateGuild(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = 'KoreanBot Token paste here'
        dbkrpy.DBKRPython(self.bot,self.token)

def setup(bot):
    bot.add_cog(UpdateGuild(bot))

```

## on_message
```py
#Auto Loop
import asyncio
import dbkrpy
import discord

client = discord.Client()

token = "token"
DBKR = "Korean Bot token"

dbkrpy.DBKRPython(client,DBKR)
```

## Patch note

### 0.1.1

* 1만서버 이상일시 오류출력.

### 0.1.0

* 첫 배포 시작
