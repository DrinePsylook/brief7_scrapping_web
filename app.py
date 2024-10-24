# imports flask
from flask import Flask, render_template
import sqlite3

from flaskr.db import create_table_pib, insert_table_pib
app = Flask(__name__)

# imports beautifulsoup
import requests
from bs4 import BeautifulSoup

@app.route("/")
def home():
    return render_template('index_template.html')

@app.route('/table/<name>')
def sql_table(name):
    db_con = sqlite3.connect("flaskr/data.db")
    cur = db_con.cursor()
    
    columns_name= []
    if name == "all":
        sql_request = '''SELECT customer.id AS id_client, customer.country AS pays, co.id AS id_commande_client, co.invoice_nb AS numero_facture, co.invoice_date AS date_facture, od.id AS id_detail_commande, od.quantity AS quantite, product.id AS id_produit, product.description AS description, product.price As prix     
                            FROM customer 
                            LEFT JOIN customer_order as co
                                ON customer.id = co.customer_id
                            LEFT JOIN order_detail as od
                                ON co.id = od.order_id
                            LEFT JOIN product
                                ON od.product_id = product.id
                            ORDER BY customer.id
                            LIMIT 50'''
    else:
        sql_request = f"SELECT * FROM {name} LIMIT 50"

    res = cur.execute(sql_request)
    resultat = res.fetchall()

    columns_name = [description[0] for description in cur.description]

    return render_template('tables_template.html', tables=resultat, name=name, col = columns_name)

@app.route('/tablePib')
def table_pib():
    url = "https://fr.wikipedia.org/wiki/Liste_des_pays_par_PIB_(PPA)_par_habitant"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    tableaux = soup.find_all('table')
    tbl2 = tableaux[2]
    ligne = tbl2.findAll('tr')
    quote= []
    for row in ligne:
        pays = row.findAll('a')
        td_elements = row.findAll('td')

        try:
            if len(td_elements) > 1 :
                quote.append([td_elements[0].get_text().strip(), td_elements[2].get_text().strip(), pays[1]['title']]) 
        except TypeError:
            continue
        print(quote)

    # create_table_pib()
    insert_table_pib(quote)

    return quote


    
