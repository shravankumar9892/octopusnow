from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.fields import BooleanField, DecimalField, FloatField
from wtforms.validators import DataRequired

class ThyroidtypedetectionForm(FlaskForm):
    age = DecimalField('age', validators=[DataRequired()])
    sex = BooleanField('sex', validators=[DataRequired()])
    on_thyroxine = BooleanField('on_thyroxine', validators=[DataRequired()])
    query_on_thyroxine = BooleanField('query_on_thyroxine', validators=[DataRequired()])
    antithyroid_medication = BooleanField('age', validators=[DataRequired()])
    sick = BooleanField('sick', validators=[DataRequired()])
    pregnant = BooleanField('pregnant', validators=[DataRequired()])
    thyroid_surgery = BooleanField('thyroid_surgery', validators=[DataRequired()])
    I131_treatment = BooleanField('I131_treatment', validators=[DataRequired()])
    query_hypothyroid = BooleanField('query_hypothyroid', validators=[DataRequired()])
    query_hyperthyroid = BooleanField('query_hyperthyroid', validators=[DataRequired()])
    lithium = BooleanField('lithium', validators=[DataRequired()])
    goitre = BooleanField('goitre', validators=[DataRequired()])
    tumor = BooleanField('tumor', validators=[DataRequired()])
    hypopituitary = BooleanField('hypopituitary', validators=[DataRequired()])
    psych = BooleanField('psych', validators=[DataRequired()])
    TSH = FloatField('TSH', validators=[DataRequired()])
    T3 = FloatField('T3', validators=[DataRequired()])
    TT4 = FloatField('TT4', validators=[DataRequired()])
    T4U = FloatField('T4U', validators=[DataRequired()])
    FTI = FloatField('FTI', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class Paul(FlaskForm):
    text = StringField('Ask Paul', validators=[DataRequired()])
    submit = SubmitField('Submit')