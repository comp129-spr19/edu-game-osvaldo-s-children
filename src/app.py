from kitchen import (
    Kitchen
)

from pygame import (
    # imported constants
    HWSURFACE,
    K_ESCAPE,
    QUIT,

    display,
    event,
    init,
    key,
    quit
)

import sprite_cluster as sc


class App:

    # internal constants
    __WINDOW_WIDTH__ = 800
    __WINDOW_HEIGHT__ = 800

    def __init__(self):
        self._running = True
        self._display_surf = None

        # initialize sprite cluster
        sc.__init__()

    def on_init(self):
        init()
        self._display_surf = display.set_mode(
            (self.__WINDOW_WIDTH__, self.__WINDOW_HEIGHT__), HWSURFACE)

        # initialize class variables
        self.kitchen = Kitchen()
        self.kitchen.on_init()

        sc.on_init()

        self._running = True

    def on_event(self, keys):
        if keys[K_ESCAPE]:
            self._running = False
        else:
            self.kitchen.on_event(keys)
            sc.on_event(keys)

    def on_loop(self):
        self.kitchen.on_loop()
        sc.on_loop()

    def on_render(self):
        # TODO: should kitchen only render once?
        self.kitchen.on_render(self._display_surf)
        sc.on_render(self._display_surf)

        # update display to register all changes
        display.flip()

    def on_cleanup(self):
        quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while (self._running):
            event.pump()
            keys = key.get_pressed()

            self.on_event(keys)
            self.on_loop()
            self.on_render()

        self.on_cleanup()
