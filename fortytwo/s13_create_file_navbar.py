"""13: Create New File With Navigation Bar

Activate the Navigation Bar and create a new file somewhere in the project tree.

- Activate, navigate to where you want to go, Cmd-N

- Current directory is easy: activate, down, Cmd-N

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
