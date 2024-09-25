from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField


class AddSnackForm(FlaskForm):

    name = StringField('name Snack')
    price = FloatField('price in USD')
    is_healthy = BooleanField('This is a  healthy snack')
    Quantity = IntegerField('How many?')

    Catergory = RadioField('Category', choices = [('ic', 'Ice Cream'), ('chips', 'poptatoes Chips'), ('candy', 'Candy/Sweets')])
    Catergory = SelectField('Category', choices = [('ic', 'Ice Cream'), ('chips', 'poptatoes Chips'), ('candy', 'Candy/Sweets')])

    prioity = SelectField('priority', choices=[(1, 'High'),(2, 'Low')], coerce=int)

class NewEmployeeForm(FlaskForm):

    name = StringField('Employee Name')
    state = StringField('State')
    dept_code = StringField('Department Code')
