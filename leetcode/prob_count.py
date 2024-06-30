import requests
import sqlite3
import pandas as pd
from table2ascii import table2ascii as t2a,PresetStyle
df=pd.DataFrame(columns=['Handle','ALL','Easy','Medium','Hard'])

def user_info():
    conn=sqlite3.connect("handles.db")
    c=conn.cursor()
    c.execute("SELECT handle FROM leetcode_handles")
    handles = c.fetchall()
    # print(handles)
    conn.close()
    total_info = []
    url = 'https://leetcode.com/graphql'
    for handle in handles:
        query = f"""
        {{
            matchedUser(username: "{handle[0]}") {{
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
                info=item['count']
                handler_info.append(info)
        handler_info.insert(0,handle[0])
        df.loc[len(df.index)] = handler_info
    return df
    # header=df.columns.tolist()
    # body=df.values.tolist()
    # output=t2a(
    #     header=header,
    #     body=body,
    #     style=PresetStyle.think_compact
    # )
    # return output

