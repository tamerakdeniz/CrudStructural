from idlelib.squeezer import count_lines_with_wrapping

from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Course:
    id: int
    title: str
    instructor: str
    rating: float
    published_date: int

    def __init__(self, id, title, instructor, rating, published_date):
        self.id = id
        self.title = title
        self.instructor = instructor
        self.rating = rating
        self.published_date = published_date

class CourseRequest(BaseModel):
    id: Optional[int] = Field(description="ID of the course, optional", default=None)
    title: str = Field(min_length=3, max_length=100, description="Title of the course")
    instructor: str = Field(min_length=3, description="Instructor of the course")
    rating: float = Field(gt=0, lt=6, description="Rating of the course")
    published_date: int = Field(gt=1990, lt=2040, description="Published date of the course")

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Course Title",
                "instructor": "Tamer",
                "rating": 4.5,
                "published_date": 2020
            }
        }
    }

courses_db = [
    Course(1, "Python", "Tamer", 4.5, 2020),
    Course(2, "Java", "David", 4.0, 2025),
    Course(3, "C++", "Smith", 1, 2018),
    Course(4, "Machine Learning", "John", 5.0, 2029),
    Course(5, "Deep Learning", "Carlos", 3.5, 2033),
    Course(6, "FastAPI", "Maria", 2.5, 2012),
]

@app.get("/courses", status_code=status.HTTP_200_OK)
async def get_all_courses():
    return courses_db

@app.get("/courses/{course_id}", status_code=status.HTTP_200_OK)
async def get_course_by_id(course_id: int = Path(gt=0)):
    for course in courses_db:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

@app.get("/courses/rating/", status_code=status.HTTP_200_OK)
async def get_courses_by_rating(course_rating: float = Query(gt=0, lt=6)):
    courses_to_return = []
    for course in courses_db:
        if course.rating == course_rating:
            courses_to_return.append(course)
    return courses_to_return

@app.get("/courses/published/", status_code=status.HTTP_200_OK)
async def get_courses_by_published_date(course_published_date: int = Query(gt=2000, lt=2024)):
    courses_to_return = []
    for course in courses_db:
        if course.published_date == course_published_date:
            courses_to_return.append(course)
    return courses_to_return

@app.post("/create_courses", status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    new_course = Course(**course_request.model_dump())
    courses_db.append(find_course_by_id(new_course))


def find_course_by_id(course: Course):
    course.id = 1 if len(courses_db) == 0 else courses_db[-1].id + 1
    return course

@app.put("/courses/update_courses/", status_code=status.HTTP_204_NO_CONTENT)
async def update_course(course_request: CourseRequest):
    course_updated = False
    for i in range(len(courses_db)):
        if courses_db[i].id == course_request.id:
            courses_db[i] = course_request
            course_updated = True
    if not course_updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")

@app.delete("/courses/delete_courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int = Path(gt=0)):
    course_deleted = False
    for i in range(len(courses_db)):
        if courses_db[i].id == course_id:
            courses_db.pop(i)
            course_deleted = True
    if not course_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
