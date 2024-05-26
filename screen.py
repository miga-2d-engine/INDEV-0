import pygame as pg
import info
import menu
import drawer
pg.init()


class create:
    def __init__(self, user_display=(960, 540), screen_name=f"{info.PROJECT_NAME} {info.VERSION}",
                 icon_path=None, max_fps=60):
        # Создание окна
        self.sc = pg.display.set_mode(user_display, pg.RESIZABLE)
        pg.display.set_caption(screen_name)
        if icon_path is not None:
            pg.display.set_icon(icon_path)

        # Прочая информация
        self.scene = "main"
        self.is_paused = False
        self.screen_pos = [0, 0]
        self.sc_size = pg.display.get_surface().get_size()
        self.clock = pg.time.Clock()
        self.max_fps = max_fps

    def loop(self, app):
        is_opened = True
        mouse_position = (-1, -1)
        while is_opened:
            click_type = 0
            self.sc_size = pg.display.get_surface().get_size()  # Фиксирование размеров окна

            # Закрытие и обновление экрана
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    is_opened = False
                elif event.type == pg.MOUSEBUTTONUP:
                    click_type = event.dict["button"]
                elif event.type == pg.MOUSEMOTION:
                    mouse_position = event.dict["pos"]

            # Отрисовка страниц
            self.sc.fill((0, 0, 0))
            self.draw_pages(mouse_position, click_type, app)

            pg.display.update()
            self.clock.tick(self.max_fps)

    def draw_pages(self, mouse_position, click_type, app):
        if self.scene == "main":
            data = menu.main_menu
            drawer.draw_menu(data, mouse_position, click_type, app)
        elif self.scene == "example_button":
            data = menu.button_example
            drawer.draw_menu(data, mouse_position, click_type, app)
