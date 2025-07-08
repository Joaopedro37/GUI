import random
import os
import cv2
import numpy as np
from typing import List, Tuple, Optional, Dict


class ManipulationPlanningScene:

    def abc(self, a: bool) -> str:
        if a:
            return "Is true."
        else:
            return "Is false."

    def efg(self, a: str) -> None:
        return print(f"{a} is the string.")





class ManipulationPredefinedMotions:

    def abc(self, a: bool) -> str:
        if a:
            return "Is true."
        else:
            return "Is false."

    def efg(self, a: str) -> None:
        return print(f"{a} is the string.")

class ManipulationUtils:

    def abc(self, a: bool) -> str:
        if a:
            return "Is true."
        else:
            return "Is false."

    def efg(self, a: str) -> None:
        return print(f"{a} is the string.")