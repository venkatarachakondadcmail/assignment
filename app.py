import streamlit as st
import psycopg2

# Connect to the PostgreSQL database
def create_connection():
    conn = psycopg2.connect(
        host="assignmentvenkata-server.postgres.database.azure.com",
        port="5432",
        dbname="ssignmentvenkata-database",
        user="vtnlmpluiw",
        password="Sai@121993"
    )
    return conn


# Define Streamlit app
def main():
    st.title("Streamlit App with PostgreSQL on Azure")
    conn = create_connection()
    st.write("Connected!")

if __name__ == '__main__':
    main()
