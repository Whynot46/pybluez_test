import bluetooth

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

bd_addr = "B0:FC:36:F5:C3:F0"
print(bd_addr)
bd_addr = str(input('Введи адрес, если хочешь его поменять <-- '))
if bd_addr=='':
    bd_addr = "B0:FC:36:F5:C3:F0"
    port = 0x1001
    sock.connect((bd_addr, port))
    sock.send("hello!!")
    sock.close()
else:
    port = 0x1001
    sock.connect((bd_addr, port))
    sock.send("hello!!")
    sock.close()
