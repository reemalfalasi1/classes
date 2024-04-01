class Artifact:
    def __init__(self, artifact_id: int, name: str, description: str, age: str, culture: str, is_on_display: bool):
        self.__artifact_id = artifact_id
        self.__name = name
        self.__description = description
        self.__age = age
        self.__culture = culture
        self.__is_on_display = is_on_display

    # getters and setters...
    def get_artifact_id(self):
        return self.__artifact_id

    def set_artifact_id(self, artifact_id: int):
        self.__artifact_id = artifact_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str) -> None:
        self.__description = description

    def get_age(self) -> str:
        return self.__age

    def set_age(self, age: str) -> None:
        self.__age = age

    def get_culture(self) -> str:
        return self.__culture

    def set_culture(self, culture: str) -> None:
        self.__culture = culture

    def get_is_on_display(self) -> bool:
        return self.__is_on_display

    def set_is_on_display(self, is_on_display: bool) -> None:
        self.__is_on_display = is_on_display
