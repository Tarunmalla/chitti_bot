import sqlite3
import requests
import json



def add_to_codeforces(name,handle):
    conn=sqlite3.connect("handles.db")
    c=conn.cursor()
    c.execute('''CREATE TABLE IF  NOT EXISTS codeforces_handles
         (name text,handle text)''')
    c.execute("INSERT INTO codeforces_handles VALUES (?,?)",(name,handle))
    conn.commit()
    conn.close()

def add_to_leetcode(name,handle):
    conn=sqlite3.connect("handles.db")
    c=conn.cursor()
    c.execute('''CREATE TABLE IF  NOT EXISTS leetcode_handles
         (name text,handle text)''')
    c.execute("INSERT INTO leetcode_handles VALUES (?,?)",(name,handle))
    conn.commit()
    conn.close()

def add_cf_handle(name,handler):
    response = requests.get(f"https://codeforces.com/api/user.info?handles={handler}")
    data_dict = json.loads(response.text)
    handler_info = []
    if data_dict["status"] == "OK":
        add_to_codeforces(name,handler)
        return "Handle added successfully"
    else:
        return "Invalid Handle"


def add_leetcode_handle(name,handler):
    response = requests.get(f"https://leetcode.com/graphql")
    data_dict = json.loads(response.text)
    handler_info = []
    add_to_leetcode(name,handler)
    return "Handle added successfully"
  