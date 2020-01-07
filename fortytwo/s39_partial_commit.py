"""39: Only Commit Some Changes

Unselect files or changed regions within files during the commit
process.

- Add a comment below under ``def main()``

    - Then edit this line in the docstring

- Commit

- De-select some files, remove chunks from some files

- Commit

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
