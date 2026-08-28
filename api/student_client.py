from endpoints import StudentsEndpoints

class StudentsClient:
    def __init__(self, client):
        self.client = client

    def get_students(self):
        response = self.client.get(StudentsEndpoints.GET)
        return response.json()

    def get_student(self, student_id):
        response = self.client.get(StudentsEndpoints.GET_STUDENT(student_id))
        return response.json()

    def create_student(self, student_data):
        response = self.client.post(StudentsEndpoints.CREATE, json=student_data)
        return response.json()

    def update_student(self, student_id, student_data):
        response = self.client.put(StudentsEndpoints.UPDATE(student_id), json=student_data)
        return response.json()

    def delete_student(self, student_id):
        response = self.client.delete(StudentsEndpoints.DELETE(student_id))
        return response.status_code == 204