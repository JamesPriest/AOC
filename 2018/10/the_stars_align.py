import matplotlib.pyplot as plt
import numpy as np

def strip_arrows(string):
    return string.strip("><= ")


class particle:
    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

    def time_evolve(self):
        self.x += self.v_x
        self.y += self.v_y


data = open("input.txt").read().split("\n")
all_particles = []
for line in data:
    if line == "":
        continue
    pos, vel = map(strip_arrows, line.strip("position").split(" velocity"))
    y, x = map(int, pos.split(", "))
    v_y, v_x = map(int, vel.split(", "))
    _part = particle(x, y, v_x, v_y)
    all_particles.append(_part)



# Main loop?
for i in range(122502):
    x_max, x_min = (
        max(all_particles, key=lambda x: x.x).x,
        min(all_particles, key=lambda x: x.x).x,
    )
    y_max, y_min = (
        max(all_particles, key=lambda x: x.y).y,
        min(all_particles, key=lambda x: x.y).y,
    )  
    if x_max < 200 and y_max < 200:
        
        # Generate matrix image
        # +1 due to input not being zero indexing..maybe
        image = np.zeros((x_max - x_min + 1, y_max - y_min + 1))
        
        for part in all_particles:
            image[part.x-x_min, part.y-y_min] = 1
        
        print(f"Iteration: {i}")

        # Show matrix image
        plt.imshow(image)
        plt.show()
    # Time evolve and repeat
    for part in all_particles:
        part.time_evolve()
