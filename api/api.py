from api.student_client import StudentsClient

class Api:
    def __init__(self, client, logger):
        self.students = StudentsClient(
            client, logger
        )