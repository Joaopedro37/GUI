import inspect
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QLineEdit, QListWidget, QTextEdit, QListWidgetItem, QFormLayout, QStackedWidget, QCheckBox, QComboBox, QScrollArea, QGroupBox
)

import numpy as np
import json

import importlib.util
from typing import get_type_hints, get_origin, get_args, Union
import re
import os
from collections import OrderedDict
import ast

from functions import functions
from widgets import widget_image, widget_lineedit, widget_textedit, widget_bool, widget_choice


def type_to_widget(type_str: str, param_name: str = "") -> QWidget:
    """
    Generates an appropriate input widget based on the given type string.
    """
    type_str = type_str.lower()

    if type_str == "bool":
        return widget_bool(param_name)
    elif type_str in {"int", "float", "str"}:
        return widget_lineedit(param_name)
    elif type_str.startswith("tuple") or type_str.startswith("list"):
        return widget_lineedit(param_name)
    elif type_str.startswith("optional"):
        return widget_lineedit(param_name)
    else:
        return widget_lineedit(param_name)


def extract_actual_widget(widget_container: QWidget) -> QWidget:
    layout = widget_container.layout()
    if layout is None or layout.count() == 0:
        return widget_container
    for i in range(layout.count()):
        item = layout.itemAt(i)
        child = item.widget()
        if isinstance(child, (QLineEdit, QCheckBox, QComboBox, QTextEdit)):
            return child
    return widget_container


def get_widget_value(widget: QWidget, type_str: str):
    """
    Extracts the value from a generic widget (like QLineEdit/QCheckBox/QComboBox)
    based on the given data type.
    """
    type_str = type_str.lower()
    actual = extract_actual_widget(widget)

    try:
        if type_str == "bool" and isinstance(actual, QCheckBox):
            return actual.isChecked()

        elif type_str == "int" and isinstance(actual, QLineEdit):
            return int(actual.text())

        elif type_str == "float" and isinstance(actual, QLineEdit):
            return float(actual.text())

        elif type_str == "str" and isinstance(actual, QLineEdit):
            return actual.text()

        elif (type_str.startswith("list") or type_str.startswith("tuple")) and isinstance(actual, QLineEdit):
            items = re.split(r",\s*", actual.text())
            return items if type_str.startswith("list") else tuple(items)

        elif type_str.startswith("optional") and isinstance(actual, QLineEdit):
            return actual.text() if actual.text() else None

        elif isinstance(actual, QLineEdit):
            return actual.text()

    except Exception as e:
        print(f"[Error extracting value from widget]: {e}")
        return None

    return None


def display_output(result, type_str: str, output_area):
    output_area.clear()
    type_str = type_str.lower().strip()

    if type_str.startswith("optional["):
        type_str = type_str[len("optional["):-1].strip()
        if result is None:
            output_area.setText("[Result: None]")
            return

    if type_str == "ndarray" and isinstance(result, np.ndarray):
        widget_image(result)
        output_area.setText("[Image displayed in an external window]")

    elif type_str == "dict":
        output_area.setText(json.dumps(result, indent=2))

    elif type_str == "list":
        text = "\n".join(str(item) for item in result)
        output_area.setText(text.strip())

    elif type_str == "tuple":
        output_area.setText(str(result))

    elif type_str == "nonetype" or type_str == "none":
        output_area.setText("")

    else:
        output_area.setText(str(result))


def create_function_widgets(function_name: str, func, config: dict) -> QVBoxLayout:
    layout = QVBoxLayout()
    layout.addWidget(QLabel(f"<b>{function_name}</b>"))

    form = QFormLayout()
    input_widgets = {}

    for param, type_str in config["inputs"].items():
        widget = type_to_widget(type_str, param)
        form.addRow(widget)
        input_widgets[param] = (widget, type_str)

    output_area = widget_textedit(True)
    button = QPushButton("Execute")
    button.setMaximumWidth(120)

    def callback():
        kwargs = {}
        for name, (widget, type_str) in input_widgets.items():
            try:
                kwargs[name] = get_widget_value(widget, type_str)
            except Exception as e:
                output_area.setText(f"[Error in input '{name}']: {e}")
                return
        try:
            result = func(**kwargs)
            display_output(result, config["output"], output_area)
        except Exception as e:
            output_area.setText(f"[Execution error]: {e}")

    button.clicked.connect(callback)

    layout.addLayout(form)

    button_row = QHBoxLayout()
    button_row.addStretch()
    button_row.addWidget(button)

    layout.addLayout(button_row)
    layout.addWidget(output_area)
    layout.addSpacing(20)

    return layout


class GenericTab(QWidget):
    def __init__(self, api_instance, functions_dict):
        super().__init__()
        self.api = api_instance
        self.functions = functions_dict
        self.init_ui()

    def init_ui(self):
        functionality = next(iter(self.functions))
        modules = self.functions[functionality]

        layout = QHBoxLayout()
        self.menu = QListWidget()
        self.stack = QStackedWidget()

        for module_name, function_dict in modules.items():
            self.menu.addItem(QListWidgetItem(module_name))

            functionality_instance = getattr(self.api, functionality, None)
            if not functionality_instance:
                self.stack.addWidget(QLabel(f"[Error] Functionality '{functionality}' not found"))
                continue

            module_widget = QWidget()
            module_layout = QVBoxLayout()

            for function_name, config in function_dict.items():
                # Assumimos que as funções são instanciadas diretamente como api.<funcionalidade>.<função>
                if not hasattr(functionality_instance, function_name):
                    continue
                func = getattr(functionality_instance, function_name)
                function_layout = create_function_widgets(function_name, func, config)
                module_layout.addLayout(function_layout)

            module_widget.setLayout(module_layout)
            scroll = QScrollArea()
            scroll.setWidget(module_widget)
            scroll.setWidgetResizable(True)
            self.stack.addWidget(scroll)

        self.menu.currentRowChanged.connect(self.stack.setCurrentIndex)

        layout.addWidget(self.menu, 1)
        layout.addWidget(self.stack, 4)
        self.setLayout(layout)

