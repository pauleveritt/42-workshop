"""08: Navigate Cursor Position Back and Forth

Easily navigate back to where you were, or where you went.

- Cmd-B on `App`, then `ServiceRegistry`

- Use left/right brackets to return/descend

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
