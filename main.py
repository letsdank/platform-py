from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from src.base.contact_info.module.management import internal_world_countries

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:password@localhost:5432/platform_python_db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return internal_world_countries.get_world_country_code('40')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
