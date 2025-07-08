import inspect
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy,
    QLabel, QLineEdit, QListWidget, QTextEdit, QListWidgetItem, QFormLayout, QStackedWidget, QCheckBox, QComboBox, QScrollArea
)

from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
import numpy as np
import cv2
from typing import get_type_hints, get_origin, get_args
import json


def widget_image(img: np.ndarray):
    """
    Displays a given image (np.ndarray) in an external OpenCV window.
    """
    if img is not None and isinstance(img, np.ndarray):
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Invalid image.")


def widget_bool(label_text: str) -> QWidget:
    container = QWidget()
    layout = QHBoxLayout()

    layout.setContentsMargins(0, 0, 0, 0)  # no extra margins
    layout.setSpacing(10)  # spacing between label and checkbox

    if label_text:
        label = QLabel(f"{label_text}")
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(label)

    checkbox = QCheckBox()
    checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # expands horizontally
    layout.addWidget(checkbox)

    layout.addStretch()  # pushes everything to the left

    container.setLayout(layout)

    # Expands horizontally, fixed height
    container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    return container


def widget_choice(choices):
    combo = QComboBox()
    if choices:
        combo.addItems(choices)
    return combo


def widget_lineedit(label_text):
    container = QWidget()
    layout = QHBoxLayout()
    if label_text:
        layout.addWidget(QLabel(f"{label_text}"))

    layout.addWidget(QLineEdit())
    container.setLayout(layout)
    return container


def widget_textedit(readonly=False):
    w = QTextEdit()
    w.setReadOnly(readonly)
    return w














