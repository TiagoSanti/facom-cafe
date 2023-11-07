class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/tads_local?options=-csearch_path%3Dfacom_cafe_schema'
    SQLALCHEMY_TRACK_MODIFICATIONS = False