from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)
print(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/<string:html>')
def homepage2(html):
    return render_template(html)


@app.route('/contact_form', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        data = request.form.to_dict()
        email = request.form['E-mail']
        subject = request.form['Subject']
        message = request.form['Message']
        print(data)
        with open('database.txt', 'a') as database:
            database.write(f'{email}, {subject}, {message}\n')
        write_to_csv(data)
        # return render_template('thanks.html')
        return redirect('thanks.html')
    else:
        return 'something went wrong!!'


def write_to_csv(data):
    email2 = data['E-mail']
    subject2 = data['Subject']
    message2 = data['Message']
    with open('database.csv', 'a', newline='') as database2:
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email2, subject2, message2])





# @app.route('/about.html')
# def works():
#     return render_template('about.html')
#
#
# @app.route('/about.html')
# def works():
#     return render_template('about.html')


# @app.route('/contact_us')
# def contact_us():
#     return 'E-mail - Phone number - Instagram'
#
#
# @app.route('/contact_us/e-mail')
# def contact_us2():
#     return 'graphiumstudio@yahoo.com'
#
#
# @app.route('/sign_in.html')
# def sign_in():
#     return render_template('sign_in.html')
#
#
# @app.route('/<username>')
# def name(username=None):
#     return render_template('index.html', name=username)


@app.route('/<username>/<int:id2>')
def name_and_id(username=None, id2=None):
    return render_template('index.html', name=username, id=id2)


