import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


DB_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'.format(
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT'),
    database=os.environ.get('DB_NAME')
)
