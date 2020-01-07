"""27: Run From Keyboard

Use the keyboard to select and run a run configuration, without toolbar.

- Start by running once via gutter icon, to create run config

- Ctrl-R re-runs your *active* run-config

- Ctrl-Alt-R brings up a speed-typeable dialog

- More than just run, look in sub-menus for each

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App
from fortytwo.models import Greeter


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
