import requests
import json
import sqlite3

def get_handle_info(handler):
    response = requests.get(f"https://codeforces.com/api/user.info?handles={handler}")
  
    data_dict = json.loads(response.text)
    if 'result' in data_dict:
        handler_info = []
        for user in data_dict["result"]:
            info = f"{user['handle']} | {user['rating']} | {user['rank']}"
            handler_info.append(info)
        return "\n".join(handler_info)
    else:
        return "No result found in the API response"

def handle_ratings():
    conn=sqlite3.connect("handles.db")
    c=conn.cursor()
    c.execute("SELECT handle FROM codeforces_handles")
    handles = c.fetchall()
    conn.close()
    handler=";".join(str(handle) for handle in handles)
    return get_handle_info(handler)
