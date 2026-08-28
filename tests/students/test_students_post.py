import allure
import pytest

from utils.student_faker import generate_fake_student, fake_student_field_negative


@allure.story("Создание нового студента")
def test_create_student(api):
    with allure.step("Генерация данных нового студента"):
        new_student_data = generate_fake_student()

    with allure.step("Создание нового студента"):
        response = api.students.create_student(new_student_data)

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
        assert json_response["message"] == "Student created successfully"

    with allure.step("Проверка наличия объекта 'student' в ответе"):
        assert "student" in json_response



@pytest.mark.parametrize(
    "invalid_phone",
    [
        "12345",
        "abcdefghij",
        "+1 (234) 567-890",
        "123-456-7890",
        "12345678901234567890",
    ],)
@allure.story("Создание нового студента (негативный тест с неправильным номером телефона)")
def test_create_student_negative_phone(api, invalid_phone):
    with allure.step(f"Генерация данных нового студента с неправильным номером телефона: {invalid_phone}"):
        new_student_data = generate_fake_student()
        new_student_data["phone_no"] = invalid_phone

    with allure.step("Попытка создания студента с неправильным номером телефона"):
        response = api.students.create_student(new_student_data)

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
        assert response.status_code == 400

    with allure.step("Проверка JSON-ответа"):
        json_response = response.json()
        allure.attach(
            str(json_response),
            name="JSON-ответ",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка сообщения об ошибке"):
        assert "error" in json_response


@pytest.mark.parametrize(
    "field_name",
    ["email", "gender", "status"]
)
@allure.story("Создание нового студента (негативный тест с неправильным полем {field_name})")
def test_create_student_negative_phone(api, field_name):
    with allure.step(f"Генерация данных нового студента с неправильным {field_name}"):
        new_student_data = generate_fake_student()
        new_field = fake_student_field_negative()
        new_student_data[field_name] = new_field

    with allure.step("Попытка создания студента с неправильным email"):
        response = api.students.create_student(new_student_data)

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
        assert response.status_code == 400

    with allure.step("Проверка JSON-ответа"):
        json_response = response.json()
        allure.attach(
            str(json_response),
            name="JSON-ответ",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка сообщения об ошибке"):
        assert "error" in json_response


@pytest.mark.parametrize(
    "missing_field",
    [
        "name",
        "email",
        "phone_no",
        "gender",
        "status"
    ]
)
@allure.story("Создание нового студента (негативный тест с отсутствием обязательного поля)")
def test_create_student_missing_required_field(api, missing_field):
    with allure.step("Генерация данных нового студента без обязательного поля 'first_name'"):
        new_student_data = generate_fake_student()
        del new_student_data[missing_field]

    with allure.step("Попытка создания студента без обязательного поля"):
        response = api.students.create_student(new_student_data)

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
        assert response.status_code == 400

    with allure.step("Проверка JSON-ответа"):
        json_response = response.json()
        allure.attach(
            str(json_response),
            name="JSON-ответ",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка сообщения об ошибке"):
        assert "error" in json_response


@pytest.mark.parametrize(
    "missing_field",
    [
        "name",
        "email",
        "phone_no",
        "gender",
        "status"
    ]
)
@allure.story("Создание нового студента (негативный тест с пустым обязательным полем)")
def test_create_student_with_empty_required_field(api, missing_field):
    new_student_data = generate_fake_student()
    new_student_data[missing_field] = ""

    with allure.step("Попытка создания студента с пустым обязательным полем"):
        response = api.students.create_student(new_student_data)

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
        assert response.status_code == 400

    with allure.step("Проверка JSON-ответа"):
        json_response = response.json()
        allure.attach(
            str(json_response),
            name="JSON-ответ",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка сообщения об ошибке"):
        assert "error" in json_response
