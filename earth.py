
from math import sin, cos, sqrt, atan2, exp

W, H = 140, 64
CHARS = "  .,:-~+=*xX#%@"
RESET = "\033[0m"

def rgb(r, g, b):
    return f"\033[38;2;{int(r)};{int(g)};{int(b)}m"

def noise(x, y):
    n = sin(x*127.1 + y*311.7)*43758.5453
    return n - int(n)

print("\033[2J\033[H")
print(rgb(230, 230, 255))
print("\n                 THAT'S NO EARTH!\n" + RESET)

for j in range(H):
    for i in range(W):

        x = (i-W/2)/(W/2)
        y = (j-H/2)/(H/2)*1.05

        r = sqrt(x*x+y*y)

        # Space outside Earth
        if r > 0.94:
            if noise(i, j) > 0.993:
                print(rgb(220, 225, 255)+"*"+RESET, end="")
            else:
                print(" ", end="")
            continue

        # Spherical surface coordinates
        z = sqrt(max(0, 1-r*r))
        lon = atan2(y, x)
        lat = atan2(z, r)

        # Continental landmass patterns
        land = (
            sin(x*5 + sin(y*7)*0.8)
            + cos(y*8 + x*3)*0.7
            + sin(x*11+y*6)*0.35
            + cos(x*4-y*12)*0.25
        )

        continents = land > 0.55

        # Ocean depth
        ocean = 0.15 + 0.3*noise(i*2, j*2)

        # Clouds
        clouds = (
            sin(x*19+y*13)
            + cos(y*25-x*11)
            + sin(x*31-y*18)
        ) / 3

        cloud = clouds > 0.55

        # Atmospheric rim
        atmosphere = exp(-((r-0.91)/0.025)**2)

        # Day and night shading
        sunlight = max(0, 0.3+0.7*cos(x*1.4+y*0.8))

        if continents:
            R, G, B = 65, 145, 75
        else:
            R, G, B = 12, 65, 145

        if continents and land > 1.1:
            R, G, B = 145, 115, 65

        if cloud:
            R, G, B = 205, 220, 235

        R *= sunlight
        G *= sunlight
        B *= sunlight

        R += atmosphere*30
        G += atmosphere*100
        B += atmosphere*180

        # Character brightness
        brightness = (0.299*R+0.587*G+0.114*B)/255
        brightness = max(0, min(1, brightness))

        index = int(brightness*(len(CHARS)-1))
        char = CHARS[index]

        # Circular outline
        if abs(r-0.94) < 0.009:
            char = "."
            R, G, B = 220, 235, 255

        print(rgb(R, G, B)+char+RESET, end="")

    print()

print("\n"+rgb(230, 230, 255))
print("                  IT'S OUR HOME hehe.")
print(RESET)
