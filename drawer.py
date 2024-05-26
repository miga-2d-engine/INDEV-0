import wx
app_wx = wx.App()
import pygame as pg
pg.init()


def getTextWidth(text, point_size, font_to_width):
    dc = wx.ScreenDC()
    size = dc.GetTextExtent(text)
    return size[0] // 20 * point_size


def draw_menu(menu, click_position, click_type, app):
    for element in menu:
        if element["type"] == "text":
            draw_text(element, app)
        elif element["type"] == "image":
            draw_image(element, app)
        elif element["type"] == "button":
            draw_button(element, click_position, click_type, app)


def draw_text(element, app):
    screen = app.sc
    sc_size = app.sc_size

    value = element["value"]
    pos = element["pos"]
    size = element["size"]
    font_name = element["font"]
    color = element["color"]
    is_bold = element["is_bold"]
    is_italic = element["is_italic"]

    font = pg.font.SysFont(font_name, int(size * sc_size[1]), is_bold, is_italic)
    text_surface = font.render(value, False, color)
    screen.blit(text_surface,
                (pos[0] * sc_size[0] - getTextWidth(value, int(size * sc_size[1]), font_name) / 2, pos[1] * sc_size[1]
                 - size * sc_size[1] / 2))


def draw_image(element, app):
    screen = app.sc
    sc_size = app.sc_size

    img = element["img"]
    pos = element["pos"]
    size = element["size"]
    rotate = element["rotate"]

    if size[0] == "auto":
        width_image, height_image = img.get_rect().size
        img = pg.transform.scale(img, (width_image*size[1]*sc_size[1]/height_image, size[1]*sc_size[1]))
        screen.blit(img, (pos[0]*sc_size[0] - width_image*size[1]*sc_size[1]/height_image/2,
                          pos[1]*sc_size[1] - size[1]*sc_size[1]/2))
    elif size[1] == "auto":
        width_image, height_image = img.get_rect().size
        img = pg.transform.scale(img, (width_image*size[0]*sc_size[0]/height_image, size[0]*sc_size[0]))
        screen.blit(img, (pos[0]*sc_size[0] - width_image*size[0]*sc_size[0]/height_image/2,
                          pos[1]*sc_size[1] - size[0]*sc_size[0]/2))


def draw_button(element, mouse_position, click_type, app):
    screen = app.sc
    sc_size = app.sc_size

    value = element["value"]
    pos = element["pos"]
    size = element["size"]
    font_name = element["font"]
    color = element["color"]
    is_bold = element["is_bold"]
    is_italic = element["is_italic"]
    width = element["width"]
    height = element["height"]
    background = element["background"]
    background_hover = element["background_hover"]
    border = element["border"]
    color_border = element["color_border"]
    click = element["click_type"]
    do = element["do"]

    pg.draw.rect(screen, color_border, (pos[0] * sc_size[0] - width * sc_size[0] // 2 - border,
                                        pos[1] * sc_size[1] - height * sc_size[1] // 2 - border,
                                        width * sc_size[0] + border * 2,
                                        height * sc_size[1] + border * 2))
    if pos[0] * sc_size[0] - width * sc_size[0] / 2 <= mouse_position[0] \
            <= pos[0] * sc_size[0] + width * sc_size[0] / 2 and pos[1] * sc_size[1] - height * sc_size[1] / 2 \
            <= mouse_position[1] <= pos[1] * sc_size[1] + height * sc_size[1] / 2:
        pg.draw.rect(screen, background_hover, (pos[0] * sc_size[0] - width * sc_size[0] / 2,
                                                pos[1] * sc_size[1] - height * sc_size[1] / 2,
                                                width * sc_size[0],
                                                height * sc_size[1]))
        if click == click_type:
            do(app)
    else:
        pg.draw.rect(screen, background, (pos[0] * sc_size[0] - width * sc_size[0] / 2,
                                          pos[1] * sc_size[1] - height * sc_size[1] / 2,
                                          width * sc_size[0],
                                          height * sc_size[1]))
    font = pg.font.SysFont(font_name, int(size * sc_size[1]), is_bold, is_italic)
    text_surface = font.render(value, False, color)
    screen.blit(text_surface,
                (pos[0] * sc_size[0] - getTextWidth(value, int(size * sc_size[1]), font_name) / 2, pos[1] * sc_size[1]
                 - size * sc_size[1] / 2))
