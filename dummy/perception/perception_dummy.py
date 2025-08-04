import random
import os
import cv2
import numpy as np
from typing import List, Tuple, Optional, Dict




class PerceptionFaceRecognition:
    def __init__(self):
        self.names_pool = ["João", "Quim", "Ricardo", "Marisa", "Inês"]
        self.male_names = ["João", "Quim", "Ricardo"]
        self.female_names = ["Marisa", "Inês"]
        self.ageRange: str = "unknown"
        self.gender: str = "unknown"
        self.recorded_detections = ["João", "Inês", "Ricardo"]

    def _generate_detections(self) -> list:
        n = random.randint(0, 5)
        selected_names = random.sample(self.names_pool, n)
        return selected_names

    def getPeopleDetection(self, read_record: bool = False) -> list:
        text1 = []
        text2 = []

        for name in self.recorded_detections:
            text1.append(f"{name} (age: {self.ageRange}, gender: {self.gender})")

        for name in self._generate_detections():
            text2.append(f"{name} (age: {self.ageRange}, gender: {self.gender})")

        if read_record:
            print("Returning recorded detections")
            return text1
        else:
            print("Simulating current detection")
            return text2

    def getImgById(self, person_id: str) -> Optional[np.ndarray]:
        print(f"[DEBUG] Received person_id: '{person_id}'")

        if not person_id or person_id.strip() == "":
            print("[ERROR] Empty ID")
            return None

        name_map = {
            "João": "joao",
            "Ricardo": "ricardo",
            "Quim": "quim",
            "Marisa": "marisa",
            "Inês": "ines"
        }

        if person_id == 'Unknown':
            return None

        mapped_name = name_map.get(person_id)
        if mapped_name is None:
            print(f"[ERROR] Name '{person_id}' not recognized.")
            return None

        file_name = mapped_name + ".png"
        image_path = os.path.join("dummy_images", file_name)

        print(f"[DEBUG] Image path: {image_path}")

        if not os.path.exists(image_path):
            print(f"[WARNING] Image not found for: {person_id}")
            return None

        img = cv2.imread(image_path)
        if img is None:
            print(f"[ERROR] Failed to load image for: {person_id}")
        return img

    def genderAndAgeDetection(self, name: str) -> Tuple[str, str]:
        if name in self.male_names:
            gender = "Male"
        elif name in self.female_names:
            gender = "Female"
        else:
            gender = "Other"
        age = str(random.randint(20, 60))
        return age, gender

    def faceAnalysis(self, person_id: str) -> Dict[str, str]:
        gender = "Male" if person_id in self.male_names else "Female"
        return {
            "emotion": "happy",
            "age": str(random.randint(20, 60)),
            "gender": gender,
            "race": "unknown"
        }


class PerceptionManipulation:
    def __init__(self):
        # List of possible places
        self.places = ["kitchen", "bedroom", "garden"]

    # Simulates navigation to a location, if the name matches an available place
    def move(self, name: str) -> str:
        for place in self.places:
            if name.lower() == place.lower():
                message = f"Going to {place}."
                return message

        message = f"Place '{name}' not recognized. Available places: {', '.join(self.places)}"
        return message


class PerceptionMediapipe:
    def __init__(self):
        self.nothing()

    def nothing(self) -> None:
        return None


class PerceptionObjectDetection:
    def __init__(self):
        self.nothing()

    def nothing(self) -> None:
        return None


class PerceptionPoseEstimation:
    def __init__(self):
        self.nothing()

    def nothing(self) -> None:
        return None


class PerceptionSurfaces:
    def __init__(self):
        self.nothing()

    def nothing(self) -> None:

        return None
