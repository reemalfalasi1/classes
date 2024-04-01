from exhibition import Exhibition
from Artifact import Artifact
from SpecialEvent import SpecialEvent
from typing import List

class LouvreMuseum:  #defining the LouvreMuseum class
    """class to represent the LouvreMuseum"""
    def __init__(self, museum_name: str, address: str, opening_hours: str):  #initializing the LouvreMuseum object with attributes
        self.__museum_name = museum_name  #assigning the museum name
        self.__address = address  #assigning the address
        self.__opening_hours = opening_hours  #assigning the opening hours
        self.__exhibitions = []  #initializing the exhibitions attribute as an empty list
        self.__artifacts = []  #initializing the artifacts attribute as an empty list
        self.__special_events = []  #initializing the special events attribute as an empty list

    # getters and setters
    def get_museum_name(self):
        return self.__museum_name

    def set_museum_name(self, museum_name: str):
        self.__museum_name = museum_name

    def get_address(self) :
        return self.__address

    def set_address(self, address: str):
        self.__address = address

    def get_opening_hours(self) :
        return self.__opening_hours

    def set_opening_hours(self, opening_hours: str):
        self.__opening_hours = opening_hours

    def get_exhibitions(self) -> List[Exhibition]:  #method to get the exhibitions attribute
        return self.__exhibitions

    def set_exhibitions(self, exhibitions: List[Exhibition]) -> None:  # Method to set the exhibitions attribute
        self.__exhibitions = exhibitions

    def add_exhibition(self, exhibition: Exhibition) -> None:  # Method to add an exhibition to the LouvreMuseum
        self.__exhibitions.append(exhibition)

    def remove_exhibition(self, exhibition: Exhibition) -> bool:  # Method to remove an exhibition from the LouvreMuseum
        if exhibition in self.__exhibitions:  # checking if the exhibition is on the list
            self.__exhibitions.remove(exhibition)  # removing the exhibition
            return True  # returning True indicating successful removal
        return False  # returning False indicating the exhibition was not found in the list

    def get_artifacts(self) -> List[Artifact]:  # a method to get the artifacts attribute
        return self.__artifacts

    def set_artifacts(self, artifacts: List[Artifact]) -> None:  # a method to set the artifacts attribute
        self.__artifacts = artifacts

    def add_artifact(self, artifact: Artifact) -> None:  # a method to add an artifact to the LouvreMuseum
        self.__artifacts.append(artifact)

    def remove_artifact(self, artifact: Artifact) -> bool:  # Method to remove an artifact from the louvreMuseum
        if artifact in self.__artifacts: #checking if the artifact is in the list
            self.__artifacts.remove(artifact)# removing the artifact
            return True  # Returning True indicating successful removal
        return False  # Returning False indicating the artifact was not found in the list

    def get_special_events(self) -> List[SpecialEvent]:  # Method to get the special events attribute
        return self.__special_events

    def set_special_events(self, special_events: List[SpecialEvent]) -> None:  # Method to set the special events attribute
        self.__special_events = special_events

    def add_special_event(self, special_event: SpecialEvent) -> None:  # Method to add a special event to the LouvreMuseum
        self.__special_events.append(special_event)

    def remove_special_event(self, special_event: SpecialEvent) -> bool:  # Method to remove a special event from the LouvreMuseum
        if special_event in self.__special_events:  # Checking if the special event is in the list
            self.__special_events.remove(special_event)  # Removing the special event
            return True  # Returning True indicating successful removal
        return False  # Returning False indicating the special event was not found in the list
# Creating instances
louvre = LouvreMuseum("Louvre Museum", "Paris, France", "9:00 AM - 6:00 PM")

# Adding exhibitions
exhibition1 = Exhibition(1, "Ancient Art", "2024-05-01", "2024-06-30", "Hall 1")
exhibition2 = Exhibition(2, "Modern Art", "2024-07-01", "2024-08-31", "Hall 2")
louvre.add_exhibition(exhibition1)
louvre.add_exhibition(exhibition2)

# Adding artifacts
artifact1 = Artifact(1, "Sculpture", "Ancient sculpture", "2000 years", "Greek", True)
artifact2 = Artifact(2, "Painting", "Modern painting", "20 years", "French", True)
louvre.add_artifact(artifact1)
louvre.add_artifact(artifact2)

# Adding special events with location provided
special_event1 = SpecialEvent(1, "2024-07-15", "123456", 50.0, "Concert", "2024-07-15", "Concert Hall")
special_event2 = SpecialEvent(2, "2024-08-10", "789012", 35.0, "Workshop", "2024-08-10", "Workshop Hall")
louvre.add_special_event(special_event1)
louvre.add_special_event(special_event2)
