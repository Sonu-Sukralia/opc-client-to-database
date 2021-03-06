import time
from opcua import Client
import mysql.connector

# SIEMENS OPC SERVER URL.
url = "opc.tcp://192.168.0.200:4840"
#"http://localhost" / "opc.tcp://192.168.0.200:4840"
client = Client(url)
client.connect()
print("Client connected")

#SENSOR VALUES INSIDE SIEMENS OPC SERVER.
while True:
    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print(f"Temperature is = {Temperature}")

    Press = client.get_node("ns=2;i=3")
    Pressure = Press.get_value()
    print(f"Pressure is = {Pressure}")

    TIME = client.get_node("ns=2;i=4")
    TIME_value = TIME.get_value()
    print(TIME_value)
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port="3306",
        database="testopc1"
    )
    cur=con.cursor()
    sql="insert into opc(pressure,temperature,Cur_date) value(%s,%s,%s)"
    cur.execute(sql,[Pressure,Temperature,TIME_value])
    con.commit()
    print("inserted")
    con.close()
    time.sleep(1)


