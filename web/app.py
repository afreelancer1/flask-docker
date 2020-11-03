from flask import Flask, render_template, flash, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import random
import math

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class primeForm(FlaskForm):
    mx = StringField('Maximum', validators=[DataRequired()])
    last = StringField('Last', validators=[DataRequired()])
    submit = SubmitField('Submit')

    @app.route('/', methods=['GET', 'POST'])
    def get_info():
        if request.method == 'POST':  # this block is only entered when the form is submitted
            number = int(request.form.get('mx'))
            end = request.form.get('last')
            all_numbers = []

            for i in range(2, number + 1):
                all_numbers.append(i)

            x = all_numbers[0]
            while x < len(all_numbers):
                for i in all_numbers:
                    if i == x or x > i or x > math.sqrt(number):
                        continue
                    elif i % x == 0:
                        all_numbers.remove(i)
                x = all_numbers[(all_numbers.index(x)) + 1]

            last_int = {}
            for i in all_numbers:
                l = str(i)[-1]
                if not l in last_int:
                    last_int[l] = [i]
                else:
                    last_int[l].append(i)

            prime = last_int[end][random.randint(0, len(last_int[end]))]
            return prime
        else:
            return '''<form method="POST">
    <p style="text-align: center;">You want a prime number between 2 and&nbsp; <input type="text" name="mx" /> that ends with&nbsp; <input type="text" name="last" /></p>
    <p style="text-align: center;"><br /> <input type="submit" value="Submit" /></p>
    </form>'''


app.run(host='0.0.0.0', port=5000)
