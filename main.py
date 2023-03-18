from src.perlinNoise import PerlinNoise
from random import randint
noise = PerlinNoise(2000, 2000, randint(0, 999999), 300)
noise.create_image()