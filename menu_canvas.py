#!usr/bin/env python3

from tkinter import Canvas, LEFT
from gui_settings import *

class MenuCanvas(Canvas):
    """
    Draw validatable buttons on canvas
    """
    def __init__(self, parent, menu_items, active):
        Canvas.__init__(
            self,
            parent,
            width=CAN_W,
            height=CAN_H,
            bg=GUI_COLORS["background"]
        )
        self.parent = parent
        self.items = menu_items
        self.active = active
        self.drawMenu()

    def drawMenu(self):
        y = 0
        for item in self.items:
            self.create_text(
                MENU_BT_PADX,
                y * MENU_BT_PADY + MENU_BT_PADY,
                fill=MENU_ITEM_COLORS[item.active],
                text=item.text,
                justify=LEFT,
                tag="item"
            )
            y += 1

    def toggleState(self, item):
        item.active = not item.active
        self.delete("item")
        self.drawMenu()
        
    def navigateUp(self):
        """
        Activate upper item when up key is pressed
        """
        for i in range(len(self.items)):
            if self.items[i].active:
                if i == 0:
                    self.toggleState(self.items[i])
                    self.toggleState(self.items[-1])
                else:
                    self.toggleState(self.items[i])
                    self.toggleState(self.items[i - 1])
            else:
                pass

    def navigateDown(self):
        """
        Activate lower item when down key is pressed
        """
        for i in range(len(self.items)):
            if self.items[i].active:
                if self.items[i] == self.items[-1]:
                    self.toggleState(self.items[i])
                    self.toggleState(self.items[0])
                else:
                    self.toggleState(self.items[i])
                    self.toggleState(self.items[i + 1])
            else:
                pass
        
