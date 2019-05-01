import venusian
from wired import ServiceRegistry

from fortytwo import models
from fortytwo.models import Greeter

__all__ = [
    'App',
    'Greeter'
]


class App:
    def __init__(self):
        self.registry = ServiceRegistry()
        scanner = venusian.Scanner(registry=self.registry)
        scanner.scan(models)

    def __enter__(self):
        self.container = self.registry.create_container()
        return self.container

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.container:
            del self.container
