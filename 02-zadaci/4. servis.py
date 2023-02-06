import aiosqlite
from aiohttp import web

routes = web.RouteTableDef()

# Temp list to store user and joke data
temp_users = []
temp_jokes = []

@routes.post("/storeData")
async def store_data(request):
    global temp_users, temp_jokes
    json_data = await request.json()

    # get user and joke from JSON
    user_data = json_data.get("data", {}).get("user", {})
    joke_data = json_data.get("data", {}).get("joke", {})

    if user_data and joke_data:
        db_input = {**user_data, **joke_data}  #combine in one dict
    
        #insert the combined data
        async with aiosqlite.connect("06/data-store.db") as db:
            await db.execute("INSERT INTO UsersJoke (name,city,username,setup,punchline) VALUES (?,?,?,?,?)", (db_input["name"],db_input["city"],db_input["username"],db_input["setup"],db_input["punchline"]))
            await db.commit()
    
        # count the number of rows
        async with aiosqlite.connect("06/data-store.db") as db:
            async with db.execute("SELECT * FROM UsersJoke") as cur:
                result = len(await cur.fetchall())

        message = {"status":"ok","data":{"numberOfRowsInTable":result}}
        return web.json_response(message, status=200)
    else:
        message = {"status":"Failed","message":"User or Joke not present"}
        return web.json_response(message, status=400)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8083)
