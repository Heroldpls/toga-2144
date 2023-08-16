from pathlib import Path

import pytest

from toga_gtk.keys import gtk_accel, toga_key
from toga_gtk.libs import Gdk, Gtk

from .probe import BaseProbe


class AppProbe(BaseProbe):
    def __init__(self, app):
        super().__init__()
        self.app = app
        assert isinstance(self.app._impl.native, Gtk.Application)

    @property
    def config_path(self):
        return Path.home() / ".config" / "testbed"

    @property
    def data_path(self):
        return Path.home() / ".local" / "share" / "testbed"

    @property
    def cache_path(self):
        return Path.home() / ".cache" / "testbed"

    @property
    def logs_path(self):
        return Path.home() / ".local" / "state" / "testbed" / "log"

    @property
    def is_cursor_visible(self):
        pytest.skip("Cursor visibility not implemented on GTK")

    def is_full_screen(self, window):
        return bool(
            window._impl.native.get_window().get_state() & Gdk.WindowState.FULLSCREEN
        )

    def content_size(self, window):
        content_allocation = window._impl.container.get_allocation()
        return (content_allocation.width, content_allocation.height)

    def _menu_item(self, path):
        main_menu = self.app._impl.native.get_menubar()
        menu = main_menu
        orig_path = path.copy()
        try:
            while True:
                label, path = path[0], path[1:]
                items = {}
                for index in range(menu.get_n_items()):
                    section = menu.get_item_link(index, "section")
                    if section:
                        for section_index in range(section.get_n_items()):
                            items[
                                section.get_item_attribute_value(
                                    section_index, "label"
                                ).get_string()
                            ] = (section, section_index)
                    else:
                        items[
                            menu.get_item_attribute_value(index, "label").get_string()
                        ] = (menu, index)

                if label == "*":
                    item = items[self.app.name]
                else:
                    item = items[label]

                menu = item[0].get_item_link(item[1], "submenu")
        except IndexError:
            pass
        except AttributeError:
            raise AssertionError(f"Menu {' > '.join(orig_path)} not found")

        action_name = item[0].get_item_attribute_value(item[1], "action").get_string()
        cmd_id = action_name.split(".")[1]
        action = self.app._impl.native.lookup_action(cmd_id)
        return action

    def _activate_menu_item(self, path):
        item = self._menu_item(path)
        item.emit("activate", None)

    def activate_menu_exit(self):
        self._activate_menu_item(["*", "Quit Toga Testbed"])

    def activate_menu_about(self):
        self._activate_menu_item(["Help", "About Toga Testbed"])

    def close_about_dialog(self):
        self.app._impl.native_about_dialog.close()

    def activate_menu_visit_homepage(self):
        self._activate_menu_item(["Help", "Visit homepage"])

    def assert_system_menus(self):
        self.assert_menu_item(["*", "Preferences"], enabled=False)
        self.assert_menu_item(["*", "Quit Toga Testbed"], enabled=True)

        self.assert_menu_item(["Help", "About Toga Testbed"], enabled=True)
        self.assert_menu_item(["Help", "Visit homepage"], enabled=True)

    def activate_menu_close_window(self):
        pytest.xfail("GTK doesn't have a window management menu items")

    def activate_menu_close_all_windows(self):
        pytest.xfail("GTK doesn't have a window management menu items")

    def activate_menu_minimize(self):
        pytest.xfail("GTK doesn't have a window management menu items")

    def assert_menu_item(self, path, enabled):
        item = self._menu_item(path)
        assert item.get_enabled() == enabled

    def keystroke(self, combination):
        accel = gtk_accel(combination)

        return toga_key(accel)
