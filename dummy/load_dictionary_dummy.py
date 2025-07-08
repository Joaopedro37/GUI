import os
import inspect
import ast
import json
import importlib.util
from typing import get_type_hints, get_origin, get_args, Union
from collections import OrderedDict


def type_for_str(tp):
    origin = get_origin(tp)
    if origin is Union:
        args = get_args(tp)
        non_none = [arg for arg in args if arg is not type(None)]
        if len(non_none) == 1:
            return f"Optional[{type_for_str(non_none[0])}]"
        else:
            return f"Union[{', '.join(type_for_str(arg) for arg in args)}]"
    if hasattr(tp, '__name__'):
        return tp.__name__
    if hasattr(tp, '_name'):
        return tp._name
    return str(tp)


def order_functions(path_file):
    with open(path_file, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    order_class = {}
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            functions = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
            order_class[class_name] = functions
    return order_class


def import_module_dynamically(path):
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def generate_function_dictionary(api_folder="dummy", output_path="functions.py"):
    result = OrderedDict()

    for funcionalidade in sorted(os.listdir(api_folder)):
        func_path = os.path.join(api_folder, funcionalidade)
        if funcionalidade.startswith("__") or not os.path.isdir(func_path):
            continue

        result[funcionalidade] = OrderedDict()

        for root, _, files in os.walk(func_path):
            for file in sorted(files):
                if not file.endswith(".py"):
                    continue

                path = os.path.join(root, file)
                try:
                    functions_in_order = order_functions(path)
                    mod = import_module_dynamically(path)
                except Exception as e:
                    print(f"[Erro ao analisar {path}]: {e}")
                    continue

                for class_name, cls in inspect.getmembers(mod, inspect.isclass):
                    if class_name not in functions_in_order:
                        continue

                    if class_name not in result[funcionalidade]:
                        result[funcionalidade][class_name] = OrderedDict()

                    methods = dict(inspect.getmembers(cls, inspect.isfunction))

                    for func_name in functions_in_order[class_name]:
                        if func_name.startswith("_") or func_name not in methods:
                            continue
                        func = methods[func_name]

                        try:
                            type_info = get_type_hints(func)
                        except Exception as e:
                            print(f"Skipped: {class_name}.{func_name} (erro: {e})")
                            continue

                        inputs = {
                            param: type_for_str(tp)
                            for param, tp in type_info.items()
                            if param != "return"
                        }

                        output = type_info.get("return", None)

                        result[funcionalidade][class_name][func_name] = {
                            "inputs": inputs,
                            "output": type_for_str(output) if output else "NoneType"
                        }

    # Escreve no ficheiro functions.py
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Input types: bool, int, float, str, Tuple, List, choice, none\n")
        f.write("# Output types: Optional, Dict, List, Tuple, none\n")
        f.write("# When the output can be an image or none, use: Optional[np.ndarray]\n\n")
        f.write("functions = ")
        f.write(json.dumps(result, indent=4))

    print(f"Dicionário de funções gerado com sucesso em '{output_path}'")


generate_function_dictionary()