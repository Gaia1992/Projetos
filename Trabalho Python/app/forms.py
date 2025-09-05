from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class ProductForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired(), Length(max=150)])
    sku = StringField('SKU', validators=[Length(max=80)])
    description = TextAreaField('Descrição')
    quantity = IntegerField('Quantidade', validators=[NumberRange(min=0)], default=0)
    min_quantity = IntegerField('Quantidade Mínima', validators=[NumberRange(min=0)], default=0)
    price = FloatField('Preço', validators=[NumberRange(min=0)], default=0.0)
    submit = SubmitField('Salvar')

class MovementForm(FlaskForm):
    product_id = SelectField('Produto', coerce=int, validators=[DataRequired()])
    type = SelectField('Tipo', choices=[('in','Entrada'), ('out','Saída')], validators=[DataRequired()])
    quantity = IntegerField('Quantidade', validators=[DataRequired(), NumberRange(min=1)])
    note = TextAreaField('Observação')
    submit = SubmitField('Registrar')

class UserForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Senha', validators=[DataRequired()])
    role = SelectField('Perfil', choices=[('admin','Administrador'), ('user','Comum')], validators=[DataRequired()])
    submit = SubmitField('Criar usuário')
