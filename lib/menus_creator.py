

class MenusCreator(object):
    def item(self, caption, args):
        return {"caption": caption, "command": self.command, "args": args}

    def fold_items(self, items):
        return {"caption": self.caption, "children": items}
