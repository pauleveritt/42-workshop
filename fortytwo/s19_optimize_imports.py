"""19: Optimize Imports

Automate the organizing and cleaning up of your Python imports with Optimize Imports.

- Problems:

    - One unused import

    - Unsorted import list, per group

    - I want multiple per line

- Optimize Imports (``Ctrl-Alt-O`` Win/Linux/macOS)

- Undo/Redo

- Split imports  via
  ``Preferences | Editor | Code Style | Python | Imports``

  - ``Structure of "from" imports`` -> ``Always split imports``

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

import os
from time import time
from sys import version
from fortytwo import App, Greeter


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
    print(version)
    print(time())
