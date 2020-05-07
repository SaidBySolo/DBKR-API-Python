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
    try:
        await dbkrpy.GetById.get_response(botid)
    except Exception:
        checklist.append("GBI")
    try:
        await dbkrpy.Page.get_response(1)
    except Exception:
        checklist.append("P")
    try:
        await dbkrpy.UpdateGuilds.post_guild_count(token,userid)
    except Exception:
        checklist.append("UG")
    assert(len(checklist) == 0)