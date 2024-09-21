import pygame as pyg
pyg.init()
screen=pyg.display.set_mode([640,480])
screen.fill([255,255,255])
running=True
while running:
    for event in pyg.event.get():
        if event.type==pyg.QUIT:
            running=False
pyg.quit()