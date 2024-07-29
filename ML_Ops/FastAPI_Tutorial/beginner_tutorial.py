from fastapi import FastAPI
from enum import Enum
app = FastAPI()
class availblecus(str,Enum):
    indian = 'indian'
    algerian = 'algerian'
food_items = {
    'indian' : ["Samosa","Dosa"],
    'algerian' :["kouskous","mhadjeb"]
}
@app.get("/get_items/{cuisine}")
async def get_items(cuisine: availblecus):
    return food_items.get(cuisine)
