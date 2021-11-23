"""Dispatcher for the simulation"""

from typing import Optional, List
from driver import Driver
from rider import Rider, CANCELLED


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.

    === Attributes ===
    waiting_list: A list of riders who don't have a driver that can be assigned
    r_drivers: The registered drivers for riders.
    """

    waiting_list: List[Rider]
    r_drivers: List[Driver]

    def __init__(self) -> None:
        """Initialize a Dispatcher.

        """
        self.waiting_list = []
        self.r_drivers = []

    def __str__(self) -> str:
        """Return a string representation.

        """
        return f'Waiting List:{self.waiting_list} ' \
               f'and Registered Drivers:{self.r_drivers}'

    def request_driver(self, rider: Rider) -> Optional[Driver]:
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        """
        flag = True
        for x in self.r_drivers:
            if x.is_idle:
                flag = False
        if flag:
            if rider not in self.waiting_list:
                self.waiting_list.append(rider)
            return None
        fastest_time = float('inf')
        fastest_driver = None
        for x in self.r_drivers:
            curr_time = x.get_travel_time(rider.origin)
            if x.is_idle:
                if curr_time <= fastest_time:
                    fastest_time = curr_time
                    fastest_driver = x
        return fastest_driver

    def request_rider(self, driver: Driver) -> Optional[Rider]:
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        """
        if driver not in self.r_drivers:
            self.r_drivers.append(driver)
        if self.waiting_list:
            rider = self.waiting_list.pop(0)
            return rider
        return None

    def cancel_ride(self, rider: Rider) -> None:
        """Cancel the ride for rider.

        """
        if rider in self.waiting_list:
            self.waiting_list.remove(rider)
        rider.status = CANCELLED

    def remove_rider(self, rider: Rider) -> None:
        """Remove rider once he is dropped off.

        """
        if rider in self.waiting_list:
            self.waiting_list.remove(rider)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing', 'driver', 'rider']})
