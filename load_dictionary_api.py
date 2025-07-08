import os
import ast
import json
from collections import OrderedDict


def extract_type(annotation):
    if isinstance(annotation, ast.Name):
        return annotation.id
    elif isinstance(annotation, ast.Subscript):
        root = extract_type(annotation.value)
        arg = extract_type(annotation.slice)
        return f"{root}[{arg}]"
    elif isinstance(annotation, ast.Attribute):
        return f"{annotation.value.id}.{annotation.attr}"
    elif isinstance(annotation, ast.Tuple):
        return "Tuple"
    elif isinstance(annotation, ast.List):
        return "List"
    elif isinstance(annotation, ast.BinOp):  # Optional | None
        return "Optional"
    else:
        return "Any"


def extract_functions_from_class(class_node):
    functions = OrderedDict()

    for item in class_node.body:
        if isinstance(item, ast.FunctionDef) and not item.name.startswith("_"):
            inputs = OrderedDict()
            for arg in item.args.args[1:]:  # Ignore 'self'
                name = arg.arg
                if arg.annotation:
                    inputs[name] = extract_type(arg.annotation)
                else:
                    inputs[name] = "Any"

            if item.returns:
                output = extract_type(item.returns)
            else:
                output = "NoneType"

            functions[item.name] = {
                "inputs": inputs,
                "output": output
            }

    return functions


def generate_function_dictionary(api_root, output_path="functions.py"):
    result = OrderedDict()

    for functionality in sorted(os.listdir(api_root)):
        path_func = os.path.join(api_root, functionality)
        if not os.path.isdir(path_func) or functionality.startswith("__"):
            continue

        result[functionality] = OrderedDict()

        for root, _, files in os.walk(path_func):
            if "test" in root or "__pycache__" in root:
                continue

            for file in sorted(files):
                if not file.endswith(".py") or file.startswith("test_") or file.startswith("__"):
                    continue

                file_path = os.path.join(root, file)
                module_name = os.path.splitext(file)[0]

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read())
                except Exception as e:
                    print(f"[Error while reading {file_path}]: {e}")
                    continue

                module_functions = OrderedDict()

                # 1. Look for 'Mixin' class
                mixin_found = False
                for node in tree.body:
                    if isinstance(node, ast.ClassDef) and node.name == "Mixin":
                        functions = extract_functions_from_class(node)
                        if functions:
                            module_functions.update(functions)
                            mixin_found = True
                        break

                #If no Mixin found collect public classes
                if not mixin_found:
                    for node in tree.body:
                        if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                            class_functions = extract_functions_from_class(node)
                            if class_functions:
                                if node.name not in module_functions:
                                    module_functions[node.name] = class_functions

                if module_functions:
                    result[functionality][module_name] = module_functions if not mixin_found else module_functions

    # Write to functions.py
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Input types: bool, int, float, str, Tuple, List, choice, none\n")
        f.write("# Output types: Optional, Dict, List, Tuple, none\n")
        f.write("# When the output can be an image or none, use: Optional[np.ndarray]\n\n")
        f.write("functions = ")
        f.write(json.dumps(result, indent=4))

    print(f"\nDictionary successfully generated at '{output_path}'\n")


api_path = "D:/isr_tiago-ros-noetic/planning/actions_tiago/src/actions_tiago_ros"
generate_function_dictionary(api_path)
