from fastapi import FastAPI
from Routers import Auth, Todos, Admin, Users
import Models
from Database import engine

app = FastAPI()

Models.Base.metadata.create_all(engine)

app.include_router(Auth.router)
app.include_router(Todos.router)
app.include_router(Admin.router)
app.include_router(Users.router)