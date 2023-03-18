from src.perlinNoise import FractalPerlinNoise
from random import randint
noise = FractalPerlinNoise(512, 512, 42, 0.02)
noise.create_image()