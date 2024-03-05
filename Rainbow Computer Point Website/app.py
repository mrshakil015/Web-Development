from flask import Flask, render_template, redirect, request, url_for, jsonify
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
    cursor.execute("SELECT * FROM course_info")
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/course_infodata')
def course_infodata():
    course_data = fetch_course_info()
    if course_data:
        return jsonify(course_data)

@app.route('/data')
def get_data():
    # Fetch data from MySQL database
    data = fetch_course_info()
    if data:
        # Convert data to a list of dictionaries
        keys = ['id','couseid', 'course_name', 'month_duration', 'weekly', 'duration_hour', 'duration_minute', 'amount', 'image_name']
        data_list = [dict(zip(keys, row)) for row in data]
        return jsonify(data_list)
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
        print("Image: ",image_file.filename)
        if image_file:
            image_file.save('static/images/' + image_name)

        data = {'courseid':courseid, 'course_name': course_name, 'month_duration': month_duration, 'weekly': weekly, 'duration_hour': duration_hour,'duration_minute':duration_minute,'amount':amount, 'image_name': image_name}
        print(data['course_name'])

        cursor = connection.cursor()
        query = "INSERT INTO course_info (courseid, course_name, month_duration, weekly, duration_hour, duration_minute, amount, image_name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (courseid, course_name, month_duration, weekly, duration_hour, duration_minute, amount, image_name)
        cursor.execute(query, values)
        connection.commit()
        message = 'Successfully Added'
        return render_template('admincourse.html',message=message)
    return render_template('admincourse.html')

@app.route('/update_course', methods=['POST'])
def update_course():
    try:
        # Get updated course information from the form
        course_id = request.form['courseid']
        course_name = request.form['coursename']
        month_duration = request.form['monthduration']
        weekly = request.form['weekly']
        duration_hour = request.form['durationhour']
        duration_minute = request.form['durationminute']
        amount = request.form['amount']
        # Update the course information in the database
        cursor = connection.cursor()
        query = "UPDATE course_info SET course_name = %s, month_duration = %s, weekly = %s, duration_hour = %s, duration_minute = %s, amount = %s WHERE id = %s"
        values = (course_name, month_duration, weekly, duration_hour, duration_minute, amount, course_id)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        return jsonify({'message': 'Course updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_course/<int:course_id>')
def get_course(course_id):
    cursor = connection.cursor()
    query = "SELECT * FROM course_info WHERE courseid = %s"
    cursor.execute(query, (course_id,))
    course_data = cursor.fetchone()
    cursor.close()
    if course_data:
        course_dict = {
            'courseid': course_data[1],
            'coursename': course_data[2],
            'monthduration': course_data[3],
            'weekly': course_data[4],
            'duration_hour': course_data[5],
            'duration_minute': course_data[6],
            'amount': course_data[7],
            'image_name': course_data[8]
        }
        return jsonify(course_dict)
    else:
        return jsonify({'error': 'Course not found'}), 404

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