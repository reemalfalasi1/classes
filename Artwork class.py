class Artwork:
    def __init__(self, artwork_id: int, title: str, artist: str, year_of_creation: int, is_featured: bool):
        self.__artwork_id = artwork_id
        self.__title = title
        self.__artist = artist
        self.__year_of_creation = year_of_creation
        self.__is_featured = is_featured

    # getters and setters...
    def get_artwork_id(self) -> int:
        return self.__artwork_id

    def set_artwork_id(self, artwork_id: int) -> None:
        self.__artwork_id = artwork_id

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        self.__title = title

    def get_artist(self) -> str:
        return self.__artist

    def set_artist(self, artist: str) -> None:
        self.__artist = artist

    def get_year_of_creation(self) -> int:
        return self.__year_of_creation

    def set_year_of_creation(self, year_of_creation: int) -> None:
        self.__year_of_creation = year_of_creation

    def get_is_featured(self) -> bool:
        return self.__is_featured

    def set_is_featured(self, is_featured: bool) -> None:
        self.__is_featured = is_featured
