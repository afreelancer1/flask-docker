from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

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
<h3 style="text-align: center;"><br /><span style="color: #808080;">You want a prime number between 2 and <input type="text" /> ending in <input list="browsers" type="text" /></span></h3>'''

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    
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
