"""
Python version of https://www.openprocessing.org/sketch/405926 by Saskia Freeke
"""

t = 0.0
theta = 0.0
max_frame_count = 200


def setup():
    size(540, 540)
    noStroke()


def draw():
    background("#242949")
    translate(width / 2, height / 2)

    t = float(frameCount) / max_frame_count
    theta = TWO_PI * t

    for x in xrange(-175, 176, 25):
        for y in xrange(-100, 156, 50):
            offSet = float(50 * x + y + y)

            x2 = float(map(cos(-theta + offSet), 0, 1, 0, 25))
            y2 = float(map(cos(-theta + offSet), 0, 1, 25, 0))
            sz2 = float(map(sin(-theta + offSet), 0, 1, 15, 45))

            fill(250 - (x / 2), 150 + (x / 6), 250 - (y / 2))

            ellipse(x + x2, y - y2, sz2, sz2)
