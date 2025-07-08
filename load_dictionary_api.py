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
            for arg in item.args.args[1:]:  # skip 'self'
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

    for funcionalidade in sorted(os.listdir(api_root)):
        path_func = os.path.join(api_root, funcionalidade)
        if not os.path.isdir(path_func) or funcionalidade.startswith("__"):
            continue

        result[funcionalidade] = OrderedDict()

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
                except Exception:
                    continue

                module_functions = OrderedDict()

                for node in tree.body:
                    if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                        functions = extract_functions_from_class(node)
                        for fname, fdata in functions.items():
                            if fname not in module_functions:
                                module_functions[fname] = fdata

                if module_functions:
                    result[funcionalidade][module_name] = module_functions

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Input types: bool, int, float, str, Tuple, List, choice, none\n")
        f.write("# Output types: Optional, Dict, List, Tuple, none\n")
        f.write("# When the output can be an image or none, use: Optional[np.ndarray]\n\n")
        f.write("functions = ")
        f.write(json.dumps(result, indent=4))

    print(f"\nDictionary successfully generated at '{output_path}'\n")

api_path = "D:/isr_tiago-ros-noetic/planning/actions_tiago/src/actions_tiago_ros"
generate_function_dictionary(api_path)

