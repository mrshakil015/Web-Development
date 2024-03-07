from flask import Flask, render_template, redirect, request, url_for, jsonify, request
import pymysql

app = Flask(__name__)

AUTHORIZED_PASSWORD = "shakil015"
AUTHORIZED_USER= "shakil015"

connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='rainbow_computer')

def fetch_course_info():
    cursor = connection.cursor()
    query = "SELECT * FROM course_info"
    cursor.execute(query)
    coursedata = cursor.fetchall()
    cursor.close()
    return coursedata

@app.route('/course_infodata')
def course_infodata():
    course_data = fetch_course_info()
    if course_data:
        return jsonify(course_data)

@app.route('/coursedata')
def get_coursedata():
    # Fetch data from MySQL database
    coursedata = fetch_course_info()
    if coursedata:
        # Convert data to a list of dictionaries
        keys = ['id','couseid', 'course_name', 'month_duration', 'weekly', 'duration_hour', 'duration_minute', 'amount', 'image_name', 'aboutcourse', 'coursetopic']
        coursedata_list = [dict(zip(keys, row)) for row in coursedata]
        return jsonify(coursedata_list)
    else:
        return jsonify([])


def fetch_service_info():
    cursor = connection.cursor()
    query = "SELECT * FROM service_info"
    cursor.execute(query)
    servicedata = cursor.fetchall()
    cursor.close()
    return servicedata

@app.route('/service_infodata')
def service_infodata():
    service_data = fetch_service_info()
    if service_data:
        return jsonify(service_data)

@app.route('/servicedata')
def get_servicedata():
    # Fetch data from MySQL database
    servicedata = fetch_service_info()
    if servicedata:
        # Convert data to a list of dictionaries
        keys = ['id','serviceid', 'servicename', 'aboutservice']
        servicedata_list = [dict(zip(keys, row)) for row in servicedata]
        return jsonify(servicedata_list)
    else:
        return jsonify([])



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/admindashboard')
def admindashboard():
    return render_template("admindashboard.html")

@app.route('/applicationform')
def applicationform():
    return render_template("applicationform.html")

@app.route('/admincourse',  methods=['POST', 'GET'])
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
        print("Image: ",image_file.filename)
        if image_file:
            image_file.save('static/images/' + image_name)

        data = {'courseid':courseid, 'course_name': course_name, 'month_duration': month_duration, 'weekly': weekly, 'duration_hour': duration_hour,'duration_minute':duration_minute,'amount':amount, 'image_name': image_name, 'aboutcourse': aboutcourse, 'coursetopic': coursetopic}
        print(data['course_name'])

        cursor = connection.cursor()
        query = "INSERT INTO course_info (courseid, course_name, month_duration, weekly, duration_hour, duration_minute, amount, image_name, aboutcourse, coursetopic) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (courseid, course_name, month_duration, weekly, duration_hour, duration_minute, amount, image_name, aboutcourse, coursetopic)
        cursor.execute(query, values)
        connection.commit()
        message = 'Successfully Added'
        return render_template('admincourse.html',message=message)
    return render_template('admincourse.html')

@app.route('/get_course/<int:course_id>')
def get_course(course_id):
    cursor = connection.cursor()
    query = "SELECT * FROM course_info WHERE courseid = %s"
    cursor.execute(query, (course_id,))
    course_data = cursor.fetchone()
    if course_data:
        course_dict = {
            'courseid': course_data[1],
            'coursename': course_data[2],
            'monthduration': course_data[3],
            'weekly': course_data[4],
            'durationhour': course_data[5],
            'durationminute': course_data[6],
            'amount': course_data[7],
            'imagename': course_data[8],
            'aboutcourse': course_data[9],
            'coursetopic': course_data[10]
        }
        print(course_data[8])
        return jsonify(course_dict)
    else:
        return jsonify({'error': 'Course not found'}), 404

@app.route('/update_course', methods=['POST'])
def update_course():
    if request.method == 'POST':
        courseid = request.form['update_courseid']
        print("Course id: ",courseid)
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
        print("Image: ",image_file.filename)
        if image_file:
            image_file.save('static/images/' + image_name)

        cursor = connection.cursor()
        query = "UPDATE course_info SET course_name = %s, month_duration = %s, weekly = %s, duration_hour = %s, duration_minute = %s, amount = %s, image_name = %s, aboutcourse = %s, coursetopic=%s WHERE courseid = %s"
        values = (course_name, month_duration, weekly, duration_hour, duration_minute, amount,image_name, aboutcourse, coursetopic, courseid)
        cursor.execute(query, values)
        connection.commit()
        
        # Optionally, you can check if any rows were affected to determine if the update was successful
        if cursor.rowcount > 0:
            message = 'Course updated successfully'
        else:
            message = 'No changes made to the course'
            
        return redirect('/admincourse')

@app.route('/delete_course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    try:
        cursor = connection.cursor()
        # Execute SQL query to delete the course with the given ID
        query = "DELETE FROM course_info WHERE courseid = %s"
        cursor.execute(query, (course_id,))
        connection.commit()
        cursor.close()
        return jsonify({'message': 'Course deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/adminservice',  methods=['POST', 'GET'])
def adminservice():
    if request.method == 'POST':
        serviceid = request.form['serviceid']
        servicename = request.form['servicename']
        aboutservice = request.form['aboutservice']
        

        data = {'serviceid':serviceid, 'servicename': servicename, 'aboutservice': aboutservice}
        print(data['servicename'])

        cursor = connection.cursor()
        query = "INSERT INTO service_info (serviceid, servicename, aboutservice) VALUES(%s,%s,%s)"
        values = (serviceid, servicename, aboutservice)
        cursor.execute(query, values)
        connection.commit()
        message = 'Successfully Added'
        return render_template('adminservice.html',message=message)
    return render_template('adminservice.html')

@app.route('/get_service/<int:service_id>')
def get_service(service_id):
    cursor = connection.cursor()
    query = "SELECT * FROM service_info WHERE serviceid = %s"
    cursor.execute(query, (service_id,))
    print("IT work")
    service_data = cursor.fetchone()
    print(service_data)
    if service_data:
        service_dict = {
            'serviceid': service_data[1],
            'servicename': service_data[2],
            'aboutservice': service_data[3],
        }
        print(service_data[1])
        return jsonify(service_dict)
    else:
        return jsonify({'error': 'Service not found'}), 404

@app.route('/update_service', methods=['POST'])
def update_service():
    if request.method == 'POST':
        serviceid = request.form['update_serviceid']
        print("Service id: ",serviceid)
        servicename = request.form['update_servicename']
        aboutservice = request.form['update_aboutservice']
        
        cursor = connection.cursor()
        query = "UPDATE service_info SET servicename = %s, aboutservice = %s WHERE serviceid = %s"
        values = (servicename, aboutservice, serviceid)
        cursor.execute(query, values)
        connection.commit()
        
        # Optionally, you can check if any rows were affected to determine if the update was successful
        if cursor.rowcount > 0:
            message = 'Service updated successfully'
        else:
            message = 'No changes made to the Service'
            
        return redirect('/adminservice')

@app.route('/delete_service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        cursor = connection.cursor()
        # Execute SQL query to delete the course with the given ID
        print("Service id is: ", service_id)
        query = "DELETE FROM service_info WHERE serviceid = %s"
        cursor.execute(query, (service_id,))
        connection.commit()
        cursor.close()
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
            # session['admin_logged_in'] = True
            return redirect(url_for('admindashboard'))
        else:
            error_message = "Invalid admin credentials"
            return render_template('adminlogin.html', error_message=error_message)
    else:
        return render_template('adminlogin.html', error_message=None)

if __name__ == '__main__':
    app.run(debug=True, port=8000)