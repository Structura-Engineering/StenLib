import ast
from pathlib import Path


class UnitTestGenerator:
    """A class for generating unittest files for all python files in the StenLib directory."""

    def __init__(self) -> None:
        """Initializes the UnitTestGenerator class."""
        self.src_dir = Path("./StenLib")
        self.tests_dir = Path("./tests")
        self.generate_tests()

    def generate_unittest_file(
        self, dir_path: Path, test_name: str, test_content: str
    ) -> None:
        """Generates a unittest file for the given test_name and test_content.

        Args:
            dir_path (Path): The path to the directory where the unittest file should be created.
            test_name (str): The name of the test file.
            test_content (str): The content of the test file.
        """
        dir_path.mkdir(parents=True, exist_ok=True)
        with open(dir_path / f"{test_name}_test.py", "w") as file:
            file.write("import unittest\n\n")
            file.write(test_content)

    def generate_test_case(self, py_file: Path) -> str:
        """Generates a test case for the given test_name and py_file.

        Args:
            py_file (Path): The path to the python file for which the test case should be generated.

        Returns:
            str: The content of the test case.
        """
        with open(py_file, "r") as file:
            module = ast.parse(file.read())

        test_content = ""

        for node in module.body:
            if isinstance(node, ast.ClassDef):
                test_class_name = f"Test{node.name}"
                class_docstring = ast.get_docstring(node, clean=False)
                test_content += f"class {test_class_name}(unittest.TestCase):\n"
                if class_docstring:
                    test_content += f'    """{class_docstring}"""\n'

                for sub_node in node.body:
                    if isinstance(sub_node, ast.FunctionDef):
                        test_method_name = f"test_{sub_node.name}"
                        test_content += f"    def {test_method_name}(self):\n"

                        method_docstring = ast.get_docstring(sub_node, clean=False)
                        if method_docstring:
                            test_content += f'        """{method_docstring}"""\n'

                        test_content += self.generate_test_body(py_file, sub_node)
                        test_content += "        pass\n\n"

        return test_content

    # TODO: This does nothing. its mimicing generate_test_case.
    def generate_test_body(self, py_file: Path, function_node: ast.FunctionDef) -> str:
        """Generates the test body for a given method.

        Args:
            py_file (Path): The path to the python file for which the test body should be generated.
            function_node (ast.FunctionDef): The function node for which the test body should be generated.

        Returns:
            str: The content of the test body.
        """
        test_body = ""

        with open(py_file, "r") as file:
            lines = file.readlines()

        method_start = function_node.lineno - 1
        method_end = function_node.end_lineno

        method_lines = lines[method_start:method_end]

        for line in method_lines[1:]:
            test_body += f"        # {line.strip()}\n"

        return test_body

    def generate_tests(self) -> None:
        """Generates unittest files for all python files in the StenLib directory."""
        for py_file in self.src_dir.rglob("*.py"):
            if "__" not in py_file.stem:
                test_name = py_file.stem
                test_content = self.generate_test_case(py_file)
                test_dir = self.tests_dir / py_file.relative_to(self.src_dir).parent
                self.generate_unittest_file(test_dir, test_name, test_content)


if __name__ == "__main__":
    UnitTestGenerator()
