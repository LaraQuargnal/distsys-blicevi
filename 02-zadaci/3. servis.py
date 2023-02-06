import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

# send the JSON data to "/storeData" 
async def store_data(session, result):
    async with session.post("http://0.0.0.0:8083/storeData", json=result) as resp:
        message = await resp.json()
        return message

@routes.post("/filterJoke")
async def filter_joke(request):
    try:
        # Read the JSON data from the request
        json_data = await request.json()

        # dict with joke data
        joke = {}
        joke["setup"] = json_data["setup"]
        joke["punchline"] = json_data["punchline"]
        result = {"data": {"joke": joke}}

        async with aiohttp.ClientSession() as session:
            message = await store_data(session, result)

        return web.json_response({"messages": message}, status=200)
    except Exception as e:
        return web.json_response({"serviceNumber":3, "messages": str(e)}, status=200)

app = web.Application()
app.router.add_routes(routes)

web.run_app(app, port=8082)
