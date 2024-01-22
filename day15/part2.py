from util import *

cannot = [IntervalSet([]) for _ in range(4000001)]
for sensor_spec in lines():
    _, _, sx, sy, _, _, _, _, bx, by = sensor_spec.split()
    sensor = Vec2(int(sx[:-1].split('=')[1]), int(sy[:-1].split('=')[1]))
    beacon = Vec2(int(bx[:-1].split('=')[1]), int(by.split('=')[1]))
    d = (sensor - beacon).manhattan()
    for l in range(max(sensor.y-d, 0), min(sensor.y+d, 4000001)):
        span = d - abs(sensor.y - l)
        cannot[l].add(Interval(sensor.x-span, sensor.x+span))

for y in range(4000001):
    if not cannot[y].contains(Interval(0, 4000000)):
        iset = cannot[y]
        x = iset.intervals[0].hi+1
        print(x * 4000000 + y)
        break
