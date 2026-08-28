class StudentsEndpoints:
    GET = f"/students"
    GET_STUDENT = lambda student_id: f"/student/{student_id}"
    CREATE = f"/student"
    DELETE = lambda student_id: f"/student/{student_id}"
    UPDATE = lambda student_id: f"/student/{student_id}"

