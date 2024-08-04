from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, FileField
from wtforms.validators import DataRequired, NumberRange

class DebtForm(FlaskForm):
    # Debt Owner Information
    debt_owner_name = StringField('Debt Owner Name', validators=[DataRequired()])
    debt_owner_phone = StringField('Debt Owner Phone', validators=[DataRequired()])
    debt_owner_image = FileField('Debt Owner Image')
    
    # Debt Details
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    duration_days = IntegerField('Duration (days)', validators=[DataRequired(), NumberRange(min=1)])
    
    # Borrower Information
    borrower_name = StringField('Borrower Name', validators=[DataRequired()])
    borrower_phone = StringField('Borrower Phone', validators=[DataRequired()])
    borrower_image = FileField('Borrower Image')
    
    # Bail Information
    bail_name = StringField('Bail Name', validators=[DataRequired()])
    bail_phone = StringField('Bail Phone', validators=[DataRequired()])
    bail_image = FileField('Bail Image')

    submit = SubmitField('Add Debt')
