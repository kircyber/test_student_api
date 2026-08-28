import json

import allure

@allure.story("Получение данных первого студента")
def test_students_get_one(api, logger):
    logger.info("Начало теста")
    with allure.step("Получение списка всех студентов"):

        logger.info("Отправка GET запроса на получение списка студентов")
        response = api.students.get_students()

        logger.info(
            f"Получен ответ. Status code: {response.status_code}"
        )


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
            logger.info("Статус ответа проверен: 200")


    students_response = response.json()


    logger.info(
        f"Получен JSON: {json.dumps(students_response, ensure_ascii=False)}"
    )

    with allure.step("Проверка наличия списка студентов в ответе"):
        assert "students" in students_response
        assert students_response["students"], "Список студентов пуст"

        logger.info("Объект 'students' присутствует в ответе")


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



    allure.attach(
        log_content,

    )



