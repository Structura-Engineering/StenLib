from StenLib.StenEnumUtils import EnumUtils


class ExampleEnum(EnumUtils):
    """
    Example enum for testing.
    """

    A = 1
    B = 2
    C = 3


def test_get_all_values():
    """
    Test the get_all_values method of EnumUtils.
    """

    result = ExampleEnum.get_all_values()
    expected_result = [ExampleEnum.A, ExampleEnum.B, ExampleEnum.C]
    assert result == expected_result
