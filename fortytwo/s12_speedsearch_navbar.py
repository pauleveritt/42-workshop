"""12: Narrow Navigation Bar With Speed Search

Narrow and select from a long folder listing Navigation Bar by typing a speed search.

- Activate

- Press down

- Type ``s13``

- Type ``s42`` to see items out of view

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
