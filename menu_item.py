#usr/bin/env python3

class MenuItem:
    def __init__(self, _id, text, active=False, cmd=None):
        """
        MenuItem(int, str, bool, func)
        """
        self._id = _id
        self.text = text
        self.tag = text.lower().replace(" ", "")
        self.active = active
        self.cmd = cmd

