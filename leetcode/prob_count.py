import requests
def user_info(handle):
    url = 'https://leetcode.com/graphql'
    query = f"""
    {{
        matchedUser(username: "{handle}") {{
            username
            submitStats: submitStatsGlobal {{
                acSubmissionNum {{
                    difficulty
                    count
                    submissions
                }}
            }}
        }}
    }}
    """
    response = requests.post(url, json={'query': query})
    data = response.json()
    acSubmissionNum = data['data']['matchedUser']['submitStats']['acSubmissionNum']
    handler_info = []
    for item in acSubmissionNum:
        if 'count' in item:
            info=f"{item['difficulty']} - {item['count']}"
            handler_info.append(info)
    return "\n".join(handler_info)