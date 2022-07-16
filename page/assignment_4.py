from flask import Flask, redirect, render_template, request,Blueprint, session, jsonify, url_for
import requests
import mysql.connector
# assignment 4 blueprint definition

assignment_4 = Blueprint('assignment_4', __name__, static_folder='static', static_url_path='/assignment_4', template_folder='templates')


# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='12345678',
                                         database='myDb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


def get_users():
    sqlquery = 'SELECT * FROM users'
    users = interact_db(sqlquery, query_type='fetch')
    return users


def get_user_by_id(id):
    sqlquery = "SELECT * FROM users where id='%s'" % id
    user = interact_db(sqlquery, query_type='fetch')
    return user

# Routes
@assignment_4.route('/assignment_4')
def assignment_4_func():
    users = get_users()
    return render_template('/assignment_4.html', users=users)


@assignment_4.route('/assignment_4/users', methods=['GET'])
def assignment_4_users_func():
    temp = {}
    users = get_users()
    for user in users:
        temp[user.id] = {
           'name': user.name,
           'email': user.email,
           'nick_name': user.nic_name,
           'password': user.password
        }
    return jsonify(temp)


@assignment_4.route('/assignment_4/outer_source', methods=['GET', 'POST'])
def assignment_4_outer_func():
    users = get_users()
    user_id = request.form['id']
    result = requests.get('https://reqres.in/api/users/' + user_id)
    return render_template('/assignment_4.html', reqres_api_users=result.json()['data'], users=users)


@assignment_4.route('/assignment_4/restapi_users/<int:USER_ID>', methods=['GET'])
def assignment_4_rest_func(USER_ID):
    user = get_user_by_id(USER_ID)
    if len(user) > 0:
        print(user)
        res = {
            'id': user[0].id,
            'email': user[0].email,
            'name': user[0].name,
            'nick_name': user[0].nic_name
        }
        return jsonify(res)
    return jsonify({
        'error': '404',
        'message': "can't find this user :("
    })


# ------------------------------------------------- #
# -------------------- INSERT --------------------- #
# ------------------------------------------------- #
@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['name']
    email = request.form['email']
    nic_name = request.form['nic_name']
    password = request.form['password']
    query1 = "SELECT * FROM users WHERE email='%s';" % email
    ans = ''
    try:
        ans = interact_db(query=query1, query_type='commit')
    except:
        message = 'This email in use try again'
        users = get_users()
        return render_template('/assignment_4.html', users=users, email_in_use=True)
    else:
        query2 = "INSERT INTO users(name, email, nic_name, password) VALUES ('%s', '%s', '%s', '%s')" % (name, email, nic_name, password)
        interact_db(query=query2, query_type='commit')
        return redirect('/assignment_4')


# ------------------------------------------------- #
# -------------------- UPDATE --------------------- #
# ------------------------------------------------- #
@assignment_4.route('/update_user_name', methods=['POST'])
def update_user_name_func():
    user_id = request.form['user_id']
    name = request.form['name']
    query = "UPDATE users SET name='%s' WHERE id='%s';" % (name, user_id)
    interact_db(query, query_type='commit')
    message = f'the user name with number id: {user_id} is: {name}'
    users = get_users()
    return render_template('/assignment_4.html', users=users, message_up_name=message)


@assignment_4.route('/update_user_email', methods=['POST'])
def update_user_email_func():
    user_id = request.form['user_id']
    email = request.form['email']
    query = "UPDATE users SET email='%s' WHERE id='%s';" % (email, user_id)
    interact_db(query, query_type='commit')
    message = f'the user email with number id: {user_id} is: {email}'
    users = get_users()
    return render_template('/assignment_4.html', users=users, message_up_email=message)


# ------------------------------------------------- #
# -------------------- DELETE --------------------- #
# ------------------------------------------------- #
@assignment_4.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['user_id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query, query_type='commit')
    message = f'the user with number id: {user_id} as been deleted'
    users = get_users()
    return render_template('/assignment_4.html', users=users, message_del=message)


