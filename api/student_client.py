from api.endpoints import StudentsEndpoints

class StudentsClient:
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def get_students(self):
        self.logger.info("GET /student")
        response = self.client.get(StudentsEndpoints.GET)

        self.logger.info(
            f"Response: {response.status_code}"
        )
        return response

    def get_student(self, student_id):
        self.logger.info(f"GET /student/{student_id}")
        response = self.client.get(StudentsEndpoints.GET_STUDENT(student_id))

        self.logger.info(
            f"Response: {response.status_code}"
        )
        return response

    def create_student(self, student_data):
        self.logger.info("POST /student")
        response = self.client.post(StudentsEndpoints.CREATE, data=student_data)

        self.logger.info(
            f"JSON Payload: {student_data}"
        )

        self.logger.info(
            f"Response: {response.status_code}"
        )

        self.logger.info(
            f"JSON Response: {response.json() if response.content else 'No Content'}"
        )

        return response

    def update_student(self, student_id, student_data):
        self.logger.info(f"PUT /student/{student_id}")
        response = self.client.put(StudentsEndpoints.UPDATE(student_id), json=student_data)

        self.logger.info(
            f"JSON Payload: {student_data}"
        )

        self.logger.info(
            f"Response: {response.status_code}"
        )

        self.logger.info(
            f"JSON Response: {response.json() if response.content else 'No Content'}"
        )

        return response

    def delete_student(self, student_id):
        self.logger.info("DELETE /student")
        response = self.client.delete(StudentsEndpoints.DELETE(student_id))

        self.logger.info(
            f"Response: {response.status_code}"
        )
        return response