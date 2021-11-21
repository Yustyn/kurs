import psycopg2
from settings import *

connection = psycopg2.connect(
    user=USER, password=PASSWORD, host=HOST, port=PORT, database="happy_smile_db"
)

cursor = connection.cursor()


person_roles = """CREATE TABLE person_roles(
    id SERIAL PRIMARY KEY,
    role_name varchar(50) NOT NULL
)"""
cursor.execute(person_roles)
connection.commit()

persons = """CREATE TABLE persons(
    id SERIAL PRIMARY KEY NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    phone_number varchar(12) NOT NULL,
    role INT REFERENCES person_roles(id),
    gender varchar(50) NOT NULL,
    birth_date DATE NOT NULL,
    registration_date DATE NOT NULL,
    discount int,
    city varchar(50) NOT NULL,
    allergy varchar(500),
    disease varchar(500)
)"""
cursor.execute(persons)
connection.commit()

visits = """CREATE TABLE visits(
    id SERIAL PRIMARY KEY,
    person_id INT REFERENCES persons(id),
    visit_date DATE NOT NULL,
    doctor INT REFERENCES persons(id),
    time_of_reception DATE NOT NULL,
    duration_of_reception INT NOT NULL,
    description varchar(500),
    treatment_cost int NOT NULL,
    img varchar(500)
)"""
cursor.execute(visits)
connection.commit()


cursor.close()
connection.close()
