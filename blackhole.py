
from math import sin, cos, sqrt, exp
for y in range(-21, 21):
    for x in range(-75, 75):
        a, b = x / 34, y / 20
        d = 1 - a*a - b*b
        v = (0.99*b - 0.14*a) / 0.22
        u = (0.99*a + 0.14*b)
        r = sqrt(u*u + v*v)
        angle = __import__('math').atan2(v, u)
        ring = exp(-((r-1.8)/0.13)**2)
        disk = exp(-((v-0.04*sin(u*5))/0.16)**2)
        swirl = 0.65 + 0.2*sin(angle*8+r*12) + 0.15*cos(u*25)
        glow = ring*(0.8+0.2*sin(angle*5))
        light = 0.02
        if d > 0:
            light += disk*swirl*0.9
        if r > 1.3 and r < 2.3 and (d < 0 or v > 0):
            light += glow*0.9
        light += 0.12*exp(-((r-1.95)/0.3)**2)
        if d > 0 and r < 0.95:
            light = 0
        light = max(0, min(light, 0.99))
        q = int(light*255)
        i = q*10//256
        c = f"\033[38;2;255;{int(100+155*light)};{int(20+220*light)}m"
        print(c + " .:-=+*#%@"[i], end="")
    print()
