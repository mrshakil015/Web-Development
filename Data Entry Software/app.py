from flask import Flask, render_template, request, url_for, redirect, session, jsonify
import pymysql
from functools import wraps
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import pytz

AUTHORIZED_USER = "sobjantame"
AUTHORIZED_PASSWORD = "Tkgl@432!"

def requires_authentication(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return func(*args, **kwargs)
    return wrapper

app = Flask(__name__)
app.secret_key = '6Lck7P8mAAAAABJdGubIiMM8u8e9lHuSE_KglmTC'
# mysql = pymysql.connect(host='localhost', user='sobjanta_de_users', password='$V75!W#P#C+J9mMM', db='sobjanta_de_users_db')
mysql = pymysql.connect(host='localhost', user='root', password='', db='dataentry_db')

# Function to generate a new operator_id
def generate_operator_id():
    cursor = mysql.cursor()
    cursor.execute("SELECT operator_id FROM operators_db ORDER BY operator_id DESC LIMIT 1")
    last_id = cursor.fetchone()
    if last_id:
        new_id = int(last_id[0]) + 1
    else:
        new_id = 10000
    cursor.close()
    return str(new_id).zfill(4)

# Function to fetch user data from the database
def fetch_user_data(username, password):
    cursor = mysql.cursor()
    query = "SELECT id, operator_id, operatorname, emailaddress, contactnumber, assignday, remainday, sheetid, totaldata, dailydata, completedata, remaindata, totalhours, dailyhours, sheetname,daywisecomplete FROM operators_db WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    cursor.close()
    return user

# Function to fetch user data from the database based on operator_id
def fetch_user_data_by_operator_id(operator_id):
    cursor = mysql.cursor()
    query = "SELECT id, operator_id, operatorname, emailaddress, contactnumber, assignday, remainday, sheetid, totaldata, dailydata, completedata, remaindata, totalhours, dailyhours, sheetname,daywisecomplete FROM operators_db WHERE operator_id = %s"
    cursor.execute(query, (operator_id,))
    user = cursor.fetchone()
    cursor.close()
    
    # Convert the tuple to a dictionary
    user_dict = {
        'id': user[0],
        'operator_id': user[1],
        'operatorname': user[2],
        'emailaddress': user[3],
        'contactnumber': user[4],
        'assignday': user[5],
        'remainday': user[6],
        'sheetid': user[7],
        'totaldata': user[8],
        'dailydata': user[9],
        'completedata': user[10],
        'remaindata': user[11],
        'totalhours': user[12],
        'dailyhours': user[13],
        'sheetname': user[14],
        'daywisecomplete': user[15]
    }

    return user_dict


# Function to set session data from the fetched user data
def set_session_operator_data(user):
    return {
        'id': user[0],
        'operator_id': user[1],
        'operatorname': user[2],
        'emailaddress': user[3],
        'contactnumber': user[4],
        'assignday': user[5],
        'remainday': user[6],
        'sheetid': user[7],
        'totaldata': user[8],
        'dailydata': user[9],
        'completedata': user[10],
        'remaindata': user[11],
        'totalhours': user[12],
        'dailyhours': user[13],
        'sheetname': user[14],
        'daywisecomplete': user[15]
    }
    
def update_hour_data_table(operator_id):
    cursor = mysql.cursor()
    query = "SELECT dailyhours, sheetname FROM operators_db WHERE operator_id = %s"
    cursor.execute(query, (operator_id,))
    user = cursor.fetchone()
    cursor.close()
@app.route('/view_user_update', methods=['POST'])
def view_user_update():
    return

@app.route('/update_hours', methods=['POST'])
def update_hours():
    total_seconds = request.json.get('totalSeconds')
    daily_seconds = request.json.get('dailySeconds')
    
    # Get the operator's ID from the session or request, depending on your setup
    operator_id = session.get('operator_data')['operator_id']

    cursor = mysql.cursor()

    # Fetch all entry dates for the operator_id
    date_query = "SELECT entry_date FROM data_table WHERE operator_id = %s"
    cursor.execute(date_query, (operator_id,))
    entry_dates = [row[0].strftime('%Y-%m-%d') for row in cursor.fetchall()]

    # Print all the entry dates
    print("All Entry Dates:", entry_dates)

    # Get the current date in the Bangladesh timezone
    bangladesh_timezone = pytz.timezone('Asia/Dhaka')
    now_in_bangladesh = datetime.now(bangladesh_timezone)
    current_date = now_in_bangladesh.strftime('%Y-%m-%d')
    print("Current date: ",current_date)

    # Fetch the current totalhours and dailyhours from the database
    select_query = "SELECT  totalhours, dailyhours FROM operators_db WHERE operator_id = %s"
    cursor.execute(select_query, (operator_id,))
    current_hours = cursor.fetchone()
    
    if not current_hours:
        # Handle the case where the operator ID doesn't exist in the database
        cursor.close()
        return jsonify({"message": "Operator not found"}, 404)

    current_totalhours, current_dailyhours = current_hours
    total_seconds = current_totalhours + total_seconds
    daily_seconds = current_dailyhours + daily_seconds

    # Update the totalhours and dailyhours in the database
    update_query = "UPDATE operators_db SET totalhours = %s, dailyhours = %s WHERE operator_id = %s"
    cursor.execute(update_query, (total_seconds, daily_seconds, operator_id))
    mysql.commit()
    
    
    try:
        if current_date in entry_dates:
            print("Update previous table")
            print("Update time table", daily_seconds)
            today_hours = daily_seconds
            update_date_query = "UPDATE data_table SET today_hours = %s WHERE operator_id = %s AND entry_date = %s"
            cursor.execute(update_date_query, (today_hours, operator_id, current_date))
            mysql.commit()
        else:
            # Insert a new record for the current date
            query = "INSERT INTO data_table (operator_id, entry_date, today_hours) VALUES (%s, %s, %s)"
            values = (operator_id, current_date, daily_seconds)
            cursor.execute(query, values)
            mysql.commit()

        # Commit the changes
        mysql.commit()
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    cursor.close()
    
    cursor = mysql.cursor()
    
    # Fetch the current totalhours and dailyhours from the database
    select_query = "SELECT totalhours, dailyhours FROM operators_db WHERE operator_id = %s"
    cursor.execute(select_query, (operator_id,))
    updated_current_hours = cursor.fetchone()
    total_seconds, daily_seconds = updated_current_hours
    print("total seconds:", total_seconds)

    # Fetch the user's data again after the update
    user_data = fetch_user_data_by_operator_id(operator_id)

    # You can now use the updated and current values as needed.
    response_data = {
        "message": "Hours updated successfully",
        # "current_totalhours": user_data['totalhours'],
        "current_totalhours": total_seconds,
        "current_dailyhours": daily_seconds,
    }

    # Render the template with the updated data and include response_data in the context
    # response_json = jsonify(response_data)
    return jsonify(response_data)

    # return render_template('index.html', operator_data=user_data, current_totalhours=total_seconds, current_dailyhours=daily_seconds, response_data=response_json)



# Filter to format seconds as hours, minutes, and seconds
@app.template_filter('format_time')
def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


# Route for operator login
@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = fetch_user_data(username, password)


        if user:
            session['logged_in'] = True
            session['operator_data'] = set_session_operator_data(user)
  
            # return render_template('index.html', operator_data=session['operator_data'])
            return redirect(url_for('dashboard'))
        else:
            error_message = "Invalid username or password"
            return render_template('login.html', error_message=error_message)
    else:
        return render_template('login.html', error_message=None)

# Route to log out
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    # session.pop('admin_logged_in', None)
    return redirect(url_for('login'))

# Function to fetch data from Google Sheets
def fetch_data_from_google_sheets(sheet_id, sheet_name):
    if 'logged_in' in session:
        operator_data = session.get('operator_data')
        operator_id = operator_data['operator_id']
        user_data = fetch_user_data_by_operator_id(operator_id)
        if operator_data:
            sheet_id = user_data.get('sheetid')
            sheet_name = user_data.get('sheetname')

            if not sheet_id or not sheet_name:
                return "Sheet data not available"

            scope = ["https://www.googleapis.com/auth/spreadsheets"]
            credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scope)
            gc = gspread.authorize(credentials)

            sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit"
            try:
                sheet = gc.open_by_url(sheet_url).worksheet(sheet_name)
                data = sheet.get_all_records()
                return data
            except gspread.exceptions.WorksheetNotFound:
                return "Worksheet not found"
            except Exception as e:
                return f"An error occurred: {str(e)}"
        else:
            print("Operator data not found in the session")
            return "Operator data not found in the session"
    else:
        print("User is not logged in")
        return "User is not logged in"
    


#----------------------remove dailyhour based on user_id----------------------

# def reset_daily_hours(operator_id):
#     cursor = mysql.cursor()

#     # Fetch the current dailyhours for the operator
#     select_query = "SELECT dailyhours FROM operators_db WHERE operator_id = %s"
#     cursor.execute(select_query, (operator_id,))
#     current_dailyhours = cursor.fetchone()[0] if cursor.rowcount > 0 else 0

#     # Reset dailyhours to 0 for the operator
#     update_query = "UPDATE operators_db SET dailyhours = 0 WHERE operator_id = %s"
#     cursor.execute(update_query, (operator_id,))
#     mysql.commit()
#     cursor.close()


# # Schedule the reset_daily_hours function to run every 1 minute for a specific operator

# operator_id_to_reset = 10000
# scheduler.add_job(
#     reset_daily_hours,
#     trigger='interval',
#     minutes=1,
#     args=[operator_id_to_reset]  # Pass the operator_id as an argument
# )

#----------------------remove all user dailyhour ----------------------

# def reset_daily_hours():
#     cursor = mysql.cursor()

#     # Fetch all operator_ids from the database
#     select_query = "SELECT operator_id FROM operators_db"
#     cursor.execute(select_query)
#     operator_ids = [row[0] for row in cursor.fetchall()]

#     # Reset dailyhours to 0 for each operator
#     for operator_id in operator_ids:
#         update_query = "UPDATE operators_db SET dailyhours = 0 WHERE operator_id = %s"
#         cursor.execute(update_query, (operator_id,))
    
#     mysql.commit()
#     cursor.close()
# # Schedule the reset_daily_hours function to run every 1 minute for all operators
# scheduler.add_job(
#     reset_daily_hours,
#     trigger='interval',
#     minutes=1
# )


# #---------------------Daily remove dailyhours values---------------
def reset_daily_hours():
    cursor = mysql.cursor()

    # Reset dailyhours to 0 for all users
    update_query = "UPDATE operators_db SET dailyhours = 0"
    cursor.execute(update_query)

    mysql.commit()
    cursor.close()

# Create a scheduler instance
scheduler = BackgroundScheduler()

# Define a function to schedule the job for resetting daily hours at 12:00 AM daily
def schedule_reset_daily_hours():
    # Schedule the reset_daily_hours function to run at 12:00 AM daily
    trigger = CronTrigger(hour=0, minute=0)  # 0:00 (12:00 AM)
    scheduler.add_job(reset_daily_hours, trigger=trigger)

# Start the scheduler
scheduler.start()
# Schedule the job to reset daily hours at 12:00 AM daily
schedule_reset_daily_hours()

# Initialize the scheduler
scheduler = BackgroundScheduler(daemon=True)
scheduler.start()

#     cursor.close()
def reset_daily_hours():
    cursor = mysql.cursor()
    # Update dailyhours, daywisecomplete, and remainday
    update_query = "UPDATE operators_db SET dailyhours = 0, daywisecomplete = 0, remainday = remainday-1"
    cursor.execute(update_query)
    mysql.commit()
    cursor.close()

# Schedule the job to reset "dailyhours" to 0 for all users at 12:00 AM daily
def schedule_reset_daily_hours():
    trigger = CronTrigger(hour=9, minute=59)  # 0:00 (12:00 AM)
    scheduler.add_job(reset_daily_hours, trigger=trigger)

schedule_reset_daily_hours()



@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        operator_data = session.get('operator_data')
        operator_id = operator_data['operator_id']
        user_data = fetch_user_data_by_operator_id(operator_id)        

        if user_data:
            # Fetch data from Google Sheets using the function
            sheet_id = operator_data['sheetid']
            sheet_name = operator_data['sheetname']
            sheet_data = fetch_data_from_google_sheets(sheet_id, sheet_name)
            
            # Fetch current_totalhours and current_dailyhours from the database
            cursor = mysql.cursor()

            # Fetch the current totalhours and dailyhours from the database
            select_query = "SELECT totalhours, dailyhours FROM operators_db WHERE operator_id = %s"
            cursor.execute(select_query, (operator_id,))
            current_hours = cursor.fetchone()
            current_totalhours, current_dailyhours = current_hours
            cursor = mysql.cursor()
        
        # Query to fetch data from the data_table based on operator id
            query = "SELECT entry_date, complete_data, today_hours, remain_data FROM data_table WHERE operator_id = %s ORDER BY entry_date DESC"
            cursor.execute(query, (operator_id,))
            daywise_data = cursor.fetchall()
            cursor.close()

            # Pass the user data, Google Sheets data, and current hours to the template
            return render_template('index.html', operator_data=user_data,daywise_data=daywise_data, sheet_data=sheet_data, current_totalhours=current_totalhours, current_dailyhours=current_dailyhours)
        else:
            return "Operator not found in the database"
    else:
        return redirect(url_for('login'))

# Route for admin login
@app.route('/admin', methods=['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        admin_username = request.form['admin_username']
        admin_password = request.form['admin_password']

        if admin_username == AUTHORIZED_USER and admin_password == AUTHORIZED_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admindashboard'))
        else:
            error_message = "Invalid admin credentials"
            return render_template('adminlogin.html', error_message=error_message)
    else:
        return render_template('adminlogin.html', error_message=None)
@app.route('/adminlogout')
def adminlogout():
    # session.pop('logged_in', None)
    session.pop('admin_logged_in', None)
    return redirect(url_for('login'))

@app.route('/admindashboard', methods=['GET'])
@requires_authentication
def admindashboard():
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM operators_db")
    data = cursor.fetchall()
    cursor.close()

    # Calculate the total assign data, completed data, and remaining data
    total_assign_data = sum(row[10] for row in data)  # Assuming 'totaldata' is the 9th column (index 8)
    total_completed_data = sum(row[12] for row in data)  # Assuming 'completedata' is the 11th column (index 10)
    total_remain_data = sum(row[13] for row in data)  # Assuming 'remaindata' is the 12th column (index 11)

    # Calculate the total user count
    total_user = len(data)

    # Create a dictionary to hold all the variables you want to pass to the template
    dashboard_data = {
        'total_completed_data': total_completed_data,
        'total_user': total_user,
        'total_assign_data': total_assign_data,
        'total_remain_data': total_remain_data
    }

    return render_template('admindashboard.html', data=data, dashboard_data=dashboard_data)


# Route to add a new operator
@app.route('/add_operator', methods=['POST'])
def add_operator():
    if request.method == 'POST':
        operator_id = generate_operator_id()
        operatorname = request.form['operatorname']
        password = request.form['password']
        emailaddress = request.form['emailaddress']
        username = emailaddress
        contactnumber = request.form['contactnumber']

        cursor = mysql.cursor()
        query = "INSERT INTO operators_db (operator_id, operatorname, username, password, emailaddress, contactnumber) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (operator_id, operatorname, username, password, emailaddress, contactnumber)

        try:
            cursor.execute(query, values)
            mysql.commit()
            cursor.close()
            return redirect(url_for('admindashboard'))
        except Exception as e:
            return "Error: " + str(e)

@app.route('/delete/<user_id>', methods=['GET'])
def delete_user(user_id):
    cursor = mysql.cursor()
    query = "DELETE FROM operators_db WHERE operator_id = %s"
    print("It work:", user_id)
    cursor.execute(query, user_id)
    mysql.commit()
    cursor.close()
    return redirect(url_for('admindashboard'))

@app.route('/assign_job', methods=['POST'])
def assign_job():
    if request.method == 'POST':
        operator_id = request.form['operator_id']
        totaldata = int(request.form['totaldata'])
        dailydata = int(request.form['dailydata'])
        assignday = int(request.form['assignday'])
        sheetid = request.form['sheetid']
        sheetname = request.form['sheetname']
        print("Assign job section", sheetname)

        # Fetch the existing data from the database
        cursor = mysql.cursor()
        query = "SELECT totaldata, dailydata, assignday, remainday, completedata, remaindata,daywisecomplete FROM operators_db WHERE operator_id = %s"
        cursor.execute(query, (operator_id,))
        data = cursor.fetchone()  # Assuming there's only one result

        if data:
            # Extract the values from the database query result
            existing_totaldata, existing_dailydata, existing_assignday, remainday, completedata, remaindata,daywisecomplete = data

            # Calculate new values
            new_remainday = remainday + assignday
            new_totaldata = existing_totaldata + totaldata
            new_dailydata = existing_dailydata+ dailydata
            new_assignday = existing_assignday + assignday
            new_completedata = completedata  # You can change this as needed
            new_remaindata = (new_totaldata - new_completedata)
            new_daywisecomplete = 0

            cursor = mysql.cursor()

            # Define your SQL query to update the operator's data
            query = "UPDATE operators_db SET totaldata = %s, completedata = %s, remaindata = %s, dailydata = %s,remainday = %s, assignday = %s,  sheetid = %s,sheetname = %s WHERE operator_id = %s"
            values = (new_totaldata, new_completedata, new_remaindata, new_dailydata, new_assignday, new_remainday, sheetid,sheetname,new_daywisecomplete, operator_id)

            try:
                cursor.execute(query, values)
                mysql.commit()
                cursor.close()
                return redirect(url_for('admindashboard'))
            except Exception as e:
                return "Error: " + str(e)
        else:
            return "Operator not found in the database"
    return "Invalid request"

# # Add a new route to fetch data from the data_table based on operator id
# @app.route('/fetch_daywise_data', methods=['POST'])
# def fetch_daywise_data():
#     if 'logged_in' in session:
#         operator_data = session.get('operator_data')
#         operator_id = operator_data['operator_id']
#         print("View report work")
        
#         cursor = mysql.cursor()
        
#         # Query to fetch data from the data_table based on operator id
#         query = "SELECT entry_date, complete_data, today_hours, remain_data FROM data_table WHERE operator_id = %s ORDER BY entry_date"
#         cursor.execute(query, (operator_id,))
#         daywise_data = cursor.fetchall()
#         cursor.close()

#         return render_template('index.html', operator_data=operator_data, daywise_data=daywise_data)

#     return redirect(url_for('login'))

@app.route('/entrydata', methods=["GET", "POST"])
def entrydata():
    operator_data = None

    if 'logged_in' in session:
        operator_data = session.get('operator_data')
        if operator_data:
            operator_id = operator_data['operator_id']
            user_data = fetch_user_data_by_operator_id(operator_id)
            operator_data = user_data
            sheet_id = operator_data['sheetid']
            sheet_name = operator_data['sheetname']
            fetch_data_from_google_sheets(sheet_id, sheet_name)

            scope = ["https://www.googleapis.com/auth/spreadsheets"]
            credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scope)
            gc = gspread.authorize(credentials)

            sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit"
            sheet = gc.open_by_url(sheet_url).worksheet(sheet_name)

            if request.method == "POST":
                # Get form data and process it
                operatorid = request.form.get("operatorid")
                operatorid = request.form.get("operatorid")
                region = request.form.get("region")
                district = request.form.get("district")
                store_name = request.form.get("storename")
                branchname = request.form.get("branchname")
                storeaddress = request.form.get("storeaddress")
                storezip = request.form.get("storezip")
                storelatitude = request.form.get("storelatitude")
                storelongitude = request.form.get("storelongitude")
                storewebsite = request.form.get("storewebsite")
                storemobilenumber = request.form.get("storemobilenumber")
                storeemailaddress = request.form.get("storeemailaddress")
                storeopeninghour = request.form.get("storeopeninghour")
                storeclosinghour = request.form.get("storeclosinghour")
                
                # Fetch all entry dates for the operator_id
                cursor = mysql.cursor()
                date_query = "SELECT entry_date FROM data_table WHERE operator_id = %s"
                cursor.execute(date_query, (operator_id,))
                entry_dates = [row[0].strftime('%Y-%m-%d') for row in cursor.fetchall()]
                
                # Print all the entry dates
                print("All Entry Dates:", entry_dates)

                # Get the current date in the Bangladesh timezone
                bangladesh_timezone = pytz.timezone('Asia/Dhaka')
                now_in_bangladesh = datetime.now(bangladesh_timezone)
                current_date = now_in_bangladesh.strftime('%Y-%m-%d')

                # Format the date and time
                entry_date = current_date
                entry_time = now_in_bangladesh.strftime('%I:%M %p')

                # Query to get complete_data for the current operator and date
                completedata_query = "SELECT complete_data FROM data_table WHERE operator_id = %s AND entry_date = %s"
                cursor.execute(completedata_query, (operator_id, current_date))
                complete_data = cursor.fetchone()

                # Check if complete_data is None and initialize to 0 if needed
                if complete_data is None:
                    complete_data_value = 0
                else:
                    complete_data_value = int(complete_data[0])

                # Increment the value
                complete_data_value += 1
                print("Complete Data:", complete_data_value)

                # Append the data, including date and time, to "Sheet2" in the Google Sheet
                data = [entry_date, entry_time, operatorid, region, district, store_name, branchname, storeaddress, storezip, storelatitude, storelongitude, storewebsite, storemobilenumber, storeemailaddress, storeopeninghour, storeclosinghour]
                sheet.append_row(data)

                # Fetch operator data again
                operator_id = operator_data['operator_id']
                operator_data = fetch_user_data_by_operator_id(operator_id)

                # Calculate new values
                new_completedata = operator_data['completedata'] + 1
                new_remaindata = operator_data['remaindata'] - 1
                new_daywisecomplete = operator_data['daywisecomplete'] + 1
                remain_data = operator_data['dailydata'] - complete_data_value
                
                # Perform the database update with the new values
                select_query = "SELECT remainday, totalhours, dailyhours FROM operators_db WHERE operator_id = %s"
                cursor.execute(select_query, (operator_id,))
                current_hours = cursor.fetchone()
                remainday, current_totalhours, current_dailyhours = current_hours

                query = "UPDATE operators_db SET completedata = %s, remaindata = %s, daywisecomplete=%s WHERE operator_id = %s"
                cursor.execute(query, (new_completedata, new_remaindata, new_daywisecomplete, operator_data['operator_id']))
                mysql.commit()

                try:
                    if current_date in entry_dates:
                        # Update the existing record for the current date
                        update_date_query = "UPDATE data_table SET complete_data = %s, remain_data = %s WHERE operator_id = %s AND entry_date = %s"
                        cursor.execute(update_date_query, (complete_data_value, remain_data, operator_id, current_date))
                        mysql.commit()
                        cursor.close()
                        return redirect(url_for('dashboard'))
                    else:
                        # Insert a new record for the current date
                        query = "INSERT INTO data_table (operator_id, complete_data, entry_date, remain_data) VALUES (%s, %s, %s, %s)"
                        values = (operator_id, complete_data_value, current_date, remain_data)
                        cursor.execute(query, values)
                        mysql.commit()
                        cursor.close()
                        return redirect(url_for('dashboard'))
                except mysql.connector.Error as e:
                    print(f"MySQL Error: {e}")
                    cursor.close()
                    operator_data = fetch_user_data_by_operator_id(operator_id)
                    return redirect(url_for('dashboard'))

                # Commit the changes
                mysql.commit()

@app.route('/get_user_info/<int:operator_id>', methods=['GET'])
def get_user_info(operator_id):
    # Query the database to fetch data from data_table
    cursor = mysql.cursor()

    query_data = "SELECT entry_date, complete_data, today_hours, remain_data FROM data_table WHERE operator_id = %s ORDER BY entry_date DESC"
    cursor.execute(query_data, (operator_id,))
    user_data = cursor.fetchall()

    # Query the database to fetch data from operator_db
    query_operator = "SELECT totaldata, completedata, remaindata, assignday, remainday, totalhours FROM operators_db WHERE operator_id = %s"
    cursor.execute(query_operator, (operator_id,))
    operator_data = cursor.fetchone()

    cursor.close()

    if user_data:
        user_info = []

        for record in user_data:
            entry_date, complete_data, total_hours, remain_data = record

            user_info.append({
                'entry_date': entry_date.strftime('%Y-%m-%d'),
                'complete_data': complete_data,
                'total_hours': total_hours,
                'remain_data': remain_data
            })

        if operator_data:
            operator_info = {
                'total_data': operator_data[0],
                'complete_data': operator_data[1],
                'remain_data': operator_data[2],
                'assigned_day': operator_data[3],
                'remain_day': operator_data[4],
                'total_hours': operator_data[5]
            }

        return jsonify({'user_info': user_info, 'operator_info': operator_info})
    else:
        return jsonify({'error': 'User not found'}, 404)
#--------------Screenshot Technique---------------------

# import os
# import time
# import mss
# from flask import send_from_directory


# # Define the directory to save the screenshots
# screenshot_directory = 'screenshots/'
# os.makedirs(screenshot_directory, exist_ok=True)

# def capture_and_save_screenshot():
#     while True:
#         # Capture a screenshot of the entire screen
#         with mss.mss() as sct:
#             screenshot = sct.shot(output=os.path.join(screenshot_directory, f"screenshot_{time.strftime('%Y%m%d%H%M%S')}.png"))

#         # Sleep for 3 seconds before capturing the next screenshot
#         time.sleep(30)

# # Start capturing screenshots in a separate thread
# from threading import Thread
# screenshot_thread = Thread(target=capture_and_save_screenshot)
# screenshot_thread.daemon = True
# screenshot_thread.start()

# @app.route('/capture_screenshot', methods=['GET'])
# def capture_screenshot_route():
#     # Provide a link to the captured screenshot directory
#     screenshot_link = "/screenshots/"
#     return jsonify({"message": "Screenshots are being captured every 3 seconds", "screenshot_link": screenshot_link})

# # Serve the captured screenshots
# @app.route('/screenshots/<filename>', methods=['GET'])
# def screenshot(filename):
#     return send_from_directory('screenshots', filename)


if __name__ == '__main__':
    app.run(debug=True)
    
