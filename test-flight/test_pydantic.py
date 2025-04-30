from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

    @field_validator('age')
    def check_age(cls, v):
        if v < 18:
            raise ValueError('Age must be at least 18')
        return v

user_data = {
    'name': 'Yuli',
    'age': 27,
    'email': 'yuli@outlook.com'
}

try:
    user = User(**user_data)
    print(user)
except ValueError as e:
    print(e)
