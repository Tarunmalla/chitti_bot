import requests
import json
import sqlite3

def get_user_submissions(handles):
    submission_info = []
    
    for handle in handles:
        print(handle)
        url = f"https://codeforces.com/api/user.status?handle={handle}&from=1&count=1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            submissions = data.get('result', [])

            for submission in submissions:
                submission_id = submission.get('id', 'Unknown ID')
                contest_id = submission.get('contestId', 'Unknown Contest ID')
                problem_name = submission.get('problem', {}).get('name', 'Unknown Problem')
                programmingLanguage = submission.get('programmingLanguage', 'Unknown Time')
                verdict = submission.get('verdict', 'Unknown Verdict')
                passedTestCount = submission.get('passedTestCount', 'Unknown passedTestCount')

                submission_info.append(f"Handle: {handle} Submission ID: {submission_id} Contest ID: {contest_id} Problem: {problem_name} Verdict: {verdict} programmingLanguage: {programmingLanguage} passedTestCount:{passedTestCount}\n")
                print(submission_info)
        else:
            submission_info.append(f"Failed to fetch submissions for {handle}")

    return "\n".join(submission_info)
    

def get_handle_info(handler):
    response = requests.get(f"https://codeforces.com/api/user.info?handles={handler}")
  
    data_dict = json.loads(response.text)
    if 'result' in data_dict:
        handler_info = []
        for user in data_dict["result"]:
            info = f"{user['handle']} | {user['rating']} | {user['rank']} | {user['maxRating']} | {user['maxRank']}"
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

def user_submissions():
    conn=sqlite3.connect("handles.db")
    c=conn.cursor()
    c.execute("SELECT handle FROM codeforces_handles")
    handles = c.fetchall()
    conn.close()
    handler = [handle[0] for handle in handles]
    # print(handler)
    return get_user_submissions(handler)