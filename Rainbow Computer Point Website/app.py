from flask import Flask, render_template, redirect, request, url_for, jsonify
import mysql.connector
import random

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