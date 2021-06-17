SQLALCHEMY_DB_URI = '{driver}://{user}:{pwd}@{host}:{port}/{db}?charset=utf8' \
    .format(
        driver='mysql+pymysql',  # or 'postgresql+psycopg2'
        host='localhost',
        port='5566',
        user='root',
        pwd='0000',
        db='test_db'
    )
