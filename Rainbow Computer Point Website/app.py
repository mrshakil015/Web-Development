from flask import Flask, render_template, redirect, request, url_for, jsonify
import mysql.connector
import random
import os
import shutil

app = Flask(__name__)

AUTHORIZED_PASSWORD = "shakil015"
AUTHORIZED_USER = "shakil015"

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'rainbow_computer'
}

@app.route('/course_infodata')
def course_infodata():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM course_info"
    cursor.execute(query)
    course_data = cursor.fetchall()
    print("type of: ", type(course_data))

    cursor.close()
    db.close()

    return jsonify(course_data)

@app.route('/coursedata')
def get_coursedata():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM course_info"
    cursor.execute(query)
    coursedata = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(coursedata)

def get_course_info_from_database(courseid):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM course_info WHERE courseid = %s"
    cursor.execute(query, (courseid,))
    course_info = cursor.fetchone()

    cursor.close()
    db.close()

    return course_info

@app.route('/courseinfo/<int:courseid>')
def show_courseinfo(courseid):
    # Assuming you have a function to fetch course info based on courseid from the database
    course_info = get_course_info_from_database(courseid)
    print("Course info type: ", type(course_info))
    # Render a template to display course info
    return render_template('coursedetails.html', course_info=course_info)


@app.route('/service_infodata')
def service_infodata():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM service_info"
    cursor.execute(query)
    service_data = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(service_data)

@app.route('/servicedata')
def get_servicedata():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM service_info"
    cursor.execute(query)
    servicedata = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(servicedata)

@app.route('/successfulstudent_infodata')
def successfulstudent_infodata():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM successfulstudent_info"
    cursor.execute(query)
    successfulstudent_data = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(successfulstudent_data)

@app.route('/galleryimagedata')
def get_galleryimagedata():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM galleryimage_info"
    cursor.execute(query)
    galleryimagedata = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(galleryimagedata)

@app.route('/successfulstudentdata')
def get_successfulstudentdata():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM successfulstudent_info"
    cursor.execute(query)
    successfulstudentdata = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(successfulstudentdata)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/admindashboard')
def admindashboard():
    return render_template("admindashboard.html")

@app.route('/contactus')
def contactus():
    return render_template("contactus.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/applicationform', methods=['POST','GET'])
def applicationform():
    while True:
        studentid = generateid()
        
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM pending_studentinfo WHERE studentid = %s"
        cursor.execute(query, (studentid,))
        dataid = cursor.fetchone()
        cursor.close()
        db.close()

        if not dataid:
            break  
    
    if request.method == 'POST':
        coursename = request.form['coursename']
        studentname = request.form['applicant-studentname']
        fathername = request.form['applicant-fathername']
        mothername = request.form['applicant-mothername']
        dob = request.form['applicant-dob']
        gender = request.form['applicant-gender']
        email = request.form['applicant-email']
        mobile = request.form['applicant-mobile']
        address = request.form['applicant-address']
        image_file = request.files['photo']
        studentphoto = f"{studentid}_{(image_file.filename)}"
        print("Photo: ",studentphoto)
        if image_file:
            image_file.save('static/images/pending_student/' + studentphoto)
        
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        insert_query = "INSERT INTO pending_studentinfo (studentid, coursename, studentname, fathername, mothername, dob, gender, email, mobile, address, studentphoto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (studentid, coursename, studentname, fathername, mothername, dob, gender, email, mobile, address, studentphoto))
        db.commit()
        cursor.close()
        db.close()
        message = "Your Application Received Successfully!"
        return render_template("applicationform.html", message = message)
    
    return render_template("applicationform.html")

@app.route('/pendingstudent')
def pendingstudent():
    # db = mysql.connector.connect(**db_config)
    # cursor = db.cursor(dictionary=True)

    # query = "SELECT * FROM pending_studentinfo"
    # cursor.execute(query)
    # data = cursor.fetchall()

    # cursor.close()
    # db.close()

    return render_template("pendingstudent.html")

@app.route('/pendingstudent_infodata')
def pendingstudent_infodata():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM pending_studentinfo"
    cursor.execute(query)
    pendingstudent_data = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(pendingstudent_data)

@app.route('/get_pendingstudent/<int:student_id>')
def get_pendingstudent(student_id):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM pending_studentinfo WHERE studentid = %s"
    cursor.execute(query, (student_id,))
    pendingstudent_data = cursor.fetchone()

    cursor.close()
    db.close()

    if pendingstudent_data:
        return jsonify(pendingstudent_data)
    else:
        return jsonify({'error': 'pendingstudent not found'}), 404

@app.route('/update_pendingstudent', methods=['POST'])
def update_pendingstudent():
    if request.method == 'POST':
        idno = request.form['update_pendingstudentid']
        photoname = request.form['update_pendingstudentphoto']
    
        rollno = request.form['update_pendingstudentrollno']
        coursename = request.form['update_pendingstudentcoursename']
        batch = request.form['update_pendingstudentbatch']
        section = request.form['update_pendingstudentsection']
        studentname=request.form['update_pendingstudentname']
        fathername = request.form['update_pendingstudentfathername']
        mothername = request.form['update_pendingstudentmothername']
        gender = request.form['update_pendingstudentgender']
        dob = request.form['update_pendingstudentdob']
        address = request.form['update_pendingstudentaddress']
        email = request.form['update_pendingstudentemail']
        mobile = request.form['update_pendingstudentmobile']
        password = mobile

        studentphoto = f"{rollno}_{photoname}"
        source_path = 'static/images/pending_student/' + photoname
        destination_path = 'static/images/students/' + studentphoto

        if os.path.exists(source_path):
            shutil.copyfile(source_path, destination_path)

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        insert_query = "INSERT INTO studentinfo (RollNo, CourseName, Batch, Section, StudentName, FatherName, MotherName, Gender, Dob, Address, Email, Mobile, StudentPhoto, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (rollno, coursename, batch, section, studentname, fathername, mothername, gender, dob, address, email, mobile, photoname, password))
        db.commit()

        delete_query = "DELETE FROM pending_studentinfo WHERE studentid = %s"
        cursor.execute(delete_query, (idno,))
        db.commit()

        cursor.close()
        db.close()

        # if cursor.rowcount > 0:
        #     message = 'pendingstudent updated successfully'
        # else:
        #     message = 'No changes made to the pendingstudent'

        return redirect('/pendingstudent ')

@app.route('/delete_pendingstudent/<int:pendingstudent_id>', methods=['DELETE'])
def delete_pendingstudent(pendingstudent_id):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        query = "DELETE FROM pending_studentinfo WHERE studentid = %s"
        cursor.execute(query, (pendingstudent_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'message': 'Student deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/studentsinfo')
def studentsinfo():
    return render_template('studentsinfo.html')

@app.route('/studentsinfo_data')
def studentsinfo_data():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM studentinfo"
    cursor.execute(query)
    students_data = cursor.fetchall()
    print(students_data)

    cursor.close()
    db.close()

    return jsonify(students_data)

@app.route('/delete_studentsinfo/<int:studentinfo_roll>', methods=['DELETE'])
def delete_studentsinfo(studentinfo_roll):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        query = "DELETE FROM studentinfo WHERE RollNo = %s"
        cursor.execute(query, (studentinfo_roll,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'message': 'Student deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_studentsinfo/<int:student_rollno>')
def get_studentinfo(student_rollno):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM studentinfo WHERE RollNo = %s"
    cursor.execute(query, (student_rollno,))
    studentinfo_data = cursor.fetchone()
    print("Student my data: ",studentinfo_data)

    # cursor.close()
    db.close()

    if studentinfo_data:
        return jsonify(studentinfo_data)
    else:
        return jsonify({'error': 'Student not found'}), 404
    
def generateid():
    randomid = random.randint(100,10000)
    return randomid

@app.route('/studentlogin', methods=['POST','GET'])
def studentlogin():
    return render_template("studentlogin.html")

@app.route('/admincourse', methods=['POST', 'GET'])
def admincourse():
    if request.method == 'POST':
        courseid = request.form['courseid']
        course_name = request.form['coursename']
        month_duration = request.form['monthduration']
        weekly = request.form['weekly']
        duration_hour = request.form['durationhour']
        duration_minute = request.form['durationminute']
        amount = request.form['amount']
        image_file = request.files['imagename']
        image_name = image_file.filename
        aboutcourse = request.form['aboutcourse']
        coursetopic = request.form['coursetopic']
        print("Image: ", image_file.filename)
        if image_file:
            image_file.save('static/images/' + image_name)

        data = {'courseid': courseid, 'course_name': course_name, 'month_duration': month_duration,
                'weekly': weekly, 'duration_hour': duration_hour, 'duration_minute': duration_minute,
                'amount': amount, 'image_name': image_name, 'aboutcourse': aboutcourse, 'coursetopic': coursetopic}
        print(data['course_name'])

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        query = "INSERT INTO course_info (courseid, course_name, month_duration, weekly, duration_hour, duration_minute, amount, image_name, aboutcourse, coursetopic) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (courseid, course_name, month_duration, weekly, duration_hour, duration_minute, amount, image_name,
                  aboutcourse, coursetopic)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()
        message = 'Successfully Added'
        return render_template('admincourse.html', message=message)
    return render_template('admincourse.html')

@app.route('/get_course/<int:course_id>')
def get_course(course_id):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM course_info WHERE courseid = %s"
    cursor.execute(query, (course_id,))
    course_data = cursor.fetchone()

    cursor.close()
    db.close()

    if course_data:
        return jsonify(course_data)
    else:
        return jsonify({'error': 'Course not found'}), 404

@app.route('/update_course', methods=['POST'])
def update_course():
    if request.method == 'POST':
        courseid = request.form['update_courseid']
        print("Course id: ", courseid)
        course_name = request.form['update_coursename']
        month_duration = request.form['update_monthduration']
        weekly = request.form['update_weekly']
        duration_hour = request.form['update_durationhour']
        duration_minute = request.form['update_durationminute']
        amount = request.form['update_amount']
        aboutcourse = request.form['update_aboutcourse']
        coursetopic = request.form['update_coursetopic']
        image_file = request.files['update_imagename']
        image_name = image_file.filename
        print("Image: ", image_file.filename)
        if image_file:
            image_file.save('static/images/' + image_name)

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        query = "UPDATE course_info SET course_name = %s, month_duration = %s, weekly = %s, duration_hour = %s, duration_minute = %s, amount = %s, image_name = %s, aboutcourse = %s, coursetopic=%s WHERE courseid = %s"
        values = (course_name, month_duration, weekly, duration_hour, duration_minute, amount, image_name, aboutcourse,
                  coursetopic, courseid)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

        if cursor.rowcount > 0:
            message = 'Course updated successfully'
        else:
            message = 'No changes made to the course'

        return redirect('/admincourse')

@app.route('/delete_course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        query = "DELETE FROM course_info WHERE courseid = %s"
        cursor.execute(query, (course_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'message': 'Course deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/adminservice', methods=['POST', 'GET'])
def adminservice():
    if request.method == 'POST':
        serviceid = request.form['serviceid']
        servicename = request.form['servicename']
        aboutservice = request.form['aboutservice']

        data = {'serviceid': serviceid, 'servicename': servicename, 'aboutservice': aboutservice}
        print(data['servicename'])

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        query = "INSERT INTO service_info (serviceid, servicename, aboutservice) VALUES(%s,%s,%s)"
        values = (serviceid, servicename, aboutservice)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()
        message = 'Successfully Added'
        return render_template('adminservice.html', message=message)
    return render_template('adminservice.html')

@app.route('/get_service/<int:service_id>')
def get_service(service_id):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM service_info WHERE serviceid = %s"
    cursor.execute(query, (service_id,))
    service_data = cursor.fetchone()

    cursor.close()
    db.close()

    if service_data:
        return jsonify(service_data)
    else:
        return jsonify({'error': 'Service not found'}), 404

@app.route('/update_service', methods=['POST'])
def update_service():
    if request.method == 'POST':
        serviceid = request.form['update_serviceid']
        servicename = request.form['update_servicename']
        aboutservice = request.form['update_aboutservice']

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        query = "UPDATE service_info SET servicename = %s, aboutservice = %s WHERE serviceid = %s"
        values = (servicename, aboutservice, serviceid)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

        if cursor.rowcount > 0:
            message = 'Service updated successfully'
        else:
            message = 'No changes made to the Service'

        return redirect('/adminservice')

@app.route('/delete_service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        query = "DELETE FROM service_info WHERE serviceid = %s"
        cursor.execute(query, (service_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'message': 'Service deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/adminsuccessfulstudent', methods=['POST', 'GET'])
def adminsuccessfulstudent():
    while True:
        successfulstudentid = generateid()
        
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM successfulstudent_info WHERE studentid = %s"
        cursor.execute(query, (successfulstudentid,))
        dataid = cursor.fetchone()
        cursor.close()
        db.close()

        if not dataid:
            break 
    if request.method == 'POST':
        successfulstudent_name = request.form['successfulstudentname']
        print("Successful Student name: ", successfulstudent_name)
        successfulstudent_designation = request.form['successfulstudentdesignation']
        successfulstudent_institute = request.form['successfulstudentinstitute']
        image_file = request.files['imagename']
        image_name = image_file.filename

        if image_file:
            image_file.save('static/images/successfulstudent/' + image_name)

        # data = {'successfulstudentid': successfulstudentid, 'successfulstudent_name': successfulstudent_name, 'month_duration': month_duration,
        #         'weekly': weekly, 'duration_hour': duration_hour, 'duration_minute': duration_minute,
        #         'amount': amount, 'image_name': image_name, 'aboutsuccessfulstudent': aboutsuccessfulstudent, 'successfulstudenttopic': successfulstudenttopic}
        # print(data['successfulstudent_name'])

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        query = "INSERT INTO successfulstudent_info (studentid, studentname, studentdesignation,studentinstitute, image_name) VALUES(%s,%s,%s,%s,%s)"
        values = (successfulstudentid, successfulstudent_name,successfulstudent_designation, successfulstudent_institute, image_name)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()
        message = 'Successfully Added'
        return render_template('adminsuccessfulstudent.html', message=message)
    return render_template('adminsuccessfulstudent.html')

@app.route('/admin', methods=['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        admin_username = request.form['admin_username']
        admin_password = request.form['admin_password']
        print(admin_username)
        print(admin_password)

        if (admin_username == AUTHORIZED_USER) and (admin_password == AUTHORIZED_PASSWORD):
            print("It works")
            return redirect(url_for('admindashboard'))
        else:
            error_message = "Invalid admin credentials"
            return render_template('adminlogin.html', error_message=error_message)
    else:
        return render_template('adminlogin.html', error_message=None)

if __name__ == '__main__':
    app.run(debug=True, port=8000)