import os
import sublime_plugin

from ..menus_creator import MenusCreator


class OpenOtherFilesCommand(sublime_plugin.WindowCommand):
    def run(self, index):
        file = self.paths[index]
        self.window.open_file(file)


class MenusOpener(MenusCreator):
    command = "open_other_files"

    def __init__(self, caption="Open Other Files", enabled=True):
        self.caption = caption
        self.enabled = enabled

    def create(self, view, event):
        if self.enabled and os.path.exists(view.file_name() or ""):
            index, items, paths = 0, [], []
            branch, leaf = os.path.split(view.file_name())
            for file in sorted(os.listdir(branch)):
                path = os.path.join(branch, file)
                if os.path.isfile(path) and file != leaf:
                    items.append(self.item(file, {"index": index}))
                    paths.append(path)
                    index += 1
            if len(items):
                OpenOtherFilesCommand.paths = paths
                return self.fold_items(items)
        return None
