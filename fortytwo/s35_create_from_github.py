"""35: Create a Project from GitHub

Let PyCharm do the work to clone and setup a project hosted on GitHub.

- Via ``VCS | Checkout from Version Control | Git``

- Or via Find Action ``ch ve``

- Speed search for ``wired``

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
