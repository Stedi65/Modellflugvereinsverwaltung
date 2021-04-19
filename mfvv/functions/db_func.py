from sqlalchemy import create_engine


def db_system(db: str):
    db_systems = {
        'sqlite3':'db_modul_sqlite',
        'PostgreSQL':'db_modul_postgresql',
        'mysql': 'db_modul_mysql',
        'mariadb': 'db_modul_mariadb'
    }
    return db_systems.get(db.lower())


def create_db_engine(db_sys: str, user: str, password: str, host: str, port: str, name: str):
    engine = ""
    if db_sys == 'sqlite3':
        engine = create_engine(f'sqlite:///data{name}')

    if db_sys == 'PostgreSQL':
        engine = create_engine(f'postgresql+pg8000:/{user}:{password}@{host}/data/{name}')

    if db_sys == 'mysql':
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/data/{name}?charset=utf8mb4')

    if db_sys == 'mariadb':
        engine = create_engine(f'mariadb+pymysql://{user}:{password}@{host}:{port}/data/{name}?charset=utf8mb4')

    return engine
