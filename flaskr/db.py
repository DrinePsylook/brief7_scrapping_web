import sqlite3

def create_table_pib():
    create_request = '''CREATE TABLE country_pib(
                        rang INT NOT NULL UNIQUE,
                        country VARCHAR(100),
                        pib INT NOT NULL,
                        PRIMARY KEY (rang)
                    ); '''
    db_con = sqlite3.connect("flaskr/data.db")
    cur = db_con.cursor()
    cur.execute(create_request)
    db_con.commit()
    db_con.close()

def insert_table_pib(infos):
    sql_request = "INSERT INTO country_pib(rang, country, pib) VALUES (?,?,?)"
    db_con = sqlite3.connect("flaskr/data.db")
    cur = db_con.cursor()
    for info in infos :
        print(f"infos = {info}")
        cur.execute(sql_request, (info[0], info[2], info[1]))
        db_con.commit()
    db_con.close()