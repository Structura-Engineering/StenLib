import ast
from pathlib import Path


class UnitTestGenerator:
    """A class for generating unittest files for all python files in the StenLib directory."""

    def __init__(self) -> None:
        """Initializes the UnitTestGenerator class."""
        self.generate_tests()

    def generate_tests(self) -> None:
        """Generates unittest files for all python files in the StenLib directory."""
        src_dir = Path("./StenLib")
        tests_dir = Path("./tests")

        tests_dir.mkdir(parents=True, exist_ok=True)
        for py_file in src_dir.rglob("*.py"):
            if "__" not in py_file.stem:
                test_name = py_file.stem
                test_content = self.generate_test_case(py_file)
                test_dir = tests_dir / py_file.relative_to(src_dir).parent
                with open(test_dir / f"test_{test_name}.py", "w") as file:
                    file.write(test_content)

    @staticmethod
    def generate_test_case(py_file: Path) -> str:
        """Generates a test case for the given test_name and py_file.

        Args:
            py_file (Path): The path to the python file for which the test case should be generated.

        Returns:
            str: The content of the test case.
        """
        with open(py_file, "r") as file:
            module = ast.parse(file.read())

        test_content = "import unittest\n\n"
        test_content += "from hypothesis import given\n"
        test_content += "from hypothesis import strategies as st\n\n"

        for node in module.body:
            if isinstance(node, ast.ClassDef):
                test_content += f"from StenLib.{py_file.stem} import {node.name}\n\n\n"

                test_class_name = f"Test{node.name}"
                class_docstring = ast.get_docstring(node, clean=False)
                test_content += f"class {test_class_name}(unittest.TestCase):\n"
                if class_docstring:
                    test_content += f'    """{class_docstring}"""\n\n'

                for sub_node in node.body:
                    if isinstance(sub_node, ast.FunctionDef):
                        test_method_name = f"test_{sub_node.name}"
                        test_content += f"    @given(st.integers(), st.integers())\n"
                        test_content += f"    def {test_method_name}(self, a, b):\n"

                        method_docstring = ast.get_docstring(sub_node, clean=False)
                        if method_docstring:
                            test_content += f'        """{method_docstring}"""\n'

                        test_content += f"        your_instance = {node.name}()\n"
                        test_content += (
                            f"        result = your_instance.{sub_node.name}(a, b)\n"
                        )
                        test_content += f"        self.assertIsNotNone(result)\n"

        return test_content


if __name__ == "__main__":
    UnitTestGenerator()
