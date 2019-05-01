"""37: Reword Commit Message

Change the wording in your last commit message, after you
committed.

- When you haven't pushed yet

- Do a commit with a typo

- Version Control | Log, right-click on commit, choose
  ``Reword``

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
