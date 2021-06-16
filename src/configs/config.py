SQLALCHEMY_DB_URI = '{driver}://{user}:{pwd}@{host}/{db}?charset=utf8' \
    .format(
        driver='mysql+pymysql',  # or 'postgresql+psycopg2'
        host='localhost',
        user='root',
        pwd='0000',
        db='test_db'
    )
