#!usr/bin/env python3

class MenuNode:
    def __init__(
            self, _id, parent=None, active=False,
            text=None, command=None, children=None):
        """
        MenuNode(
        """
        self.parent   = parent
        self.active   = active
        self.text     = text
        self._id      = _id
        self.command  = command
        self.children = children

    def hasParent(self):
        return not (not self.parent)

    def hasChildren(self):
        return not (not self.children)


class MenuTree:
    def __init__(self, d):
        """
        A MenuTree is instanciated with a dictionnary
        
        root = Node(
          parent = None,
          text   = None,
          _id = 0,
          
        ):
            
        m = MenuTree({
            "root": {
                "play": MenuNode(
                    "root", "Play", 0, self.play
                    ),
                "options": MenuNode(
                    "root", "Options", 1, self.options 
                    ),
                "quit": MenuNode(
                    "root", "Quit", 2, 
                    )
            } 
        })
        """
        self.root = d["root"]
        for k, v in d.items():
            pass
