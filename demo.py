#!usr∕bin∕env python3

import tkinter as tk
import tkinter.font as tkf
from settings import *
from menu_canvas import MenuCanvas

class Demo(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, X, Y))
        self.title("tk-tree-menus demo app")


    def play(self):
        pass

    def option1(self):
        pass

    def option2(self):
        pass
        
    def initMenu(self):
        self.menu_tree = MenuTree({
            "root": {
                "play": MenuNode(
                    _id     = 1,
                    parent  = "root",
                    active  = True,
                    text    = "Play",
                    command = self.play,
                ),
                "options": MenuNode(
                    _id      = 2,
                    parent   = "root",
                    text     = "Options",
                    children = {
                        "option1": MenuNode(
                            _id     = 21,
                            parent  = "options",
                            text    = "Switch colors",
                            command = self.switchColors
                        ),
                        "option2": MenuNode(
                            _id     = 22
                            parent  = "options",
                            text    = "Increase text size",
                            command = self.increaseTextSize
                        ),
                        "option3": MenuNode(
                            _id     = 23
                            parent  = "options",
                            text    = "Decrease text size",
                            command = self.decreaseTextSize
                        )
                    }
                ),
                "quit": MenuNode(
                    _id    = 3
                    parent = "root",
                    text   = "Quit",
                    cmd    = self.quit
                )
                
            }
        })
