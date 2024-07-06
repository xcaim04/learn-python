from fastapi import FastAPI
from pydantic import BaseModel # Definir una entidad users

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str

userlist = [User(id=4, name='Carlos', surname='Javier', age=19, url='https://carlosblanco.dev'),
        User(id=44 ,name='Javier', surname='Andres', age=10, url='https://javierblanco.dev')]


""" Search a user by an id on userlist[] """

def search_user(ID: int) -> User:
    my_users = filter(lambda user: user.id == ID, userlist)
    
    try:
        return list(my_users)[0]
    except:
        return {'error': 'Not found 404'}


@app.get('/users')
async def users():
    return userlist


# Query => url.../?user_id=1/
@app.get("/user")
async def user(user_id: int):
    return search_user(user_id)


# Path => url.../userquery/4
@app.get("/userquery/{user_id}")
async def user(user_id: int):
    return search_user(user_id)


@app.post("/addUser/")
async def addUser(userToAdd: User):
    if type(search_user(userToAdd.id)) == User:
        return {'error': 'User already exists'}
    else:
        userlist.append(userToAdd)

@app.put("/updateUser/")
async def updateUser(user: User):

    found = False
    for index, saved_user in enumerate(userlist):
        if saved_user.id == user.id:
            userlist[index] = user
            found = True
    if found:
        return list(user)[0]
    return {"error": "User not found"}
    