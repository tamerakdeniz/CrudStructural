# 🎓 Course Management API

A FastAPI-based REST API for managing course information with CRUD operations.

## 🌟 Features

- Create new courses
- Retrieve all courses
- Get course by ID
- Filter courses by rating
- Filter courses by published date
- Update existing courses
- Delete courses

## 🔧 Requirements

- Python 3.x
- FastAPI
- Pydantic
- Starlette

## ⚡ Installation

1. Clone the repository:
```bash
git clone https://github.com/tamerakdeniz/CrudStructural.git
cd CrudStructural
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Endpoints

- `GET /courses` - Get all courses
- `GET /courses/{course_id}` - Get course by ID
- `GET /courses/rating/` - Get courses by rating
- `GET /courses/published/` - Get courses by published date
- `POST /create_courses` - Create a new course
- `PUT /courses/update_courses/` - Update an existing course
- `DELETE /courses/delete_courses/{course_id}` - Delete a course

## 📝 Example Course Object

```json
{
    "title": "Course Title",
    "instructor": "Tamer",
    "rating": 4.5,
    "published_date": 2020
}
```

## 📖 API Documentation

After running the application, you can access:
- Interactive API documentation at: `http://localhost:8000/docs`
- Alternative documentation at: `http://localhost:8000/redoc`
