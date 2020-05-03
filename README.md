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
import dbkrpy
import discord
from discord.ext import commands

class UpdateGuild(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = 'Token paste here'
        dbkrpy.DBKRPython(bot=self.bot,token=self.token)

def setup(bot):
    bot.add_cog(UpdateGuild(bot))

```

## Patch note

### 0.1.0

* 첫 배포 시작
