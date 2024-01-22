from util import *

l = 2000000

cannot = set()
b = set()
for sensor_spec in lines():
    _, _, sx, sy, _, _, _, _, bx, by = sensor_spec.split()
    sensor = Vec2(int(sx[:-1].split('=')[1]), int(sy[:-1].split('=')[1]))
    beacon = Vec2(int(bx[:-1].split('=')[1]), int(by.split('=')[1]))
    if beacon.y == l:
        b.add(beacon.x)
    d = (sensor - beacon).manhattan()
    span = d - abs(sensor.y - l)
    cannot.update(range(sensor.x-span, sensor.x+span+1))

cannot -= b

print(len(cannot))