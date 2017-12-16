class Configuration(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://esydispabrrdtx:74fe323264f1b9d38bdb43ce157dfba764ed23886a1abb6193927fe9168c87a3@ec2-184-72-228-128.compute-1.amazonaws.com:5432/de553hborc4cpf'
    CSRF_ENABLED = True
    SECRET_KEY='welc0me'

    ### Flask sequrity ###
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'