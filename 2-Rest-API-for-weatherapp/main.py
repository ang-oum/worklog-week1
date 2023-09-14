#https://www.youtube.com/watch?v=DlNIXC9SaF4

import os
import psycopg2
from datetime import datetime, timezone
from dotenv import load_dotenv
from flask import Flask, request


#SQL Queries:
CREATE_ROOMS_TABLE = (
  "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"
)
CREATE_TEMPS_TABLE ="""CREATE TABLE IF NOT EXISTS temperatures (room_id INTEGER, temperature REAL, date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"""

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"

INSERT_TEMP = (
  "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);"
)

GLOBAL_NUMBER_OF_DAYS = (
  """SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures;"""
)

GLOBAL_AVG = """SELECT AVG(temperature) as average FROM temperatures"""


load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.post("/api/room") #http method
def create_room():
  date = request.get_json()
  name = data["name"]
  with connection:
    #cursor = object that allows to insert data or iterate over rows with a query.
    with connection.cursor() as cursor: #cursor = object that allows to insert data or iterate over rows with a query.
      cursor.execute(CREATE_ROOMS_TABLE)
      cursor.execute(INSERT_ROOM_RETURN_ID, (name,))#(name,) tuple w single value
      room_id = cursor.fetchone()[0] #pointing at first row (each row has 2 columns) we select first column
    return {"id": room_id, "message": f"Room {name} created."}, 201


@app.post("/api/temperature")
def add_temp():
    data = request.get_json()
    temperature = data["temperature"]
    room_id = data["room"]
    try:
        date = datetime.strptime(data["date"], "%m-%d-%y %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)

    with connection:
      with connection.cursor() as cursor:
        cursor.execute(CREATE_TEMPS_TALE)
        cursor.execute(INSERET_TEMP, (room_id, temperature, date))

    return {"message": "Temperature added."}, 201


@app.get("/api/average")
def get_global_avg():
  with connection:
    with connection.cursor() as cursor:
      cursor.execute(GLOBAL_AVG)
      average = cursor.fetchone()[0]
      cursor.execute(GLOBAL_NUMBER_OF_DAYS)
      days = cursor.fetchone()[0]
  return {"average": round(average, 2), "days": days}
      
  
      






