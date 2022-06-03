from guizero import App, Box, Text, Waffle, PushButton, Slider, TextBox, Picture
from PIL import Image

import system


def go():
    name = "Case Controller"
    app = App(name)
    SCREEN_REZ = system.config_2_dict()
    app.width = SCREEN_REZ['REZ'][0]
    app.height = SCREEN_REZ['REZ'][1]
    boxTitle = Box(app, width='fill')
    boxTitle.border = True
    title = Text(boxTitle, text=f"{name}",)
    path = system.list_2_path(['Panda_Roux.gif'])[0]
    animatedLogo = Picture(boxTitle, path)
   

    app.display()



