from PIL import Image
import random
import math

import random
from PIL import Image


class FractalPerlinNoise:
    def __init__(self, width, height, seed, frequency, lacunarity=2.0, octaves=5, persistence=0.5):
        self.width = width
        self.height = height
        self.seed = seed
        self.frequency = frequency
        self.octaves = octaves
        self.lacunarity = lacunarity
        self.persistence = persistence
        self.p = self.generate_permutation_table(seed)

    def fade(self, t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(self, t, a, b):
        return a + t * (b - a)

    def grad(self, hash, x, y):
        h = hash & 7
        u = x if h < 4 else y
        v = y if h < 4 else x
        return ((hash & 8) and -u or u) + ((hash & 1) and -v or v)

    def perlin(self, x, y):
        X = int(x) & 255
        Y = int(y) & 255
        xf = x - int(x)
        yf = y - int(y)
        u = self.fade(xf)
        v = self.fade(yf)
        A = self.p[X] + Y
        AA = self.p[A]
        AB = self.p[A+1]
        B = self.p[X+1] + Y
        BA = self.p[B]
        BB = self.p[B+1]
        return self.lerp(v, self.lerp(u, self.grad(self.p[AA], xf, yf),
                           self.grad(self.p[BA], xf-1, yf)),
                   self.lerp(u, self.grad(self.p[AB], xf, yf-1),
                           self.grad(self.p[BB], xf-1, yf-1)))

    def generate_permutation_table(self, seed):
        permutation = list(range(256))
        random.seed(seed)
        random.shuffle(permutation)
        return permutation * 2

    def get_perlin_value(self, x, y, zoom=1):
        amplitude = 1
        frequency = self.frequency
        noise_value = 0
        for i in range(self.octaves):
            noise_value += self.perlin(x * frequency * zoom, y * frequency * zoom) * amplitude
            amplitude *= self.persistence
            frequency *= self.lacunarity
        normalized_value = (noise_value + 1) / 2
        perlin_color = int(normalized_value * 255)
        return perlin_color

    def create_image(self):
        img = Image.new("RGB", (self.width, self.height), (0, 0, 0))
        for i in range(self.width):
            for j in range(self.height):
                perlin_color = self.get_perlin_value(i, j)
                img.putpixel((i, j), (perlin_color, perlin_color, perlin_color))
        img.show()
        img.save('fractal_perlin_noise.png')
        return img


