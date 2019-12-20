import webbrowser
import sublime_plugin

from ..menus_creator import MenusCreator


class SearchOnlineCommand(sublime_plugin.WindowCommand):
    platforms = {}

    def run(self, platform):
        api = self.platforms[platform]
        webbrowser.open_new_tab(api % self.content)


class MenusSearcher(MenusCreator):
    command = "search_online"

    def __init__(self, caption="Search Online", enabled=True, platforms={}):
        self.caption = caption
        self.enabled = enabled
        SearchOnlineCommand.platforms = platforms

    def get_selected(self, view, event):
        pt = view.window_to_text((event["x"], event["y"]))
        selected = view.sel()
        if view.has_non_empty_selection_region():
            selection = selected[0]
            if not selection.empty() and selection.contains(pt):
                content = view.substr(selected[0]).strip()
                if content:
                    return content
        return None

    def create(self, view, event):
        platforms = sorted(SearchOnlineCommand.platforms)

        if self.enabled and len(platforms) > 0:
            content = self.get_selected(view, event)

            if content is not None:
                SearchOnlineCommand.content = content

                if len(platforms) == 1:
                    caption = "Search With " + platforms[0]
                    return self.item(caption, {"platform": platforms[0]})
                else:
                    items = [self.item(p, {"platform": p}) for p in platforms]
                    return self.fold_items(items)

            return None
