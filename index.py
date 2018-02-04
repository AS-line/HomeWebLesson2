from flask import Flask, render_template, request
from models import db, Person

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        index_name = request.form.get("name_html_athribut", "noname")
        index_year = request.form.get('year_html_athribut', 1990)
        index_male = request.form.get('male_html_athribut', False)
        print(index_name, index_year, index_male)
        Person.create(name=index_name, year=index_year, male=index_male)
    persons = Person.select()
    return render_template('home.html', persons=persons)


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5001)
