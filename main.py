from fastapi import FastAPI
from DataModel.UserModel import UserModel
from Database.DatabaseOperations import Database
import os
import uvicorn

app = FastAPI()
db = Database( os.path.join(os.path.dirname(os.path.abspath(__file__)), "Database\\curd.db"))

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/create")
async def create_user(user: UserModel):
    try:
        query = "INSERT INTO users (name, lastName, address) VALUES (?, ?, ?)"
        db.conn.execute(query, (user.name, user.last_name, user.address))
        db.conn.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
   uvicorn.run("main:app", host="localhost", port=8000, reload=True)
   
