from fastapi import FastAPI,HTTPException
from models import Student, UpdateStudent
from database import students_collection
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app=FastAPI(
    title="Student crud api",
    description="mongodb integration",
    version="1.0"
)

@app.post("/students")
def create_student(student:Student):
    existing_student=students_collection.find_one(
        {"email":student.email}
    )
    
    if existing_student:
        raise HTTPException(
            status_code=404,
            detail="email already exist"
        )
    result=students_collection.insert_one(
        student.dict()
    )
    return {'message':'student added succesfulllyyyyyyy',
            'id':str(result.inserted_id)}

@app.get("/students/{email}")
def get_student(email:str):
    student=students_collection.find_one(
        {"email":email}
    )
    if not student:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )
    return{
        "id":str(student["_id"]),
        "name":student["name"],
        "age":student["age"],
        "course":student["cousre"],
        "email":student["email"]
    }

#server static files
app.mount("/static",StaticFiles(directory="static"),name="static")

#home page
@app.get("/")
async def home():
    return FileResponse("static/index.html")

@app.get("/home")
def homepage():
    return {"message":"page found"}