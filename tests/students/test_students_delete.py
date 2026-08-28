import allure
import json

import pytest


@allure.story("Удаление студента (позитивный сценарий")
def test_student_delete(api):
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

    with allure.step("Удаление последнего студента с ID {last_student_id}"):
        response = api.students.delete_student(student_id=last_student_id)

        allure.attach(
            f"{response.request.method} {response.request.url}",
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

    with allure.step("Проверка сообщения об успешном удалении студента"):
        assert json_response["message"] == "Student deleted successfully"



@pytest.mark.parametrize(
    "invalid_student_id",
    [
        "invalid_id",
        "124sfdsaf1343",
        "!@#$%^&*()",
        "-235",
        ""
    ])
@allure.story("Удаление студента (негативный сценарий)")
def test_student_delete_negative(api, invalid_student_id):
    with allure.step(f"Удаление последнего студента с ID {invalid_student_id}"):
        response = api.students.delete_student(student_id=invalid_student_id)

        allure.attach(
            f"{response.request.method} {response.request.url}",
            name="Запрос",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Проверка статуса ответа"):
        allure.attach(
            str(response.status_code),
            name="Статус ответа",
            attachment_type=allure.attachment_type.TEXT
        )
        assert response.status_code == 404