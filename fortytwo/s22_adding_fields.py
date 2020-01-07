"""22: Adding Fields In a Constructor

Let your IDE add constructor arguments to your instance.

- Type an argument to ``__init__``

    - Wrong: manually add ``name`` and ``self.name = name``

- Alt-Enter to make it a field

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App, Greeter


class Customer:
    # Pass in ``name``, store as ``self.first_name``
    def __init__(self):
        pass


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
