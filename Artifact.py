from datetime import date

class Artifact:
    """class to represent artifact"""
    def __init__(self, artifact_id: int, name: str, description: str, age: str, culture: str, is_on_display: bool):#initializing the Artifact object with attributes
        self.__artifact_id = artifact_id #assigning the artifat's id
        self.__name = name #the name of the artifact
        self.__description = description #the description of the artifact
        self.__age = age #the age of the artifact
        self.__culture = culture #the culture of the artifact (where it came from)
        self.__is_on_display = is_on_display #if the artifact is currently on display in the museum or not

    # getters and setters
    def get_artifact_id(self):
        return self.__artifact_id

    def set_artifact_id(self, artifact_id: int):
        self.__artifact_id = artifact_id

    def get_name(self) :
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_description(self) :
        return self.__description

    def set_description(self, description: str) :
        self.__description = description

    def get_age(self) -> str:
        return self.__age

    def set_age(self, age: str):
        self.__age = age

    def get_culture(self) :
        return self.__culture

    def set_culture(self, culture: str):
        self.__culture = culture

    def get_is_on_display(self) :
        return self.__is_on_display

    def set_is_on_display(self, is_on_display: bool):
        self.__is_on_display = is_on_display

# Create an instance of Artifact
artifact = Artifact(
    artifact_id=1,
    name="Ancient Vase",
    description="A beautifully crafted ceramic vase from ancient times.",
    age="2000 years",
    culture="Greek",
    is_on_display=True
)

# Print artifact details
print("Artifact Details:")
print("Artifact ID:", artifact.get_artifact_id())
print("Name:", artifact.get_name())
print("Description:", artifact.get_description())
print("Age:", artifact.get_age())
print("Culture:", artifact.get_culture())
print("Is on display:", artifact.get_is_on_display())
