
from . import connection
import streamlit as st
import joblib
from .models import predictor
from . import hasher as h

def insert_mail_content(from_email, subject, message, to_email):
   
    # make predictions on new data
    y_pred = predictor.predict(message)
    print('y_pred', y_pred)
    cur = connection.conn.cursor()
    # cur.execute("INSERT INTO TB_MAIL (login, mail_content, to_login) VALUES (%s, %s, %s)", (from_email, message, to_email))
    cur.execute("""
    INSERT INTO TB_MAIL (login, mail_content, to_login, user_id, spam)
    SELECT %s, %s, %s, user_id, %s FROM TB_USERS WHERE login = %s
""", (from_email, message, to_email,str(y_pred),from_email))
    connection.conn.commit()
    cur.close()

def insert_user(login, password):
    # Insert the new user into the database
    password = h.encrypt_password(password)
    cur = connection.conn.cursor()
    cur.execute("INSERT INTO TB_USERS (login, password) VALUES (%s, %s)", (login, password))
    connection.conn.commit()
    cur.close()
    

def get_all_mails(login):
    try:
        if login:
            # Execute your SQL statement
            connection.conn.commit()
            cur = connection.conn.cursor()
            qry = "SELECT * FROM TB_MAIL WHERE to_login = '{0}'".format(str(login))
            cur.execute(qry)
            results = cur.fetchall()
            cur.close()
            return results
    
    except Exception as e:
        # Handle all other exceptions here
        connection.conn.rollback()
        print(f"Error: {e}")
        return None
