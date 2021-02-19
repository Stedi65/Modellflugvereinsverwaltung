import platform


def load_config(cfg_file: str) -> dict:
    res_dict = {}
    with open(cfg_file, "r") as fobj:
        for line in fobj:
            tmp = line.replace("\n", "").split(':')
            key = tmp[0]
            value = tmp[1]
            res_dict.update({key:value})
    return res_dict


def check_os():
    return platform.system().lower()


def db_system(db: str):
    db_systems = {
        'sqlite3':'db_modul_sqlite',
        'mysql': 'db_modul_mysql',
        'mariadb': 'db_modul_mariadb'
    }
    return db_systems.get(db.lower())


def main():
    operating_system = check_os()
    mfvv_config = load_config("mfvv.cfg")
    db_sys = db_system(mfvv_config.get("db_system"))

    print(f"Betriebsystem  : {operating_system}")
    print(f"Datenbanksystem: {db_sys}")



if __name__ == '__main__':
    main()