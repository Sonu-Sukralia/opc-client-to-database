import time
from opcua import Server
from random import randint
import datetime

server = Server()
url = "opc.tcp://192.168.0.200:4840"
#url = "opc.tcp://192.168.0.204:4840"
# "http://localhost"
server.set_endpoint(url)

name = "Simulation"
addspace = server.register_namespace(name)
node = server.get_objects_node()

Parm = node.add_object(addspace, "Parameters")

Temp = Parm.add_variable(addspace, "Temperature", 0)
Pres = Parm.add_variable(addspace, "Pressure", 0)
Tim = Parm.add_variable(addspace, "Time", 0)

Temp.set_writable()
Pres.set_writable()
Tim.set_writable()

server.start()
print("Server Start at {}".format(url))
while True:
    Temperature = randint(10, 50)
    Pressure = randint(200, 999)
    Time = datetime.datetime.now()

    print(Temperature, Pressure, Time)

    Temp.set_value(Temperature)
    Pres.set_value(Pressure)
    Tim.set_value(Time)
    time.sleep(1)
