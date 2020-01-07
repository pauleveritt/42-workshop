"""34: Use Local History to Avoid Disaster

Use the IDE's built-in history facility to recover changes when VCS can't help you.

- Prep: Un-split All, close the Coverage suite

- Delete all of ``main` `, use Show History to restore

- Delete ``models.py``, use Show History to restore

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
