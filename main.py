import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QMessageBox
from display import GenericTab
from functions import functions
import inspect
import os
import importlib

sys.path.append("/home/joao/isr_tiago/planning/actions_tiago/src/actions_tiago_ros/tools")
from tiago_api_interactive_shell import api


'''
def import_module_dynamically(path):
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def create_api_instance(folder):
    class API: pass
    api = API()

    for functionality in sorted(os.listdir(folder)):
        path_func = os.path.join(folder, functionality)
        if functionality.startswith("__") or not os.path.isdir(path_func):
            continue

        # Create sub-instance of functionality (e.g., perception, manipulation)
        functionality_class = type(functionality, (), {})
        functionality_instance = functionality_class()

        # Recursively go through all .py files in the functionality folder
        for root, _, files in os.walk(path_func):
            for file in sorted(files):
                if not file.endswith(".py"):
                    continue

                full_path = os.path.join(root, file)
                try:
                    module = import_module_dynamically(full_path)
                except Exception as e:
                    print(f"[Error importing {full_path}]: {e}")
                    continue

                for class_name, cls in inspect.getmembers(module, inspect.isclass):
                    try:
                        instance = cls()
                        setattr(functionality_instance, class_name, instance)
                    except Exception as e:
                        print(f"[Error instantiating {class_name}]: {e}")

        setattr(api, functionality, functionality_instance)

    return api


# Create the API instance from real or dummy files
robot_api_instance = create_api_instance("dummy")  # Change "dummy" to the desired API folder


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TIAGo GUI")
        self.setMinimumSize(800, 500)
        self.tabs = QTabWidget()

        for functionality in functions:
            if hasattr(robot_api_instance, functionality):
                tab = GenericTab(robot_api_instance, {functionality: functions[functionality]})
                self.tabs.addTab(tab, functionality.capitalize())
            else:
                print(f"[Warning] Functionality '{functionality}' not found in API instance.")

        self.setCentralWidget(self.tabs)

        menubar = self.menuBar()
        help_menu = menubar.addMenu("Help")
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self.show_about)

    def show_about(self):
        QMessageBox.information(self, "About", "Generic interface for any compatible robot.")
'''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TIAGo GUI")
        self.setMinimumSize(800, 500)
        self.tabs = QTabWidget()

        for functionality in functions:
            if hasattr(api, functionality):
                tab = GenericTab(api, {functionality: functions[functionality]})
                self.tabs.addTab(tab, functionality.capitalize())
            else:
                print(f"[Warning] Functionality '{functionality}' not found in API instance.")

        self.setCentralWidget(self.tabs)

        menubar = self.menuBar()
        help_menu = menubar.addMenu("Help")
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self.show_about)

    def show_about(self):
        QMessageBox.information(self, "About", "GUI.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
