from datetime import date
from typing import List


class Exhibition:
    def __init__(self, exhibition_id: int, name: str, start_date: date, end_date: date, location: str):
        self.__exhibition_id = exhibition_id
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__location = location
        self.__artworks = []  # Initialized as empty list

    # getters and setters...
    def get_exhibition_id(self) -> int:
        return self.__exhibition_id

    def set_exhibition_id(self, exhibition_id: int) -> None:
        self.__exhibition_id = exhibition_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_start_date(self) -> date:
        return self.__start_date

    def set_start_date(self, start_date: date) -> None:
        self.__start_date = start_date

    def get_end_date(self) -> date:
        return self.__end_date

    def set_end_date(self, end_date: date) -> None:
        self.__end_date = end_date

    def get_location(self) -> str:
        return self.__location

    def set_location(self, location: str) -> None:
        self.__location = location

    def get_artworks(self) -> List[Artwork]:
        return self.__artworks

    def set_artworks(self, artworks: List[Artwork]) -> None:
        self.__artworks = artworks

    def add_artwork(self, artwork: Artwork) -> None:
        self.__artworks.append(artwork)

    def remove_artwork(self, artwork: Artwork) -> bool:
        if artwork in self.__artworks:
            self.__artworks.remove(artwork)
            return True
        return False
