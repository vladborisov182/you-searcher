class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://lembsogecgixpr:fef72d9c605d6d7acdaa26f9d1bc125a58f28d6eaa8e80d5bd0f8d7f5d05c68e@ec2-23-23-245-89.compute-1.amazonaws.com:5432/da1mm6uia1ifgg'
    CSRF_ENABLED = True
    SECRET_KEY='welc0me'

    ### Flask sequrity ###
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'