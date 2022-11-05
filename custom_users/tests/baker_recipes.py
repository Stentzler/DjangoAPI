from model_bakery.recipe import Recipe
from addresses.models import Address
from grades.models import Grade
from custom_users.models import Student, Teacher

student_custom = Recipe(
    Student,
    username = "student",
    rg = "999-999-999",
    first_name = "Stu",
    last_name = "Dent",
    age = 22,
    contacts = "Dona Angela",
    email = "student@mail.com",
    password = "1234",
)

teacher_custom = Recipe(
    Teacher,
    username = "teacher",
    rg = "999-999-999",
    first_name = "Tea",
    last_name = "Cher",
    age = 18,
    contacts = "Dona Angela",
    email = "teacher@mail.com",
    password = "1234",
    cpf = '12345678910'
)