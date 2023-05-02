import flask_wtf
import wtforms

class FormLogin(flask_wtf.FlaskForm):
    name = wtforms.StringField("Please, insert name", [wtforms.validators.DataRequired()])
    address = wtforms.StringField("Please, insert address", [wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")