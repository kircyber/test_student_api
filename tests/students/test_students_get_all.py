import json

import allure

@allure.feature("Студенты")
@allure.story("Получение списка всех студентов")
def test_students_get_all(api):
    with allure.step("Получение списка всех студентов"):
        response = api.students.get_students()

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
            json.dumps(json_response),
            name="JSON-ответ",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка наличия объекта 'students' в ответе"):
        assert "students" in json_response