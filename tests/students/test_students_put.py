import json

import allure
import pytest

from utils.student_faker import generate_fake_update_student, fake_student_field_negative


@allure.story("Обновление полей для студента")
def test_student_update_field(api):
    with allure.step("Получение списка всех студентов"):
        response = api.students.get_students()

        allure.attach(
            str(response.status_code),
            name="Статус HTTP-ответа",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            json.dumps(response.json(), indent=4, ensure_ascii=False),
            name="JSON список студентов",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200

    students_response = response.json()

    with allure.step("Проверка наличия списка студентов в ответе"):
        assert "students" in students_response
        assert students_response["students"], "Список студентов пуст"

    with allure.step("Получение ID последнего студента"):
        last_student_id = students_response["students"][-1]["id"]
        allure.attach(
            str(last_student_id),
            name="ID первого студента",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Генерация данных для обновления студента"):
        new_student_data = generate_fake_update_student()

    with allure.step("Создание нового студента"):
        response = api.students.update_student(last_student_id, new_student_data)

        allure.attach(
            f"{response.request.method} {response.request.url}\n\nRequest Body: {new_student_data}",
            name="Запрос",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Проверка статуса ответа"):
        allure.attach(
            str(response.status_code),
            name="Статус ответа",
            attachment_type=allure.attachment_type.TEXT
        )
        assert response.status_code == 200

    with allure.step("Проверка JSON-ответа"):
        json_response = response.json()
        allure.attach(
            str(json_response),
            name="JSON-ответ",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка сообщения об успешном создании студента"):
        assert json_response["message"] == "Student updated successfully"

    with allure.step("Проверка наличия объекта 'student' в ответе"):
        assert "student" in json_response


@pytest.mark.parametrize(
    "field_name",
    ["email", "gender", "status"]
)
@allure.story("Создание нового студента (негативный тест с неправильным полем {field_name})")
def test_create_student_negative_phone(api, field_name):
    with allure.step("Получение списка всех студентов"):
        response = api.students.get_students()

        allure.attach(
            str(response.status_code),
            name="Статус HTTP-ответа",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            json.dumps(response.json(), indent=4, ensure_ascii=False),
            name="JSON список студентов",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200

    students_response = response.json()

    with allure.step("Проверка наличия списка студентов в ответе"):
        assert "students" in students_response
        assert students_response["students"], "Список студентов пуст"

    with allure.step("Получение ID последнего студента"):
        last_student_id = students_response["students"][-1]["id"]
        allure.attach(
            str(last_student_id),
            name="ID первого студента",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step(f"Генерация данных студента с неправильным {field_name}"):
        new_student_data = generate_fake_update_student()
        new_field = fake_student_field_negative()
        new_student_data[field_name] = new_field

    with allure.step(f"Попытка обновления студента с неправильным {field_name}"):
        response = api.students.update_student(last_student_id, new_student_data)

        allure.attach(
            f"{response.request.method} {response.request.url}\n\nRequest Body: {{}}",
            name="Запрос",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Проверка статуса ответа"):
        allure.attach(
            str(response.status_code),
            name="Статус ответа",
            attachment_type=allure.attachment_type.TEXT
        )
        assert response.status_code == 200

    with allure.step("Проверка JSON-ответа"):
        json_response = response.json()
        allure.attach(
            str(json_response),
            name="JSON-ответ",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка сообщения об ошибке"):
        assert "not updated" in json_response['message']


@pytest.mark.parametrize(
    "missing_field",
    [
        "name",
        "email",
        "gender",
        "status"
    ]
)
@allure.story("Обновление студента (негативный тест с отсутствием обязательного поля)")
def test_create_student_missing_required_field(api, missing_field):
    with allure.step("Получение списка всех студентов"):
        response = api.students.get_students()

        allure.attach(
            str(response.status_code),
            name="Статус HTTP-ответа",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            json.dumps(response.json(), indent=4, ensure_ascii=False),
            name="JSON список студентов",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200

    students_response = response.json()

    with allure.step("Проверка наличия списка студентов в ответе"):
        assert "students" in students_response
        assert students_response["students"], "Список студентов пуст"

    with allure.step("Получение ID последнего студента"):
        last_student_id = students_response["students"][-1]["id"]
        allure.attach(
            str(last_student_id),
            name="ID первого студента",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step(f"Генерация данных студента без обязательного поля {missing_field}"):
        new_student_data = generate_fake_update_student()
        del new_student_data[missing_field]

    with allure.step("Попытка обновления студента без обязательного поля"):
        response = api.students.update_student(last_student_id, new_student_data)

        allure.attach(
            f"{response.request.method} {response.request.url}\n\nRequest Body: {new_student_data}",
            name="Запрос",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Проверка статуса ответа"):
        allure.attach(
            str(response.status_code),
            name="Статус ответа",
            attachment_type=allure.attachment_type.TEXT
        )
        assert response.status_code == 200

    with allure.step("Проверка JSON-ответа"):
        json_response = response.json()
        allure.attach(
            str(json_response),
            name="JSON-ответ",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка сообщения об ошибке"):
        assert "not updated" in json_response['message']


@pytest.mark.parametrize(
    "missing_field",
    [
        "name",
        "email",
        "gender",
        "status"
    ]
)
@allure.story("Обновление данных студента (негативный тест с пустым обязательным полем)")
def test_create_student_with_empty_required_field(api, missing_field):
    with allure.step("Получение списка всех студентов"):
        response = api.students.get_students()

        allure.attach(
            str(response.status_code),
            name="Статус HTTP-ответа",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            json.dumps(response.json(), indent=4, ensure_ascii=False),
            name="JSON список студентов",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200

    students_response = response.json()

    with allure.step("Проверка наличия списка студентов в ответе"):
        assert "students" in students_response
        assert students_response["students"], "Список студентов пуст"

    with allure.step("Получение ID последнего студента"):
        last_student_id = students_response["students"][-1]["id"]
        allure.attach(
            str(last_student_id),
            name="ID первого студента",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step(f"Генерация данных студента с пустым полем {missing_field}"):
        new_student_data = generate_fake_update_student()
        new_student_data[missing_field] = ""

    with allure.step("Попытка обновления данных студента с пустым обязательным полем"):
        response = api.students.update_student(last_student_id, new_student_data)

        allure.attach(
            f"{response.request.method} {response.request.url}\n\nRequest Body: {new_student_data}",
            name="Запрос",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Проверка статуса ответа"):
        allure.attach(
            str(response.status_code),
            name="Статус ответа",
            attachment_type=allure.attachment_type.TEXT
        )
        assert response.status_code == 200

    with allure.step("Проверка JSON-ответа"):
        json_response = response.json()
        allure.attach(
            str(json_response),
            name="JSON-ответ",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка сообщения об ошибке"):
        assert "not updated" in json_response['message']








