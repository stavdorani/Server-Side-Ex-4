from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from datetime import timedelta

app = Flask(__name__)


app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=25)


@app.route('/')
def first_page():
    return redirect(url_for('home_page'))


@app.route('/home')
def home_page():
    return render_template('home page.html')


@app.route('/contact')
def contact_page():
    return render_template('contact us.html')


@app.route('/assignment3_1')
def assignment31_page():
    climbing_style = 'Bolder'
    bolder_climbing_sites = {'Preformance Rock TLV': 'https://performancerock.co.il/', 'Vking': 'https://vking.co.il/', 'The Block': 'https://www.thebloc.co.il/', 'Bolder Haifa': 'https://boulder.co.il/', 'Monkeys Climbing Gym': 'https://www.monkeysclimbinggym.co.il/'}
    sport_climbing_sites = {'iclimb TLV': 'https://iclimb.co.il/%D7%A1%D7%A0%D7%99%D7%A3-%D7%AA%D7%9C-%D7%90%D7%91%D7%99%D7%91-%D7%A8%D7%90%D7%A9%D7%99/', 'iclimb Jerusalem' : 'https://iclimb.co.il/jerusalem/%D7%A8%D7%90%D7%A9%D7%99/', 'Rockiz': 'https://www.rockiz.co.il/'}
    return render_template('assignment3_1.html',climbing_style=climbing_style,bolder_climbing_sites=bolder_climbing_sites,sport_climbing_sites=sport_climbing_sites)

users = {
    "user_1": {"name": "Omri", "email": "omri@gmail.com", "nic_name": "omi", "password": 'om123'},
    "user_2": {"name": "Ziv", "email": "ziv@gmail.com", "nic_name": "Dido", "password": 'zi123'},
    "user_3": {"name": "Ran", "email": "ran@gmail.com", "nic_name": "rano", "password": 'ra123'},
    "user_4": {"name": "Gal", "email": "gal@gmail.com", "nic_name": "galcha", "password": 'ga123'},
    "user_5": {"name": "Moshe", "email": "moshe@gmail.com", "nic_name": "mushnic", "password": 'mo123'}
}

password_dictionary_by_name = {}
for user in users:
    password_dictionary_by_name[users[user]["name"]] = users[user]["password"]

### assignment 4
from page.assignment_4 import assignment_4
app.register_blueprint(assignment_4)


@app.route('/assignment3_2',methods=['GET','POST'])
def assignment32_page():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        if user_name in password_dictionary_by_name:
            user_password = password_dictionary_by_name[user_name]
            if password == user_password:
                session['user_name'] = user_name
                for user in users:
                    if users[user]["name"] == user_name:
                        session['nic_name'] = users[user]["nic_name"]
                        break
                return render_template('assignment3_2.html',
                                       message='You are in!',
                                       user_name=user_name)
            else:
                return render_template('assignment3_2.html',
                                       message='Wrong password!')
        else:
            return render_template('assignment3_2.html',
                                   message='Please sign in!')
    if "name" in request.args:
        name = request.args["name"]
        if name == '':
            return render_template('assignment3_2.html', all_users=users)
        is_user_in_the_dict = 0
        for user_name in users.values():
            if user_name['name'] == name:
                the_user = user_name
                is_user_in_the_dict = 1
                break
        if is_user_in_the_dict == 1:
            return render_template('assignment3_2.html',
                                   name=the_user['name'],
                                   email=the_user['email'],
                                   nic_name=the_user['nic_name'])
        else:
            return render_template('assignment3_2.html',
                                   message2='Try Again I Cant Find the User')
    return render_template('assignment3_2.html',
                           all_users=users)


@app.route('/log_out')
def logout_func():
    session.clear()
    return redirect(url_for('assignment32_page'))


@app.route('/session')
def session_func():
    return jsonify(dict(session))


if __name__ == '__main__':
    app.run(debug=True)
