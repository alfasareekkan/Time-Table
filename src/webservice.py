import os
from flask import *
from werkzeug.utils import secure_filename

app=Flask(__name__)
from src.dbconnection import *




@app.route('/logincode',methods=['post'])
def logincode():
    username=request.form['username']
    password=request.form['password']
    qry="select * from login where user_name=%s and password=%s and user_type='student'"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return jsonify({"task":"invalid"})
    else:
        return jsonify({"task":"success",'id':res[0]})

@app.route('/viewSub',methods=['post'])
def viewSub():
    print(request.form)
    lid=request.form['lid']

    qry="SELECT `subject`.* FROM `subject` JOIN `course` ON `course`.`course_id`=`subject`.`course_id` JOIN `student` ON `student`.`course_id`=`course`.`course_id` WHERE `student`.`login_id`=%s"
    val=(lid)
    res=androidselectall(qry, val)
    print(res)

    return jsonify(res)

@app.route('/viewNote',methods=['post'])
def viewNote():
    subid=request.form['subid']

    qry="SELECT * FROM `note` WHERE `note`.`subject_id`=%s"
    val=(subid)
    res=androidselectall(qry,val)
    return jsonify(res)



@app.route('/viewAttendence',methods=['post'])
def viewAttendence():
    lid = request.form['lid']
    sid = request.form['ssid']

    qry="SELECT * FROM `student_attendance` WHERE `student_attendance`.`std_id`=%s and `subject_id`=%s"
    val=(lid,sid)
    res=androidselectall(qry,val)
    return jsonify(res)


@app.route('/total',methods=['post'])
def total():
    lid = request.form['lid']
    sid = request.form['ssid']

    qry="SELECT  (COUNT(`attendance`)* 100 / (SELECT COUNT(*) FROM `student_attendance`)) AS Score FROM `student_attendance` JOIN `student` ON `student`.`login_id`=`student_attendance`.`std_id` WHERE  `student_attendance`.`std_id`=%s AND `student_attendance`.`attendance`=1  AND `student_attendance`.`subject_id`=%s GROUP BY `student`.`login_id`"
    val=(lid,sid)
    res=selectone(qry,val)
    if res is not None:
        return jsonify({'task':str(res[0])})
    else:
        return jsonify({'task':"no value"})



@app.route('/askDoubt',methods=['post'])
def askDoubt():
    print(request.form)
    doubt=request.form['doubt']
    staffid=request.form['sid']
    stdid=request.form['lid']


    qry="insert into doubtt values(Null,%s,'pending',%s,%s)"
    val=(doubt,stdid,staffid)
    res=iud(qry,val)

    return jsonify({'task':'success'})

@app.route('/doubtReply',methods=['post'])
def doubtReply():
    print(request.form)
    lid = request.form['lid']
    qry="SELECT `staff`.`first_name`,`staff`.`last_name` ,`doubtt`.* FROM `doubtt` JOIN `staff` ON `staff`.`login_id`=`doubtt`.`staff_id` WHERE `doubtt`.`std_id`=%s"
    val=(lid)
    res=androidselectall(qry,val)
    print(res)

    return jsonify(res)


@app.route('/sendFeadback', methods=['post'])
def sendFeadback():
    stdid=request.form['stdid']
    feadback=request.form['feadback']
    qry = "insert into feedback values(Null,%s,%s,CURDATE())"
    val =(feadback,stdid)
    iud(qry,val)

    return jsonify({"task": "success"})

@app.route('/viewClasWork', methods=['post'])
def viewClasWork():
    sid=request.form['sid']

    qry="SELECT * FROM `work` WHERE `staff_id`=%s"
    val=(sid)
    res=androidselectall(qry,val)

    return jsonify(res)

@app.route('/uploadWrok', methods=['post'])
def uploadWork():
    print(request.form)
    workid=request.form['wid']
    lid = request.form['lid']
    work=request.files['file']
    file=secure_filename(work.filename)
    work.save(os.path.join('static/report',file))

    qry="insert into work_report values(null,%s,%s,%s)"
    val=(file,workid,lid)
    iud(qry,val)
    return jsonify({"task": "success"})

@app.route('/staff',methods=['post'])
def staff():
    print(request.form)
    lid = request.form['lid']
    qry="SELECT * FROM `staff` WHERE `dept` IN (SELECT `course_id` FROM `student` WHERE `login_id`=%s)"
    val=(lid)
    res=androidselectall(qry,val)

    return jsonify(res)

@app.route('/timetable',methods=['post'])
def timetable():
    print(request.form)
    lid = request.form['lid']
    day=request.form['day']
    qry="SELECT `semester`,`course_id` FROM `student` WHERE `login_id`=%s"
    v=lid
    ee=selectone(qry,v)
    print("ee",ee)
    crid=ee[1]
    sem=ee[0]
    q1="SELECT `time_table`.`hour`,`subject`.`subject` FROM `time_table` JOIN `subject` ON `subject`.`subject_id`=`time_table`.`subject_id` WHERE time_table.`course_id`=%s AND time_table.`semester`=%s AND time_table.`day`=%s"
    val=crid,sem,day
    res=androidselectall(q1,val)
    print("res",res)

    return jsonify(res)


app.run(port=5000,host="0.0.0.0")

