import pygame as pg
pg.init()


def example_function_1(app):
    print("Это пример использования нажатия кнопки")
    app.scene = "example_button"


def example_function_2(app):
    print("Это пример использования нажатия кнопки")
    app.scene = "main"


main_menu = [
    {"type": "text",
     "value": "example text",
     "pos": (0.5, 0.3),
     "size": 0.1,
     "font": "timesnewromanpsmt.ttf",
     "color": (255, 255, 255),
     "is_bold": False,
     "is_italic": False},

    {"type": "button",
     "value": "example button",
     "pos": (0.5, 0.5),
     "size": 0.1,
     "font": "timesnewromanpsmt.ttf",
     "color": (255, 255, 255),
     "is_bold": False,
     "is_italic": False,
     "width": 0.5,
     "height": 0.2,
     "background": (0, 0, 0),
     "background_hover": (64, 64, 64),
     "border": 5,
     "color_border": (255, 255, 255),
     "click_type": 1,
     "do": example_function_1},  # Функция без скобок

    {"type": "image",
     "img": pg.image.load("example.jpg"),
     "pos": (0.5, 0.8),
     "size": (0.15, "auto"),  # Размер по сравнению с высотой окна
     "rotate": 0},  # В градусах по часовой стрелке
]
end_credits = []
button_example = [{"type": "button",
                   "value": "example button 2  ",
                   "pos": (0.5, 0.5),
                   "size": 0.1,
                   "font": "timesnewromanpsmt.ttf",
                   "color": (255, 255, 255),
                   "is_bold": False,
                   "is_italic": False,
                   "width": 0.5,
                   "height": 0.2,
                   "background": (0, 0, 0),
                   "background_hover": (64, 64, 64),
                   "border": 5,
                   "color_border": (255, 255, 255),
                   "click_type": 1,
                   "do": example_function_2}]

# НАПОМИНАНИЕ: в этом файле координаты указываются при помощи процентов
