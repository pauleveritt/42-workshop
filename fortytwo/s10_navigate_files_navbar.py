"""10: Navigate Files With Navigation Bar

Move around your project tree and select files, from your keyboard, with the Navigation Bar.

- Left, down, up

- E.g. go to s09

- Current directory doesn't need initial left

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
