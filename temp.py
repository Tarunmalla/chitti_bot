import sqlite3

conn=sqlite3.connect("handles.db")
c=conn.cursor()
c.execute("UPDATE leetcode_handles SET handle='tarun_malla' WHERE handle='tarun_516'")