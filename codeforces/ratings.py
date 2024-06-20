import requests
import json

def get_handle_info(handler):
  response = requests.get(f"https://codeforces.com/api/user.info?handles={handler}")
  data_dict = json.loads(response.text)
  handler_info = []
  for user in data_dict["result"]:
      info = f"{user['handle']} | {user['rating']} | {user['rank']}"
      handler_info.append(info)
  return "\n".join(handler_info)