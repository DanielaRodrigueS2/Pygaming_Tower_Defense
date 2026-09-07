import pygame as pg

class Game:
    def __init__(self):

        pg.init()

        self.width = 1200
        self.height = 800

        self.screen = pg.display.set_mode((self.width, self.height))

        self.clock = pg.Clock()
        self.running = True

        self.current_screen = None

    def change_current_screen(self, screen):
        self.current_screen = screen

    def run(self):

        while self.running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                self.current_screen.handle_events(event)

            self.current_screen.update()

            self.current_screen.draw(self.screen)

            pg.display.flip()
            self.clock.tick(60)

        pg.quit()
