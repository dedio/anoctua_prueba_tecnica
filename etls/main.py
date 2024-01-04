#~ Punto 1

import csv, sqlite3

#~ Conecta con la base de datos y crea un cursor
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

#~ Crea la tabla cotizaciones
cur.execute("DROP TABLE IF EXISTS cotizaciones;")
cur.execute("CREATE TABLE cotizaciones (indice_tiempo, tipo_cambio_bna_vendedor);")

#~ Abre el fichero csv y transforma los datos en una lista
with open('data/data.csv','r') as data:
    dr = csv.DictReader(data)
    to_db = [(i['indice_tiempo'], i['tipo_cambio_bna_vendedor']) for i in dr]

#~ Carga los datos transformados en la tabla cotizaciones
cur.executemany("INSERT INTO cotizaciones (indice_tiempo, tipo_cambio_bna_vendedor) VALUES (?, ?);", to_db)

#~ Hace el commit y cierra la conexión
con.commit()
con.close()
