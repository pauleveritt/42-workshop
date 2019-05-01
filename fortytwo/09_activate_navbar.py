"""09: Activate Navigation Bar

Bring up the Navigation Bar as needed, let it disappear when finished.

- What I *do* need to browse files?

- Jump to Navigation Bar (Alt-Home Win/Linux, Cmd-Up macOS)

- Hit ``Esc`` to dismiss

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
