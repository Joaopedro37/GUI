import random
import os
import cv2
import numpy as np
from typing import List, Tuple, Optional, Dict


class Arm:
    def abc(self, a: bool) -> str:
        if a:
            return "Is true."
        else:
            return "Is false."

    def efg(self, a: str) -> None:
        print(f"{a} is the string.")


class Head:
    def abc(self, a: bool) -> str:
        if a:
            return "Is true."
        else:
            return "Is false."

    def efg(self, a: str) -> None:
        print(f"{a} is the string.")


class Torso:
    def abc(self, a: bool) -> str:
        if a:
            return "Is true."
        else:
            return "Is false."

    def efg(self, a: str) -> None:
        print(f"{a} is the string.")


class PalGripper:
    def __init__(self):
        self.nothing()

    def nothing(self) -> None:
        return None
