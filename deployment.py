import pygame
import json

class Deploy:

    def __init__(self):
        f = open('config.json')
        data = json.load(f)

        pygame.init()
        self.window_size = data["initialization"]["window_size"]
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(data["credits"]["title"])

        self.H_FPS = data["initialization"]["H_FPS"]
        self.FPS = data["initialization"]["FPS"]

        self.colors = {
            "ceil": data["colors"]["ceil"],
            "snake": data["colors"]["snake"],
            "apple": data["colors"]["apple"]
        }

        self.ceil_size = data["settings"]["ceil_size"]
        self.ceil_border = data["settings"]["ceil_border"]
        self.field_size = (self.window_size[0] // self.ceil_size, self.window_size[1] // self.ceil_size)
        self.speed = (0, 0)

