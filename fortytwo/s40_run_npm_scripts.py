"""40: Run npm Scripts from package.json

Browse your package.json scripts and run in a dedicated tool
window.

- Right-click on ``package.json`` and select ``Show npm scripts``

- Close that panel, re-do from ``Recent Files``

- Find Action | ``run ser``

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
