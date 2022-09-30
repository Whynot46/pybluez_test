import bluetooth

bd_addr = "B0:FC:36:F5:C3:F0"

port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

sock.send("I am alive!")

sock.close()
