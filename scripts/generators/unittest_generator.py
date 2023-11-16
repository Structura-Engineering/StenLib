import ast
from pathlib import Path


class UnitTestGenerator:
    def __init__(self) -> None:
        self.src_dir = Path("./StenLib")
        self.tests_dir = Path("./tests")
        self.generate_tests()

    def generate_unittest_file(
        self, dir_path: Path, test_name: str, test_content: str
    ) -> None:
        dir_path.mkdir(parents=True, exist_ok=True)
        with open(dir_path / f"{test_name}_test.py", "w") as file:
            file.write("import unittest\n\n")
            file.write(test_content)

    def generate_test_case(self, test_name: str, py_file: Path) -> str:
        with open(py_file, "r") as source:
            tree = ast.parse(source.read())
        methods = [f.name for f in tree.body if isinstance(f, ast.FunctionDef)]
        test_case_str = f'class Test{test_name.capitalize()}(unittest.TestCase):\n    """Test cases for {test_name}.py"""\n'
        for _, method in enumerate(methods):
            test_case_str += f'    def test_{method}(self):\n        """Test case for {method}"""\n        self.assertEqual(1, 1)\n'
        return test_case_str

    def generate_tests(self) -> None:
        for py_file in self.src_dir.rglob("*.py"):
            if "__" not in py_file.stem:
                test_name = py_file.stem
                test_content = self.generate_test_case(test_name, py_file)
                test_dir = self.tests_dir / py_file.relative_to(self.src_dir).parent
                self.generate_unittest_file(test_dir, test_name, test_content)


if __name__ == "__main__":
    UnitTestGenerator()
