from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import random

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
testest = '''<datalist id="browsers">
<option value="1"></option>
<option value="3"></option>
<option value="5"></option>
<option value="7"></option>
<option value="9"></option>
</datalist>
<form action="/prime">
<h3 style="text-align: center;"><br /><span style="color: #808080;">You want a prime number between 2 and <input type="text" id="mx" name="mx" /> ending in <input list="browsers" type="text" id="last" name="last" /></span></h3>
<h3 style="text-align: center;"><input type="submit" value="Submit" /></h3>
</form>'''

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    
    @app.route("/prime", methods=['GET', 'POST'])
    def get_prime():
        number = request.args.get('mx')
        end = request.args.get('last')
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
        ends_in = ['2', '3', '5', '7', '1', '9']
        for i in all_numbers:
            l = str(i)[-1]
            if not l in last_int:
                last_int[l] = [i]
            else:
                last_int[l].append(i)

        prime = last_int[end][random.randint(0, len(last_int[end]))]
        return "Your prime number is " + str(prime)

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
        
        print form.errors
        if request.method == 'POST':
            name=request.form['name']
            print name
        
        if form.validate():
        # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('Error: All the form fields are required. ')
        
        return testest
 
app.run(host='0.0.0.0', port=5000)
