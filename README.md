# DBKR-API-Python

[![PyPI - Downloads](https://img.shields.io/pypi/dm/dbkrpy)](https://pypi.org/project/dbkrpy/)

## 사용하시기 전에 제발 읽어주세요.

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

## 사용 예제들

### Cogs

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

### Bot(class)

```py
#Auto Loop
import discord
from discord.ext import commands
import dbkrpy

token = "bot token"
DBKR_token = "DBKR Token here"

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="&")
    

if __name__ == '__main__':
    bot = Bot()
    dbkrpy.DBKRPython(bot,DBKR_token)
    bot.run(token)
```

### Bot(not using class)

```py
#Auto Loop
import discord
from discord.ext import commands

token = "bot token"
DBKR_token = "DBKR Token here"

bot = commands.Bot(command_prefix="$")

dbkrpy.DBKRPython(bot,DBKR_token)
bot.run(token)
```

### on_message

```py
#Auto Loop
import dbkrpy
import discord

client = discord.Client()

token = "token"
DBKR = "Korean Bot token"

dbkrpy.DBKRPython(client,DBKR)

client.run(token)
```

## Patch note

### 0.1.2

* 독스트링 추가

### 0.1.1

* 1만서버 이상일시 오류출력.

### 0.1.0

* 첫 배포 시작
