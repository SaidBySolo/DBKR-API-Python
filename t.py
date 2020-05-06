from dbkrpy.dbkrpage import Page
import asyncio

async def main():
    asdf = await Page.get_response(1)
    lol = Page(asdf)
    print(lol.idlist)

asyncio.run(main())