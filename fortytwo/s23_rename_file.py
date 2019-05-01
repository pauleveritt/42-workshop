"""23: Rename a File and Its References

Change your mind on a file name and the IDE makes all the changes
for you.

- Activate navbar, select ``models.py``

- Refactor -> Rename

- See the import below is changed, as is VCS

- Undo to put it back

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
