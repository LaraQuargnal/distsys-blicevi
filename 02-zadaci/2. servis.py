import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

# send Json to /storeData
async def store_data(session, result):
    async with session.post("http://0.0.0.0:8083/storeData", json=result) as resp:
        message = await resp.json()
        return message

@routes.post("/filterUser")
async def filter_user(request):
    try:
        json_data = await request.json()

        # create dict
        user = {}
        data = json_data["results"][0]
        user["name"] = f"{data['name']['first']} {data['name']['last']}"
        user["city"] = data["location"]["city"]
        user["username"] = data["login"]["username"]
        result = {"data": {"user": user}}

        # send it to /storeData
        async with aiohttp.ClientSession() as session:
            message = await store_data(session, result)
        return web.json_response({"messages": message}, status=200)
    except Exception as e:
        return web.json_response({"serviceNumber":2,"messages": str(e)}, status=200)

app = web.Application()
app.router.add_routes(routes)

web.run_app(app, port=8081)
