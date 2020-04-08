from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField , IntegerField,SelectField,RadioField ,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,required ,length
from models import User


from wtforms.widgets.html5 import NumberInput


import phonenumbers
from models import *
from validate_email import validate_email as ve

class RegistrationForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeter le mot de passe', validators=[DataRequired(), EqualTo('password',message='Les mots de passe ne correspondent pas')])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Nom d'utilisateur existant")

    def validate_password(self, password):
        if len(password.data) < 4:
            raise ValidationError("Le mot de passe doit contenir au moins 4 caractères")




class LoginForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    """
    def validate_username(self, username):
        if len(username.data) < 3 :
            raise ValidationError("Nom d'utilisateur doit contenir au moins 3 caractères")"""

class ProfileForm(FlaskForm):
    username = StringField('Nom', validators=[DataRequired()])
    adresse = StringField('Adresse')
    email = StringField('Email')
    telephone = StringField('Numéro de téléphone')

    def validate_email(self,email):
        if email.data:
            if ve(email.data)==False:
                raise ValidationError('Email invalide')
        else:
            print("pas d'email")

    def validate_telephone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Numéro de téléphone invalide')


class ExamenForm(FlaskForm):
    age = IntegerField(widget=NumberInput())
    sexe=RadioField('Sexe', choices=[('Homme','Homme'),('Femme','Femme')])
    touxrecente = RadioField('Avez vous eu une toux récente ?', choices=[('Oui','Oui'),('Non','Non')])
    respirer = RadioField('Avez vous eu des difficultés à respirer ?', choices=[('Oui','Oui'),('Non','Non')])

    fievreSensation = RadioField('Avez vous eu une sensation de fièvre ?', choices=[('Oui','Oui'),('Non','Non')])
    fievre = RadioField('Avez vous eu de la fièvre ?', choices=[('Oui','Oui'),('Non','Non')])
    malGorge = RadioField('Avez vous eu un mal de gorge ?', choices=[('Oui','Oui'),('Non','Non')])
    impossibiliteManger = RadioField('Avez vous eu une impossibilité de manger ou boire depuis 24 heures ou plus ?', choices=[('Oui','Oui'),('Non','Non')])
    
    courbatures = RadioField('Avez-vous des courbatures en dehors des douleurs musculaires liées à une activité sportive intense ?', choices=[('Oui','Oui'),('Non','Non')])
    perteOrdorat = RadioField('Avez-vous perdu l’odorat de manière brutale sans rapport avec le nez bouché ?', choices=[('Oui','Oui'),('Non','Non')])
    diarrhee = RadioField('Avez-vous la diarrhée ?', choices=[('Oui','Oui'),('Non','Non')])
    maladieConnu = RadioField('Avez-vous une autre maladie connue ?', choices=[('Oui','Oui'),('Non','Non')])


class SavoirForm(FlaskForm):
    modeTransmission=RadioField('Comment la maladie à coronavirus (COVID-19) se transmet-elle ?', choices=[('V','Par des gouttelettes respiratoires produites par une personne qui tousse ou éternue'),('F','En touchant des surfaces contaminées par le virus et en se touchant ensuite le visage'),('Les deux ','Les deux V')])
    touxrecente = RadioField('Mon animal de compagnie peut-il me transmettre la maladie à coronavirus (COVID-19) ?', choices=[('F','Oui'),('V','NonV')])
    respirer = RadioField('Avez vous eu des difficultés à respirer ?', choices=[('Oui','Oui'),('Non','Non')])

    fievreSensation = RadioField('Avez vous eu une sensation de fièvre ?', choices=[('Oui','Oui'),('Non','Non')])
    fievre = RadioField('Avez vous eu de la fièvre ?', choices=[('Oui','Oui'),('Non','Non')])
    malGorge = RadioField('Avez vous eu un mal de gorge ?', choices=[('Oui','Oui'),('Non','Non')])
    impossibiliteManger = RadioField('Avez vous eu une impossibilité de manger ou boire depuis 24 heures ou plus ?', choices=[('Oui','Oui'),('Non','Non')])
    
    courbatures = RadioField('Avez-vous des courbatures en dehors des douleurs musculaires liées à une activité sportive intense ?', choices=[('Oui','Oui'),('Non','Non')])
    perteOrdorat = RadioField('Avez-vous perdu l’odorat de manière brutale sans rapport avec le nez bouché ?', choices=[('Oui','Oui'),('Non','Non')])
    diarrhee = RadioField('Avez-vous la diarrhée ?', choices=[('Oui','Oui'),('Non','Non')])
    maladieConnu = RadioField('Avez-vous une autre maladie connue ?', choices=[('Oui','Oui'),('Non','Non')])




class DeclarationForm(FlaskForm):
    lieu = StringField("Le lieu de l'évènement")
    descriptif = TextAreaField(f"Que se passe t'il concrètement ?", [required(),length(max=200)])
    
class DonForm(FlaskForm):
    descriptif = TextAreaField(u'Décrivez nous ce que vous aimeriez donner et grâce à votre adresse nous viendrons récupérer 😊 ', [required(),length(max=200)])
    


