"""32: Auto-Run Tests

Get into testing mode by telling PyCharm to automatically
re-run tests as you type.

- Click the auto-test button and click Play

- Change ``test_32`` that causes failure

- Fix, don't save...still runs

- Configurable delay

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
