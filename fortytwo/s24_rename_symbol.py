"""24: Rename Symbol

Change a variable name, class name, or other symbol, across the
project.

- ``Greeter`` is used in many places, but we want to change to
  ``Welcomer``

- Navigate to Symbol with Cmd-B

- Ctrl-T | Rename -> ``Welcomer``

- Left-bracket back to code

- **** UNDO **** puts ``Greeter`` back everywhere

- Could also rename from here

- Works on *symbols* not strings

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
