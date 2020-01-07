"""38: Undo Last Commit

Easily and visually recover from a commit-in-error.

- VCS -> Log -> Select an un-pushed commit

- ``Undo Commit``, into the ``Default Changelist``

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
