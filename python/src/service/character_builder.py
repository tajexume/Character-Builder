"""
This class creates a fake character with either randomly generated attributes or set attributes
"""
import io

from datetime import date

from faker import Faker

fake = Faker()

gender_choice = {
    'M': fake.first_name_male(),  # Male Choice
    'F': fake.first_name_female(),  # Female Choice
    'NB': fake.first_name_nonbinary(),  # NonBinary Choice
    'R': fake.name(),     # Random Name and Gender
}

gender_map = {
    'M': 'Male',
    'F': 'Female',
    'NB': 'NonBinary',
}


class FakeCharacter:

    def __init__(self, gender: str = 'R', height: int = 68, weight: int = 180, creator: str = "Unknown",
                 dob=date.today(), characterID: int = -1, race: str = "AA"):
        """
        :str gender: character's gender, Set to Random if not specified
        :int height: character's height in inches, Set to Average Height if not specified
        :int weight: character's weight in lbs., Set to Average Weight if not specified
        :str creator: the creator of the character, Set to Unknown if not specified
        :[IOBase, str] bio: character's biography (is always empty upon creation)
        :date dob: character's date of birth, Set to today's date if not specified
        :int characterID: character's unique creation ID, Set to -1 if not specified
        :str race: characters race, Set to AA if not specified
        """
        if gender not in gender_choice:
            raise Exception(f"{gender} is not a valid option!")
        elif gender == 'R':
            gender = fake.random_choices(elements=('M', 'F', 'NB'), length=1)[0]
            self.gender = gender_map[gender]
            self.first_name = gender_choice[gender]
            self.last_name = fake.last_name()
        else:
            self.gender = gender_map[gender]
            self.first_name = gender_choice[gender]
            self.last_name = fake.last_name()
        if height < 1:
            raise Exception("Height must be at least 1 in.")
        else:
            self.height = height
        if weight < 1:
            raise Exception("Weight must be at least 1 lbs.")
        else:
            self.weight = weight
        self.creator = creator
        self.dob = dob
        self.bio = ""
        self.characterID = characterID
        self.race = race

    def set_first_name(self, first_name: str) -> None:
        self.first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        self.last_name = last_name

    def create_bio(self, bio) -> None:
        if isinstance(bio, io.IOBase):
            with open(bio, 'r') as file:
                self.bio = bio.read()
        elif isinstance(bio, str):
            self.bio = bio
        else:
            raise TypeError("You did not enter a Text File or String!")

    def switch_gender(self, gender: str) -> None:
        if gender not in gender_choice:
            raise Exception(f"{gender} is not an option! Please select M, F, NB, or R")

        match gender:
            case 'R':
                self.gender = gender_choice[fake.random_choices(elements=('M', 'F', 'NB'), length=1)][0]

            case 'M':
                self.gender = 'Male'

            case 'F':
                self.gender = 'Female'

            case 'NB':
                self.gender = 'NonBinary'

    def whoCreatedMe(self) -> str:
        return self.creator

    def whenIsMyBirthday(self) -> date:
        return self.dob

    def change_birthday(self, dob: date) -> None:
        self.dob = dob

    def set_height(self, height: int) -> None:
        if height < 1:
            raise Exception("Height must be at least 1 in.")
        self.height = height

    def set_weight(self, weight: int) -> None:
        if weight < 1:
            raise Exception("Weight must be at least 1 in.")
        self.weight = weight

    def jsonify(self):
        """
        returns a dictionary with FakeCharacter attribute names
        and values
        :return dict(
        bio, characterID, creator, dob, first_name, gender, height, last_name, weight)
        """
        attrs = [
            self.bio,
            self.characterID,
            self.creator,
            self.dob,
            self.first_name,
            self.gender,
            self.height,
            self.last_name,
            self.race,
            self.weight,
        ]
        attr_names = [attr for attr in dir(self) if
                      not attr.startswith("__") and not callable(getattr(self, attr))]
        return dict(zip(attr_names, attrs))