"""14: Find In Path With Navigation Bar

Use keyboard and Navigation Bar to find files under a path.

- Activate, up, Shift-Cmd-F

- Type ``Mary``

- Other things you can do, e.g. refactor copy current file

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App, Greeter


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
