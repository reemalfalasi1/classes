class LouvreMuseum:
    def __init__(self, museum_name: str, address: str, opening_hours: str):
        self.__museum_name = museum_name
        self.__address = address
        self.__opening_hours = opening_hours
        self.__exhibitions = []  # Initialized as empty list
        self.__artifacts = []  # Initialized as empty list
        self.__special_events = []  # Initialized as empty list

    # getters and setters...
    def get_museum_name(self) -> str:
        return self.__museum_name

    def set_museum_name(self, museum_name: str) -> None:
        self.__museum_name = museum_name

    def get_address(self) -> str:
        return self.__address

    def set_address(self, address: str) -> None:
        self.__address = address

    def get_opening_hours(self) -> str:
        return self.__opening_hours

    def set_opening_hours(self, opening_hours: str) -> None:
        self.__opening_hours = opening_hours

    def get_exhibitions(self) -> List[Exhibition]:
        return self.__exhibitions

    def set_exhibitions(self, exhibitions: List[Exhibition]) -> None:
        self.__exhibitions = exhibitions

    def add_exhibition(self, exhibition: Exhibition) -> None:
        self.__exhibitions.append(exhibition)

    def remove_exhibition(self, exhibition: Exhibition) -> bool:
        if exhibition in self.__exhibitions:
            self.__exhibitions.remove(exhibition)
            return True
        return False

    def get_artifacts(self) -> List[Artifact]:
        return self.__artifacts

    def set_artifacts(self, artifacts: List[Artifact]) -> None:
        self.__artifacts = artifacts

    def add_artifact(self, artifact: Artifact) -> None:
        self.__artifacts.append(artifact)

    def remove_artifact(self, artifact: Artifact) -> bool:
        if artifact in self.__artifacts:
            self.__artifacts.remove(artifact)
            return True
        return False

    def get_special_events(self) -> List[SpecialEvent]:
        return self.__special_events

    def set_special_events(self, special_events: List[SpecialEvent]) -> None:
        self.__special_events = special_events

    def add_special_event(self, special_event: SpecialEvent) -> None:
        self.__special_events.append(special_event)

    def remove_special_event(self, special_event: SpecialEvent) -> bool:
        if special_event in self.__special_events:
            self.__special_events.remove(special_event)
            return True
        return False
