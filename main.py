import sqlite3
from datetime import datetime
from random import randint
from time import sleep 

con = sqlite3.connect("control.bd")
print("Criando banco de dados")

con.execute("""CREATE TABLE IF NOT EXISTS leituras(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            tipo_leitura INTEGER NOT NULL,
            id_mac VARCHAR(10),
            data_hora DATE,
            leitura integer )""")
print("Criando tabela")

script = "SELECT * FROM leituras;"
con.execute(script)

print(script)

print("Lendo temperaturas")
for i in range(1,60):
    
    tp = 1
    mac = "sp32_sensor01"
    vl = randint(-99, 99)
    data_e_hora = datetime.now()
    sleep(2)
    print(i, tp, mac, vl, data_e_hora)

    script = "INSERT INTO leituras (tipo_leitura, id_mac, data_hora, leitura) VALUES (?, ?, ?, ?);"
    con.execute(script, (tp, mac, vl, data_e_hora)) # execute the script

con.commit()
print("programa encerrado")
