from datetime import date#importing the 'date' class from the 'datetime' module
from typing import List  #importing the 'List' type from the 'typing' module
class Artwork:
    """class to represent an Artwork"""
    def __init__(self, artwork_id: int, title: str, artist: str, year_of_creation: int, is_featured: bool):
        # Constructor initializing the Artwork object with attributes
        self.__artwork_id = artwork_id  # The artwork id
        self.__title = title  # The title of the artwork
        self.__artist = artist  # The artist of the artwork
        self.__year_of_creation = year_of_creation  # The year of creation of the artwork
        self.__is_featured = is_featured  # If the artwork is featured in the museum or not

    # Getters and setters
    def get_artwork_id(self):
        return self.__artwork_id

    def set_artwork_id(self, artwork_id: int):
        self.__artwork_id = artwork_id

    def get_title(self):
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def get_artist(self):
        return self.__artist

    def set_artist(self, artist: str):
        self.__artist = artist

    def get_year_of_creation(self):
        return self.__year_of_creation

    def set_year_of_creation(self, year_of_creation: int):
        self.__year_of_creation = year_of_creation

    def get_is_featured(self):
        return self.__is_featured

    def set_is_featured(self, is_featured: bool):
        self.__is_featured = is_featured

# Creating an instance of the Artwork class
artwork = Artwork(
    artwork_id=1,
    title="Starry Night",
    artist="Vincent van Gogh",
    year_of_creation=1889,
    is_featured=True
)

class Exhibition:  #defining the Exhibition class
    """class to represent an Exhibition"""
    def __init__(self, exhibition_id: int, name: str, start_date: date, end_date: date, location: str):  #Initializing the Exhibition object with attributes
        self.__exhibition_id = exhibition_id  #assigning the exhibition ID
        self.__name = name  #assigning the name of the exhibition
        self.__start_date = start_date  # assigning the start date attribute if the exhibition
        self.__end_date = end_date  #assigning the end date of the exhibition
        self.__location = location  #assigning the location of the exhibition
        self.__artworks = []  #initializing the artworks attribute as an empty list

    #getters and setters

    def get_exhibition_id(self) :
        return self.__exhibition_id

    def set_exhibition_id(self, exhibition_id: int):
        self.__exhibition_id = exhibition_id

    def get_name(self) :
        return self.__name

    def set_name(self, name: str) :
        self.__name = name

    def get_start_date(self) :
        return self.__start_date

    def set_start_date(self, start_date: date) :
        self.__start_date = start_date

    def get_end_date(self) :
        return self.__end_date

    def set_end_date(self, end_date: date) :
        self.__end_date = end_date

    def get_location(self):
        return self.__location

    def set_location(self, location: str):
        self.__location = location

    def get_artworks(self) -> List[Artwork]:#a method to get the artworks attribute
        return self.__artworks

    def set_artworks(self, artworks: List[Artwork]):# method to set the artworks attribute
        self.__artworks = artworks

    def add_artwork(self, artwork: Artwork):  #method to add an artwork to the exhibition
        self.__artworks.append(artwork)

    def remove_artwork(self, artwork: Artwork) -> bool:  # method to remove an artwork from the exhibition
        if artwork in self.__artworks:  #check if the artwork is in the list
            self.__artworks.remove(artwork)  # removing the artwork
            return True  # returning True indicating successful removal
        return False  # returning False indicating the artwork was not found in the list
# Creating an instance of the Exhibition class
exhibition = Exhibition(
    exhibition_id=1,
    name="Modern Art Gallery",
    start_date=date(2024, 4, 1),
    end_date=date(2024, 6, 30),
    location="Gallery 3"
)

# Printing the details of the exhibition instance
print("Exhibition Details:")
print("Exhibition ID:", exhibition.get_exhibition_id())
print("Name:", exhibition.get_name())
print("Start Date:", exhibition.get_start_date())
print("End Date:", exhibition.get_end_date())
print("Location:", exhibition.get_location())