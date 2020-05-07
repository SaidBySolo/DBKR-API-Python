import dbkrpy
import os
import asyncio

token = os.environ['token']
botid = os.environ['bot_id']
userid = os.environ['user_id']

checklist=[]

async def checkall():
    try:
        await dbkrpy.CheckVote.get_response(token,userid)
    except Exception:
        checklist.append("CB")
    else:
        pass
    
    try:
        await dbkrpy.GetById.get_response(botid)
    except Exception:
        checklist.append("GBI")
    else:
        pass

    try:
        await dbkrpy.Page.get_response(1)
    except Exception:
        checklist.append("P")
    else:
        pass
    
    try:
        await dbkrpy.UpdateGuilds.post_guild_count(token,userid)
    except Exception:
        checklist.append("UG")
    else:
        pass

    assert(checklist == 0)

loop = asyncio.get_event_loop()
loop.run_until_complete(checkall())