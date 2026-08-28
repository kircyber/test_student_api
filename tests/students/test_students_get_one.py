import json

import allure
import pytest


@allure.story("Получение данных первого студента")
def test_students_get_one(api):
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



    with allure.step("Получение ID первого студента"):
        first_student_id = students_response["students"][0]["id"]
        allure.attach(
            str(first_student_id),
            name="ID первого студента",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step(f"Получение данных первого студента с ID {first_student_id}"):
        response = api.students.get_student(student_id=first_student_id)

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
            json.dumps(json_response, indent=4, ensure_ascii=False),
            name="JSON-ответ на получение данных студента",
            attachment_type=allure.attachment_type.JSON
        )


    with allure.step("Проверка равенства ID студента в ответе и в запросе"):
        assert json_response["student"]["id"] == first_student_id, f"ID студента в ответе ({json_response['id']}) не совпадает с ID в запросе ({first_student_id})"




@pytest.mark.parametrize("invalid_student_id", ["invalid_id", "124sfdsaf1343", "!@#$%^&*()", "-235", ""])
@allure.story("Попытка получения данных студента с некорректным ID")
def test_students_get_one_negative(api, invalid_student_id):

    with allure.step(f"Попытка получения данных студента с некорректным ID {invalid_student_id}"):
        response = api.students.get_student(student_id=invalid_student_id)

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
        assert response.status_code == 404, f"Ожидался статус 404, но получен {response.status_code}"



