
class Config:
    TEST_VALUE = "CONFIG_VALUE"
    SECRET_KEY = b'\x08\x0e_\xb8\x94]\xacL\x13N\xedVD\xba\xfd\x85'
    PG_USER = "flask_app"
    PG_PASSWORD = "very_secret_password"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "falsk_app"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False