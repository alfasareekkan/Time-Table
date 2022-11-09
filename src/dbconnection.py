import pymysql

def iud(qry,value):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,database="timetable")
    cmd=con.cursor()
    cmd.execute(qry,value)
    id=cmd.lastrowid
    con.commit()
    con.close()
    return id

def select(qry):
    con = pymysql.connect(host="localhost", user="root", password="", port=3306, database="timetable")
    cmd = con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    return res

def selectall(qry,value):
    con = pymysql.connect(host="localhost", user="root", password="", port=3306, database="timetable")
    cmd = con.cursor()
    cmd.execute(qry,value)
    res=cmd.fetchall()
    return res

def selectone(qry,value):
    con = pymysql.connect(host="localhost", user="root", password="", port=3306, database="timetable")
    cmd = con.cursor()
    cmd.execute(qry,value)
    res=cmd.fetchone()
    return res



def androidselectall(q,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='timetable')
    cmd=con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


def androidselectone(q,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='timetable')
    cmd=con.cursor()
    cmd.execute(q,val)
    s = cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data

def androidselectallnew(q):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='timetable')
    cmd=con.cursor()
    cmd.execute(q)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


def selects(qry):
    con = pymysql.connect(host="localhost", user="root", password="", port=3306, database="timetable")
    cmd = con.cursor()
    cmd.execute(qry)
    res=cmd.fetchone()
    return res
