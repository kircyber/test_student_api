

class Api:
    def __init__(self, client):
        self.students = StudentsClient(
            client
        )