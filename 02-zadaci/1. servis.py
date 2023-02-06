import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/getJokes")
async def get_jokes(req):
    async with aiohttp.ClientSession() as session:

        # send 4 get requests
        jokes_tasks = [asyncio.create_task(session.get(f"https://official-joke-api.appspot.com/random_joke")) for _ in
                       range(4)]
        users_tasks = [asyncio.create_task(session.get(f"https://randomuser.me/api/")) for _ in range(4)]
        final_results = await asyncio.gather(*jokes_tasks, *users_tasks)
        final_results = [await r.json() for r in final_results]

    async with aiohttp.ClientSession() as session:

        # split final result in half
        half = len(final_results) // 2
        users_tasks = [asyncio.create_task(session.post("http://0.0.0.0:8081/filterUser", json=final_results[i])) for i
                       in range(half)]
        jokes_tasks = [asyncio.create_task(session.post("http://0.0.0.0:8082/filterJoke", json=final_results[half + i]))
                       for i in range(half)]
        final_results = await asyncio.gather(*users_tasks, *jokes_tasks)
        final_results = [await r.json() for r in final_results]

    return web.json_response({"results": final_results}, status=200)


app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8080)
