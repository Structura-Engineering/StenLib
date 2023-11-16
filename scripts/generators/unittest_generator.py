from pathlib import Path


class UnitTestGenerator:
    def __init__(self, src_dir: str) -> None:
        self.src_dir = Path(src_dir)
        self.generate_tests()

    def generate_unittest_file(
        self, dir_path: Path, test_name: str, test_content: str
    ) -> None:
        dir_path.mkdir(parents=True, exist_ok=True)
        with open(dir_path / f"{test_name}_test.py", "w") as file:
            file.write("import unittest\n\n")
            file.write(test_content)

    def generate_test_case(self, test_name: str, test_cases: list) -> str:
        test_case_str = f"class Test{test_name.capitalize()}(unittest.TestCase):\n"
        for i, test_case in enumerate(test_cases):
            test_case_str += f"""
        def test_case{i+1}(self):
            {test_case}
    """
        return test_case_str

    def generate_tests(self) -> None:
        for py_file in self.src_dir.rglob("*.py"):
            if "__" not in py_file.stem:
                test_name = py_file.stem
                test_cases = ["self.assertEqual(1, 1)", "self.assertEqual(2, 2)"]
                test_content = self.generate_test_case(test_name, test_cases)
                test_dir = Path("tests") / py_file.relative_to(self.src_dir).parent
                self.generate_unittest_file(test_dir, test_name, test_content)


if __name__ == "__main__":
    UnitTestGenerator("./StenLib")
