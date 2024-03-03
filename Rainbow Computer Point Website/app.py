from flask import Flask, render_template, redirect, request, url_for, jsonify
import pymysql

app = Flask(__name__)

AUTHORIZED_PASSWORD = "shakil015"
AUTHORIZED_USER= "shakil015"

connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='rainbow_computer')

def fetch_data_from_mysql():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM course_info")
    data = cursor.fetchall()
    cursor.close()
    return data


@app.route('/data')
def get_data():
    # Fetch data from MySQL database
    data = fetch_data_from_mysql()
    if data:
        # Convert data to a list of dictionaries
        keys = ['id', 'course_name', 'month_duration', 'weekly', 'duration_hour', 'duration_minute', 'amount', 'image_name']
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

@app.route('/addcourse', methods=['GET', 'POST'])
def addcourse():
    if request.method == 'POST':
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

        data = {'course_name': course_name, 'month_duration': month_duration, 'weekly': weekly, 'duration_hour': duration_hour,'duration_minute':duration_minute,'amount':amount, 'image_name': image_name}
        print(data['course_name'])

        cursor = connection.cursor()
        query = "INSERT INTO course_info (course_name, month_duration, weekly, duration_hour, duration_minute, amount, image_name) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = (course_name, month_duration, weekly, duration_hour, duration_minute, amount, image_name)
        cursor.execute(query, values)
        connection.commit()
        message = 'Successfully Added'
        return render_template('addcourse.html',message=message)
    return render_template('addcourse.html')

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