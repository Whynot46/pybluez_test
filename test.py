import bluetooth
import asyncio

temp = {
    's_temp': 0.0,
    's_incline': 0.0,
    'a_engine_power': 0,
    'a_engine_angle': 0.0,
    'a_sail_angle': 0.0,
    'a_flaperon_angle': 0.0}
'''
0 - s_temp -- температруа
1 - s_incline -- крен
2 - a_engine_power -- мощность двигателя в (0-100%)
3 - a_engine_angle -- поворот двигателя (-90 - 0 - 90)
4 - a_sail_angle - поворот паруса (-90 - 0 - 90)
5 - a_flaperon_angle - поворот флаперона (-90 - 0 - 90)
'''


s_temp = 0.0
s_incline = 0.0
data=(f"engine_power:{str(1)}||engine_angle:{str(1.0)}||sail_angle:{str(1.0)}||flaperon_angle:{str(1.0)}")


server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_sock.bind(("", port))
server_sock.listen(1)


async def main():
    temp['s_temp'] = 0.1452
    while True:
        global a_engine_power, a_engine_angle, a_sail_angle, a_flaperon_angle
        client_sock, address = server_sock.accept()
        data = client_sock.recv(1024)
        print(f'From : {address}')
        a_engine_power, a_engine_angle, a_sail_angle, a_flaperon_angle = map(data.split("||"))
        a_engine_power = int(a_engine_power.partition(':')[-1])
        a_engine_angle = float(a_engine_angle.partition(':')[-1]) * 9
        a_sail_angle = float(a_sail_angle.partition(':')[-1]) * 9
        a_flaperon_angle = float(a_flaperon_angle.partition(':')[-1]) * 9
        if s_temp != temp['s_temp'] or s_incline != temp['s_incline'] or a_engine_power != temp['a_engine_power'] or a_engine_angle != temp['a_engine_angle'] or a_sail_angle != temp['a_sail_angle'] or a_flaperon_angle != ['a_flaperon_angle']:
            await update_temp()

async def update_temp():
        temp['s_temp'] = s_temp
        temp['s_incline'] = s_incline
        temp['a_engine_power'] = a_engine_power
        temp['a_engine_angle'] = a_engine_angle
        temp['a_sail_angle'] = a_sail_angle
        temp['a_flaperon_angle'] = a_flaperon_angle
        print(temp)

asyncio.run(main())
