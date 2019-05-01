from dataclasses import dataclass

from wired.dataclasses import factory


@factory()
@dataclass
class Greeter:
    name: str = 'Mary'

    def __call__(self, customer: str) -> str:
        msg = 'Hello {customer} my name is {name}'
        return msg.format(customer=customer, name=self.name)
