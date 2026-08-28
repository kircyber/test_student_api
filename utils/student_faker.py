import random

from faker import Faker

fake = Faker("en_US")

def fake_student_name():
    return fake.name()

def fake_student_email():
    return fake.email()

def fake_student_field_negative():
    return fake.sentence(nb_words=3)

def fake_student_phone():
    return f"+7999{random.randint(1000000, 9999999):07d}"

def fake_student_phone_negative():
    return fake.phone_number()


def generate_fake_student():
    return {
        "name": fake_student_name(),
        "email": fake_student_email(),
        "phone_no": fake_student_phone(),
        "gender": fake.random_element(elements=("male", "female")),
        "status": 1
    }


def generate_fake_update_student():
    return {
            "email": fake_student_email(),
            "gender": fake.random_element(elements=("male", "female")),
            "name": fake_student_name(),
            "status": fake.random_element(elements=(0, 1))
        }