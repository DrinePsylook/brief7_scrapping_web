import sqlite3

def create_table_pib():
    create_request = '''DROP TABLE IF EXISTS customer;
                    CREATE TABLE country_pib(
                        rang INT NOT NULL UNIQUE,
                        country VARCHAR(100) NOT NULL,
                        pib INT NOT NULL UNIQUE,
                        PRIMARY KEY (rang)
                    ); '''
    db_con = sqlite3.connect("flaskr/data.db")
    cur = db_con.cursor()
    cur.execute(create_request)

def insert_table_pib(infos):
    sql_request = "INSERT INTO country_pib(rang, country, pib) VALUES (?,?,?)"
    for info in infos :
        print(info)