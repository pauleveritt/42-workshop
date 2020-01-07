"""33: Spot Coverage Gaps Using the Gutter

Let the IDE help you spot coverage gaps in your testing. *Note: Requires
PyCharm Professional.*

- Run tests, but under coverage

- Spot the coverage gap in ``def foo``

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App
from fortytwo.models import Greeter


def foo():
    x = 1
    return x


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
