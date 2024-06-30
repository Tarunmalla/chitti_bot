import requests
import sqlite3
import pandas as pd

from table2ascii import table2ascii as t2a, PresetStyle

def user_info():
    df=pd.DataFrame(columns=['Handle','ALL','Easy','Medium','Hard'])
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
        print(acSubmissionNum)
        handler_info = []
        for item in acSubmissionNum:
            if 'count' in item:
                info=item['count']
                handler_info.append(info)
        handler_info.insert(0,handle[0])
        df.loc[len(df.index)] = handler_info
               
    table = convert_to_table(df)
    # print(table)
    return table

def convert_to_table(df):
    table = t2a(
        header=list(df.columns),
        body=df.values.tolist(),
        style=PresetStyle.thin_compact
    )
    return table