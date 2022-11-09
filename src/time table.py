import os
from flask import *
from werkzeug.utils import secure_filename

app=Flask(__name__)
from src.dbconnection import *
app.secret_key="123"


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/add_and_manage_course')
def manageCourse():
    qry = "select * from course"
    res = select(qry)

    return render_template('add and manage course.html',val=res)


@app.route('/add_and_manage_staff')
def manageStaff():
    qry="SELECT staff.*,`course`.`course` FROM staff  JOIN `course` ON `course`.`course_id`=`staff`.`dept`"
    res=select(qry)
    return render_template('add and manage staff.html',val=res)



@app.route('/add_course',methods=['post'])
def addCourse():
    return render_template('add course.html')

@app.route('/add_staff',methods=['post'])
def addStaff():
    qry="select * from course"
    res=select(qry)
    return render_template('add staff.html',val=res)






@app.route('/assign_subject_staff',methods=['post'])
def assign_subject_staff():
    qry="select * from staff"
    res = select(qry)
    qry1="select * from subject"
    res1 = select(qry1)
    return render_template('assign subject to staff.html',val=res,val1=res1)
@app.route('/home')
def homePage():
    return render_template('home page.html')
@app.route('/staff_attendance')
def staffattendance():
    q="select * from course"
    res=select(q)
    return render_template('staff attendance.html',val=res)
@app.route('/update')
def updatestaff():
    return render_template('update staff.html')
@app.route('/feedback')
def viewfeedback():
    qry="SELECT `student`.`fname`,`student`.`lname`,`feedback`.*  FROM `feedback` JOIN `student` ON `student`.`login_id`=`feedback`.`sid`"
    res=select(qry)
    return render_template('view feedback.html',val=res)
@app.route('/staffSubjects')
def staffSubjects():
    qry="SELECT `staff`.`first_name`,`staff`.`last_name`,`allocate_subject`.*,`subject`.`subject` FROM `staff` JOIN `allocate_subject` ON `allocate_subject`.`staff_id`=`staff`.`login_id` JOIN `subject` ON `subject`.`subject_id`=`allocate_subject`.`subject_id`"
    res=select(qry)
    return render_template('staff subjects.html',val=res)


@app.route('/logincode',methods=['post'])
def logincode():
    username=request.form['textfield']
    password=request.form['textfield2']

    print(password)

    qry="select * from login where user_name=%s and password=%s "
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("inavlid");window.location="/"</script>'''
    elif res[3]=="admin":
        session['lid']=res[0]
        return '''<script>alert("login success");window.location="/home"</script>'''
    elif res[3]=="staff":
        session['lid'] = res[0]
        return '''<script>alert("login success");window.location="/teacherhome"</script>'''
    else:
        return '''<script>alert("inavlid");window.location="/"</script>'''

#add and manage staff

@app.route('/addStaffcode',methods=['post'])
def addStaffcode():
    try:
        fname=request.form['textfield']
        lname=request.form['textfield2']
        gender=request.form['radiobutton']
        pnumber=request.form['textfield3']
        gmail=request.form['textfield4']
        department=request.form['textfield5']
        username=request.form['textfield6']
        password=request.form['textfield7']

        qry="insert into login values(Null,%s,%s,'staff')"
        val=(username,password)
        id=iud(qry,val)

        qry1="insert into staff values(Null,%s,%s,%s,%s,%s,%s,%s)"
        val1=(str(id),fname,lname,gender,pnumber,gmail,department)
        iud(qry1,val1)
        return '''<script>alert("success");window.location="/add_and_manage_staff#services"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry of username....");window.location="/add_and_manage_staff#services"</script>'''

@app.route('/deleteStaff')
def deleteStaff():
    id=request.args.get('id')
    qry="delete from staff where login_id=%s"
    val=str(id)
    iud(qry,val)
    qry1="delete from login where login_id=%s"
    val = str(id)
    iud(qry1, val)

    return '''<script>alert("delete");window.location="/add_and_manage_staff"</script>'''
@app.route('/editStaff')
def editStaff():
    id = request.args.get('id')
    session['id']=id
    qry="select * from staff where login_id=%s"
    res=selectone(qry,session['id'])
    return render_template('edit staff.html',val=res)

@app.route('/updateStaff',methods=['post'])
def updateStaff():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['radiobutton']
    pnumber = request.form['textfield3']
    gmail = request.form['textfield4']

    qry="update staff set first_name=%s,last_name=%s,gender=%s,phone_number=%s,email=%s where login_id=%s"
    var=(fname,lname,gender,pnumber,gmail,session['id'])
    iud(qry,var)
    return '''<script>alert("updated");window.location="/add_and_manage_staff#services"</script>'''


#add and manage course
@app.route('/updateCourse',methods=['post'])
def updateCourse():
    course=request.form['textfield']
    qry="insert into course values(Null,%s)"
    val=(course)
    iud(qry,val)
    return '''<script>alert("added");window.location="/add_and_manage_course"</script>'''
@app.route('/deleteCourse')
def deleteCourse():
    id=request.args.get('id')
    qry="delete from course where course_id=%s"
    val = str(id)
    iud(qry, val)
    return '''<script>alert("delete");window.location="/add_and_manage_course"</script>'''

@app.route('/manage_subject',methods=['post','get'])
def manageSubject():
    qry = "SELECT `subject`.*,`course`.* FROM`subject` JOIN `course` ON `subject`.`course_id`=`course`.`course_id`"
    res = select(qry)
    print(res )
    print("___________________________________________")
    return render_template('add and manage subject.html',val=res)

@app.route('/add_subject',methods=['post'])
def addSubject():
    qry="select * from course"
    res=select(qry)
    print("______________________")
    print(res)
    print("______________________")

    return  render_template('add subject.html',val=res)

@app.route('/addSubjectvalues',methods=['post'])
def addSubjectvalues():
    course=request.form['select']
    semester=request.form['select2']
    subject_id=request.form['textfield']
    subject=request.form['textfield2']
    qry="insert into subject values(Null,%s,%s,%s,%s)"
    val=(course,subject_id,subject,semester)
    iud(qry,val)
    return '''<script>alert("success");window.location="/manage_subject#services"</script>'''

@app.route('/deleteSubject')
def deleteSubject():
    id=request.args.get('id')
    qry="DELETE FROM SUBJECT WHERE subject_id=%s"
    iud(qry,id)

    return '''<script>alert("deleted");window.location="/manage_subject#services"</script>'''
@app.route('/editSubject')
def editSubject():
    id = request.args.get('id')
    session['eid'] = id
    qry = "select * from subject where subject_id=%s"
    res = selectone(qry, session['eid'])
    qry1="select * from course"
    res1=select(qry1)

    return render_template('editSubject.html',val=res,val1=res1)

@app.route('/editSubjectvalues',methods=['post'])
def editSubjectvalues():
    course = request.form['select']
    semester = request.form['select2']
    subject_id = request.form['textfield']
    subject = request.form['textfield2']
    qry = "update subject set course_id=%s,subject_code=%s,subject=%s,semester=%s where subject_id=%s"
    val = (course, subject_id, subject, semester,session['eid'])
    iud(qry, val)
    return '''<script>alert("success");window.location="/manage_subject#services"</script>'''

@app.route('/assignSubject1',methods=['post'])
def assignSubject1():
    staff=request.form['select']
    subject=request.form['select2']
    q="select * from allocate_subject where subject_id=%s and staff_id=%s "
    val=(subject,staff)
    res=selectone(q,val)
    if res is None:
        qry="insert into allocate_subject values(Null,%s,%s)"
        val=(subject,staff)
        iud(qry,val)
        return '''<script>alert("success");window.location="/staffSubjects#services"</script>'''
    else:
        return '''<script>alert("already exist");window.location="/staffSubjects#services"</script>'''








#module 2
@app.route('/add_and_manage_student')
def manageStudent():
    qry = "SELECT `student`.*,`course`.`course` FROM `student` JOIN `course` ON `student`.`course_id`=`course`.`course_id`"
    res = select(qry)

    return render_template('module2/add and manage student.html',val=res)

@app.route('/add_class_work')
def addClassWork():
    q="select * from work where staff_id=%s"
    res=selectall(q,str(session['lid']))

    return render_template('module2/add class work.html',val=res)

@app.route('/class_work',methods=['post'])
def class_work():
    work=request.files['file']
    file=secure_filename(work.filename)
    work.save(os.path.join("static/work",file))
    qry="insert into work values(Null,%s,%s)"
    val=(file,session['lid'])
    iud(qry,val)
    return '''<script>alert("added");window.location="/add_class_work#services"</script>'''




@app.route('/add_note')
def add_note():
    qry = "SELECT `subject`.* FROM`subject` JOIN `allocate_subject` ON `allocate_subject`.`subject_id`=`subject`.`subject_id` WHERE `staff_id`=%s"
    res = selectall(qry, session['lid'])
    qq="SELECT `subject`.`subject`,`note`.* FROM `note` JOIN `subject` ON `subject`.`subject_id`=`note`.`subject_id` WHERE `note`.`subject_id` IN (SELECT  `subject_id` FROM `allocate_subject`  WHERE `staff_id`=%s)"
    rr=selectall(qq,session['lid'])
    return render_template('module2/add notes.html',val=res,val1=rr)

@app.route('/addNote',methods=['post'])
def addNote():
    note = request.files['file']
    file = secure_filename(note.filename)
    note.save(os.path.join("static/note", file))
    subject_id=request.form['select']
    qry = "insert into note values(Null,%s,%s)"
    val = (file,subject_id)
    iud(qry, val)
    return '''<script>alert("added");window.location="/add_note"</script>'''

@app.route('/add_student',methods=['post'])
def addStudent():
    qry = "select * from course"
    res = select(qry)

    return render_template('module2/add student.html',val=res)

@app.route('/doubt_clearence')
def doubt_clearence():
    qry="SELECT `doubtt`.*,`student`.`fname`,`lname` FROM `doubtt` JOIN `student` ON `doubtt`.`std_id`=`student`.`login_id` WHERE `doubtt`.`staff_id`=%s and `doubtt`.`doubt_reply`='pending'"
    res=selectall(qry,session['lid'])
    return render_template('module2/doubt clearence.html',val=res)

@app.route('/mark_attendence')
def markAttendence():
    qry="SELECT `student`.`login_id`,`student`.`fname`,`student`.`lname`,`student`.`reg_no`,`allocate_subject`.`subject_id` FROM `student` JOIN `course` ON `course`.`course_id`=`student`.`course_id` JOIN `staff` ON staff.`dept`=`course`.`course_id` JOIN `allocate_subject` ON `allocate_subject`.`staff_id`=`staff`.`login_id` WHERE `staff`.`login_id`=%s"
    res=selectall(qry,session['lid'])

    return render_template('module2/mark attendence.html',val=res)

@app.route('/attendence',methods=['post'])
def attendence():
    student = request.form.getlist('checkbox')
    print(student)

    qry="SELECT `student`.`login_id`,`student`.`fname`,`student`.`lname`,`student`.`reg_no`,`allocate_subject`.`subject_id` FROM `student` JOIN `course` ON `course`.`course_id`=`student`.`course_id` JOIN `staff` ON staff.`dept`=`course`.`course_id` JOIN `allocate_subject` ON `allocate_subject`.`staff_id`=`staff`.`login_id` WHERE `staff`.`login_id`=%s"
    val=(session['lid'])
    result=selectall(qry,val)
    print(result)

    for i in result:


        if str(i[0]) in student:
            print(i[0])
            q="select * from student_attendance where std_id=%s and subject_id=%s  and date=curdate()"
            val=(str(i[0]),str(i[4]))
            re=selectone(q,val)
            if re is None:


                qry="INSERT INTO `student_attendance` VALUES(NULL,%s,%s,'1',CURDATE())"
                val=(str(i[0]),str(i[4]))
                iud(qry,val)
            else:
                qq="update student_attendance set attendance=1 where attendance_id=%s "
                val=re[0]
                iud(qq,val)

        else:
            q = "select * from student_attendance where std_id=%s and subject_id=%s  and date=curdate()"
            val = (str(i[0]), str(i[4]))
            re = selectone(q, val)
            if re is None:
                qry = "INSERT INTO `student_attendance` VALUES(NULL,%s,%s,'0',CURDATE())"
                val = (i[0],i[4])
                iud(qry, val)
            else:
                qq="update student_attendance set attendance=0 where attendance_id=%s "
                val=re[0]
                iud(qq,val)


    return '''<script>alert("success");window.location="/mark_attendence"</script>'''


@app.route('/mark_topic_covered')
def markTopicCovered():
    qry="SELECT `subject`.* FROM`subject` JOIN `allocate_subject` ON `allocate_subject`.`subject_id`=`subject`.`subject_id` WHERE `staff_id`=%s"
    res = selectall(qry, session['lid'])

    return render_template('module2/mark topic covered.html',val=res)

@app.route('/reply')
def reply():

    id=request.args.get('id')
    session['did']=id
    return render_template('module2/reply.html')

@app.route('/view_allocated_subject')
def viewAllocatedSubject():
    qry = "SELECT `subject`.`subject` FROM`subject` JOIN `allocate_subject` ON `allocate_subject`.`subject_id`=`subject`.`subject_id` WHERE `staff_id`=%s"
    res = selectall(qry, session['lid'])


    return render_template('module2/view allocated subject.html',val=res)

@app.route('/view_student_upload')
def viewStudentUpload():
    qry="SELECT `student`.`fname`,`student`.`lname` ,work_report.`work_report` FROM `student` JOIN `work_report` ON `student`.`std_id`=`work_report`.`std_id`"
    res=select(qry)

    return render_template('module2/view student upload.html',val=res)

@app.route('/teacherhome')
def teacherHome():

    return render_template('module2/teacherhome.html')

@app.route('/addStudent',methods=['post'])
def addStudent1():
    regno = request.form['textfield']
    fname = request.form['textfield2']
    lname = request.form['textfield3']
    course = request.form['select']
    semester = request.form['select2']
    gender = request.form['radiobutton']
    phone =request.form['textfield4']
    parent_phone=request.form['textfield5']
    email=request.form['textfield6']
    username=request.form['textfield7']
    password=request.form['textfield8']

    qry = "insert into login values(Null,%s,%s,'student')"
    val = (username, password)
    id = iud(qry, val)

    qry1 = "insert into student values(Null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id),regno,fname,lname,course,semester,gender,phone,parent_phone,email)
    iud(qry1, val1)
    return '''<script>alert("success");window.location="/add_and_manage_student#services"</script>'''

@app.route('/deletestudent')
def deleteStudent():
    id=request.args.get('id')
    qry="delete from student where std_id=%s"
    val=str(id)
    iud(qry,val)
    qq="delete from login where login_id=%s"
    iud(qq,val)
    return '''<script>alert("delete");window.location="/add_and_manage_student"</script>'''

@app.route('/replyStaff',methods=['post'])
def replayStaff():
    reply=request.form['textarea']
    qry = "UPDATE`doubtt` SET `doubtt`.`doubt_reply`=%s WHERE `doubtt`.`doubt_id`=%s"
    val=(reply,session['did'])
    iud(qry,val)
    return '''<script>alert("replyed");window.location="/doubt_clearence"</script>'''









@app.route('/deleteassignt')
def deleteassignt():
    id=request.args.get('id')
    qry="delete from allocate_subject where allocate_id=%s"
    val=str(id)
    iud(qry,val)
    return '''<script>alert("delete");window.location="/staffSubjects#services"</script>'''


@app.route('/removework')
def removework():
    id=request.args.get('id')
    qry="delete from work where work_id=%s"
    val=str(id)
    iud(qry,val)
    return '''<script>alert("delete");window.location="/add_class_work"</script>'''



@app.route('/removenote')
def removenote():
    id=request.args.get('id')
    qry="delete from note where note_id=%s"
    val=str(id)
    iud(qry,val)
    return '''<script>alert("delete");window.location="/add_note#services"</script>'''




@app.route('/timetable')
def timetable():
    q="select * from course"
    s=select(q)
    return render_template("timetable.html",val=s)



@app.route('/sub',methods=['post'])
def sub():
    cr=request.form['select']
    session['crid']=cr
    sem=request.form['select2']
    session['sem']=sem
    q = "select * from course"
    s = select(q)

    q="select * from `subject` WHERE `course_id`=%s AND `semester`=%s"
    v=cr,sem
    res=selectall(q,v)
    return render_template("timetable.html",val1=res,val=s,cr=cr)



@app.route('/insertdata',methods=['post'])
def insertdata():
    print(request.form)
    s1=request.form['select3']
    if int(s1)!=0:
        q="select * from time_table where course_id=%s and semester=%s and day='MONDAY' and hour=1 and subject_id=%s"
        v=session['crid'],session['sem'],s1
        res=selectone(q,v)
        print(res)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'MONDAY',1,%s)"
            v = session['crid'], session['sem'],s1
            iud(q,v)
    s2=request.form['select8']
    if int(s2)!=0:
        q = "select * from time_table where course_id=%s and semester=%s and day='MONDAY' and hour=2 and subject_id=%s"
        v = session['crid'], session['sem'], s2
        res = selectone(q, v)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'MONDAY',2,%s)"
            v = session['crid'], session['sem'], s2
            iud(q, v)

    s3=request.form['select13']
    if int(s3)!=0:
        q = "select * from time_table where course_id=%s and semester=%s and day='MONDAY' and hour=3 and subject_id=%s"
        v = session['crid'], session['sem'], s3
        res = selectone(q, v)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'MONDAY',3,%s)"
            v = session['crid'], session['sem'], s3
            iud(q, v)

    s4=request.form['select18']
    if int(s4)!=0:
        q = "select * from time_table where course_id=%s and semester=%s and day='MONDAY' and hour=4 and subject_id=%s"
        v = session['crid'], session['sem'], s4
        res = selectone(q, v)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'MONDAY',4,%s)"
            v = session['crid'], session['sem'], s4
            iud(q, v)

    s5=request.form['select23']
    if int(s5)!=0:
        q = "select * from time_table where course_id=%s and semester=%s and day='MONDAY' and hour=5 and subject_id=%s"
        v = session['crid'], session['sem'], s5
        res = selectone(q, v)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'MONDAY',5,%s)"
            v = session['crid'], session['sem'], s5
            iud(q, v)

    s6=request.form['select4']
    if int(s6)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='TUESDAY' and hour=1 and subject_id=%s"
        v = session['crid'], session['sem'], s6
        res = selectone(q, v)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'TUESDAY',1,%s)"
            v = session['crid'], session['sem'], s6
            iud(q, v)

    s7=request.form['select9']
    if int(s7)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='TUESDAY' and hour=2 and subject_id=%s"
        v = session['crid'], session['sem'], s7
        res = selectone(q, v)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'TUESDAY',2,%s)"
            v = session['crid'], session['sem'], s7
            iud(q, v)
    s8=request.form['select14']
    if int(s8)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='TUESDAY' and hour=3 and subject_id=%s"
        v = session['crid'], session['sem'], s8
        res = selectone(q, v)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'TUESDAY',3,%s)"
            v = session['crid'], session['sem'], s8
            iud(q, v)
    s9=request.form['select19']
    if int(s9)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='TUESDAY' and hour=4 and subject_id=%s"
        v = session['crid'], session['sem'], s9
        res = selectone(q, v)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'TUESDAY',4,%s)"
            v = session['crid'], session['sem'], s9
            iud(q, v)

    s10=request.form['select24']
    if int(s10)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='TUESDAY' and hour=5 and subject_id=%s"
        v = session['crid'], session['sem'], s10
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'TUESDAY',5,%s)"
            v = session['crid'], session['sem'], s10
            iud(q, v)
    s11=request.form['select5']
    if int(s11)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='WEDNESDAY' and hour=1 and subject_id=%s"
        v = session['crid'], session['sem'], s11
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'WEDNESDAY',1,%s)"
            v = session['crid'], session['sem'], s11
            iud(q, v)
    s12=request.form['select10']
    if int(s12)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='TUESDAY' and hour=2 and subject_id=%s"
        v = session['crid'], session['sem'], s11
        res = selectone(q, v)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'WEDNESDAY',2,%s)"
            v = session['crid'], session['sem'], s12
            iud(q, v)
    s13=request.form['select15']
    if int(s13)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='WEDNESDAY' and hour=3 and subject_id=%s"
        v = session['crid'], session['sem'], s11
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'WEDNESDAY',3,%s)"
            v = session['crid'], session['sem'], s11
            iud(q, v)
    s14=request.form['select20']
    if int(s14)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='WEDNESDAY' and hour=4 and subject_id=%s"
        v = session['crid'], session['sem'], s14
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'WEDNESDAY',4,%s)"
            v = session['crid'], session['sem'], s14
            iud(q, v)
    s15=request.form['select25']
    if int(s15)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='WEDNESDAY' and hour=3 and subject_id=%s"
        v = session['crid'], session['sem'], s15
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'WEDNESDAY',3,%s)"
            v = session['crid'], session['sem'], s15
            iud(q, v)

    s16=request.form['select6']
    if int(s16)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='THURSDAY' and hour=1 and subject_id=%s"
        v = session['crid'], session['sem'], s16
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'THURSDAY',1,%s)"
            v = session['crid'], session['sem'], s16
            iud(q, v)

    s17=request.form['select11']
    if int(s17)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='THURSDAY' and hour=2 and subject_id=%s"
        v = session['crid'], session['sem'], s17
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'THURSDAY',2,%s)"
            v = session['crid'], session['sem'], s17
            iud(q, v)

    s18=request.form['select16']
    if int(s18)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='THURSDAY' and hour=3 and subject_id=%s"
        v = session['crid'], session['sem'], s18
        res = selectone(q, v)
        if res is  None:

            q = "insert into time_table values(null,%s,%s,'THURSDAY',3,%s)"
            v = session['crid'], session['sem'], s18
            iud(q, v)


    s19=request.form['select21']
    if int(s19)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='THURSDAY' and hour=4 and subject_id=%s"
        v = session['crid'], session['sem'], s19
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'THURSDAY',4,%s)"
            v = session['crid'], session['sem'], s19
            iud(q, v)

    s20=request.form['select26']
    if int(s20)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='THURSDAY' and hour=5 and subject_id=%s"
        v = session['crid'], session['sem'], s20
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'THURSDAY',5,%s)"
            v = session['crid'], session['sem'], s20
            iud(q, v)

    s21=request.form['select7']
    if int(s21)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='FRIDAY' and hour=1 and subject_id=%s"
        v = session['crid'], session['sem'], s21
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'FRIDAY',1,%s)"
            v = session['crid'], session['sem'], s21
            iud(q, v)

    s22=request.form['select12']
    if int(s22)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='FRIDAY' and hour=2 and subject_id=%s"
        v = session['crid'], session['sem'], s22
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'FRIDAY',2,%s)"
            v = session['crid'], session['sem'], s22
            iud(q, v)
    s23=request.form['select17']
    if int(s23)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='FRIDAY' and hour=3 and subject_id=%s"
        v = session['crid'], session['sem'], s23
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'FRIDAY',3,%s)"
            v = session['crid'], session['sem'], s23
            iud(q, v)

    s24=request.form['select22']
    if int(s24)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='FRIDAY' and hour=4 and subject_id=%s"
        v = session['crid'], session['sem'], s24
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'FRIDAY',4,%s)"
            v = session['crid'], session['sem'], s24
            iud(q, v)
    s25=request.form['select27']
    if int(s25)!= 0:
        q = "select * from time_table where course_id=%s and semester=%s and day='FRIDAY' and hour=5 and subject_id=%s"
        v = session['crid'], session['sem'], s25
        res = selectone(q, v)
        if res is  None:
            q = "insert into time_table values(null,%s,%s,'FRIDAY',5,%s)"
            v = session['crid'], session['sem'], s25
            iud(q, v)

    return '''<script>alert("Timetable Added");window.location="/timetable#services"</script>'''







@app.route('/sattendance',methods=['post'])
def sattendance():
    cr=request.form['select']
    session['ccid']=cr
    q="select * from staff where dept=%s"
    v=cr
    res1=selectall(q,v)
    q = "select * from course"
    res = select(q)
    return render_template("staff attendance.html",val1=res1,val=res)


@app.route('/ssattendance',methods=['post'])
def ssattendance():
    sid = request.form.getlist('checkbox')
    print(sid)
    cr=session['ccid']
    q = "select * from staff where dept=%s"
    v = cr
    result = selectall(q, v)

    print(result)

    for i in result:

        if str(i[1]) in sid:
            print(i[1])
            qq="select * from staff_attendance where staff_id=%s and date=curdate() "
            tt=selectone(qq,str(i[1]))
            if tt is None:

                qry = "INSERT INTO `staff_attendance` VALUES(NULL,%s,CURDATE(),'1')"
                val = (str(i[1]))
                iud(qry, val)
            else:
                qq="update staff_attendance set attendance=1 where aid=%s "
                iud(qq,tt[0])



        else:
            qq = "select * from staff_attendance where staff_id=%s and date=curdate()"
            tt = selectone(qq, str(i[1]))
            if tt is None:

                qry = "INSERT INTO `staff_attendance` VALUES(NULL,%s,CURDATE(),'0')"
                val = (str(i[1]))
                iud(qry, val)
            else:
                qq="update staff_attendance set attendance=0 where aid=%s "
                iud(qq,tt[0])


    return '''<script>alert("success");window.location="/staff_attendance#services"</script>'''




@app.route('/leaverequest',methods=['post'])
def leaverequest():
    date=request.form['date']
    reason=request.form['name']
    day=request.form['select']
    # import datetime
    # date = datetime.date.strftime(datetime.date.today(), "%m/%d/%Y")
    # date=date.replace('/',' ')
    # print(date)
    #
    # import datetime
    #
    # day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    # print(day_name[day])
    q="insert into leave_approach values(null,%s,curdate(),%s,%s,'pending',%s)"
    v=session['lid'],date,reason,day
    iud(q,v)
    return '''<script>alert("success");window.location="/leave"</script>'''

@app.route('/leave')
def leave():
    q="select * from leave_approach where staff_id=%s"
    re=selectall(q,session['lid'])
    print(re)
    return render_template("module2/leave.html",val1=re)



@app.route('/leaverequests')
def leaverequests():

    q="SELECT `staff`.`first_name`,`staff`.`last_name`,`leave_approach`.* FROM `leave_approach` JOIN `staff` ON `staff`.`login_id`=`leave_approach`.`staff_id`  WHERE `leave_approach`.`status`='pending'"
    res=select(q)
    return render_template("leaverequest.html",val=res)


@app.route('/acceptreq')
def acceptreq():
    id=request.args.get('id')
    q="update `leave_approach` SET `status`='accept' WHERE `leave_id`=%s"
    v=id
    iud(q,v)
    return '''<script>alert("approved");window.location="/leaverequests"</script>'''



@app.route('/rejectreq')
def rejectreq():
    id=request.args.get('id')
    q="update `leave_approach` SET `status`='reject' WHERE `leave_id`=%s"
    v=id
    iud(q,v)
    return '''<script>alert("approved");window.location="/leaverequests"</script>'''

@app.route('/topiccovered',methods=['post'])
def topiccovered():
    print(request.form)
    sub=request.form['select']
    sid = request.form.getlist('checkbox')
    print(sid)
    result=6
    for i in  range(1,7):
        print("jefdnscx")
        print(i)

        if str(i) in sid:
            print("i",i)
            q="select * from topic_covered where staff_id=%s and subject_id=%s and module=%s and topic_covered='1'"
            v=str(session['lid']),sub,str(i)
            s=selectone(q,v)
            if s is None:
                qry = "INSERT INTO `topic_covered` VALUES(NULL,%s,%s,%s,'1')"
                val = (str(session['lid']),sub,str(i))
                iud(qry, val)




    return '''<script>alert("success");window.location="/mark_topic_covered"</script>'''

@app.route('/freeperiod')
def freeperiod():
    import datetime
    current_day = datetime.date.today()
    print("\n Default Date Object:", current_day, "\n")
    formatted_date = datetime.date.strftime(current_day, "%d/%m/%Y")
    print("\n Formatted Date String:", formatted_date, "\n")
    date=formatted_date.replace('/'," ")
    print(date)
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    print(day_name[day])
    day=day_name[day]
    q=" select * from `leave_approach` WHERE  `leave_date`=CURDATE() and status='accept'"
    res=selects(q)
    print(res)
    # print("res",len(res))
    if res is not  None:
        stf=res[1]
        q="select * FROM `allocate_subject` WHERE `staff_id`=%s"
        rr=selectone(q,stf)
        print("rr",rr)
        if rr is not None:
            sub=rr[1]
            qq="SELECT * FROM `time_table` WHERE `day`=%s AND `subject_id`=%s "
            v=day,sub
            ss=selectone(qq,v)
            print("ss",ss)
            if ss is not None:
                qq="SELECT COUNT(*) FROM `topic_covered` WHERE `topic_covered`=1 AND `staff_id`=%s"
                tt=selectone(qq,session['lid'])
                cnt=tt[0]
                print("cnt",cnt)
                if cnt<=4:
                    qw = "select * from free where tid=%s"
                    vv =str(ss[0])
                    ff=selectone(qw,vv)
                    print("ff",ff)
                    if ff is  None:
                        qq="insert into free values(null,%s,%s)"
                        v=str(ss[0]),str(session['lid'])
                        iud(qq,v)

        q = "SELECT `time_table`.* FROM `time_table` JOIN `free` ON `free`.`tid`=`time_table`.`id` WHERE `free`.`sid`=%s"
        v = str(session['lid'])
        dd = selectall(q, v)
        return render_template("module2/freeperiod.html", val=dd)
    else:
        return '''<script>alert("no data");window.location="/teacherhome#services"</script>'''



app.run(debug=True)