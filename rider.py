"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
WAITING: A constant used for the waiting rider status.
CANCELLED: A constant used for the cancelled rider status.
SATISFIED: A constant used for the satisfied rider status
"""
from __future__ import annotations
from location import Location

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:

    """A rider for a ride-sharing service.

    === Attributes ===
    id: the name of the rider.
    patience: the patience of a rider.
    origin: the rider's start location.
    destination: where the rider wants to go.
    status: the status of the rider.
    """

    id: str
    patience: int
    origin: Location
    destination: Location
    status: str

    def __init__(self, identifier: str, patience: int, origin: Location,
                 destination: Location) -> None:
        """Initialize a Rider.

        """
        self.id = identifier
        self.patience = patience
        self.origin = origin
        self.destination = destination
        self.status = WAITING

    def __str__(self) -> str:
        """Return a string representation.

        """
        return f'({self.id}, {self.origin}, {self.destination})'

    def __eq__(self, other: Rider) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        return self.id == other.id


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['location']})
