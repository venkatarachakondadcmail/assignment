import psycopg2

def create_connection():
    conn = psycopg2.connect(
        host="assignmentvenkata.postgres.database.azure.com",
        port="5432",
        dbname="db.user",
        user="venkata",
        password="Sai@121993"
    )
    return conn

conn =create_connection()