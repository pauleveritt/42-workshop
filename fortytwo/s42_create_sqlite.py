"""42: Create SQLite Database Connection By Drag-and-Drop

Drag-and-drop a .sqlite database file onto the Database tool to
create a connection.

- Open ``Database`` tool window

- Drag-and-drop ``sample_db.sqlite`` from root

- Expand schema

- Browse table

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
