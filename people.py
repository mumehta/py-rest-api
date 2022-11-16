from datetime import datetime

from flask import abort, make_response
import urllib.request, pymysql
import json

url = "https://my-json-server.typicode.com/mumehta/py-rest-api/db"

def show_people():
    with urllib.request.urlopen(url) as u:
        data = json.load(u)
    return list(data.values())

def fetch_all():
    response = urllib.request.urlopen(url)
    data = response.read().decode('UTF-8')
    file = open("data.json","w")
    file.write(data)
    return list(data.values())

def read_all():
    with open('data.json') as json_file:
        data = json.load(json_file)
        print(data)
    return list(data.values())
    # return list(PEOPLE.values())

def save_all():
    with open('data.json') as json_file:
        data = json.load(json_file)
        print(data)
    conn = pymysql.connect(host="172.17.0.4", user="root", password="password", database="people")

    cursor = conn.cursor()

    for item in data.values():
        lname = item.get("lname")
        fname = item.get("fname")
        cursor.execute("insert into person (lname, fname) value (%s, %s)", (lname, fname))
    conn.commit()
    conn.close()
