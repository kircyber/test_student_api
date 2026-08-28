class StudentsClient:
    def __init__(self, client):
        self.client = client

    def get_student(self, student_id):
        response = self.client.get(f"/students/{student_id}")
        return response.json()

    def create_student(self, student_data):
        response = self.client.post("/students", json=student_data)
        return response.json()

    def update_student(self, student_id, student_data):
        response = self.client.put(f"/students/{student_id}", json=student_data)
        return response.json()

    def delete_student(self, student_id):
        response = self.client.delete(f"/students/{student_id}")
        return response.status_code == 204