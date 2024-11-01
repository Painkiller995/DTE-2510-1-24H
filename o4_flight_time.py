"""
This module represents a flight time implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

from datetime import datetime


class Flight:
    """
    A class representing a flight information.
    """

    def __init__(
        self,
        flight_number: str,
        departure_time: datetime,
        arrival_time: datetime,
    ):
        self._flight_number = flight_number
        self._departure_time = departure_time
        self._arrival_time = arrival_time

    @property
    def flight_number(self) -> str:
        """
        Property returning the flight number.
        """
        return self._flight_number

    @flight_number.setter
    def flight_number(self, value: str) -> None:
        """
        Set the flight number.
        """
        self._flight_number = value

    @property
    def departure_time(self) -> datetime:
        """
        Property returning the departure time.
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value: datetime):
        """
        Set the departure time.
        """
        self._departure_time = value

    @property
    def arrival_time(self) -> datetime:
        """
        Property returning the arrival time.
        """
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, value: datetime):
        """
        Set the arrival time.
        """
        self._arrival_time = value

    def get_flight_time(self) -> float:
        """
        Calculate the flight time in minutes.
        Args:
            time_zone: The time zone of the flight.

        Returns:
            The flight time in minutes.
        """
        flight_time = self.arrival_time - self.departure_time
        return flight_time.seconds / 60


class Itinerary:
    """
    A class representing an itinerary.
    """

    def __init__(self, flights: list[Flight]):
        self._flights = sorted(flights, key=lambda flight: flight.departure_time)

    @property
    def flights(self) -> list[Flight]:
        """
        Property returning the flights.
        """
        return self._flights

    @flights.setter
    def flights(self, value: list[Flight]) -> None:
        """
        Set the flights and sort them by departure time.
        """
        self._flights = sorted(value, key=lambda flight: flight.departure_time)

    def get_total_flight_time(self) -> float:
        """
        Calculate the total flight time in minutes.
        Returns:
            The total flight time in minutes.
        """
        return sum(flight.get_flight_time() for flight in self.flights)

    def get_total_travel_time(self) -> float:
        """
        Calculate the total travel time in minutes.
        Returns:
            The total travel time in minutes.
        """
        if not self.flights:
            return 0
        start_time = self.flights[0].departure_time
        end_time = self.flights[-1].arrival_time
        return (end_time - start_time).total_seconds() / 60


if __name__ == "__main__":
    flights: list[Flight] = []

    flights.append(
        Flight("US230", datetime(2014, 4, 5, 5, 5, 0), datetime(2014, 4, 5, 6, 15, 0))
    )

    flights.append(
        Flight("US235", datetime(2014, 4, 5, 6, 55, 0), datetime(2014, 4, 5, 7, 45, 0))
    )

    flights.append(
        Flight("US237", datetime(2014, 4, 5, 9, 35, 0), datetime(2014, 4, 5, 12, 55, 0))
    )

    itinerary = Itinerary(flights)

    for flight in itinerary.flights:
        print(
            f"Flight: {flight.flight_number}",
            f"Departure: {flight.departure_time}",
            f"Arrival: {flight.arrival_time}",
            f"Flight time: {flight.get_flight_time()} minutes",
            "----------------------------------",
            sep="\n",
        )

    print(itinerary.get_total_travel_time())
    print(itinerary.get_total_flight_time())
