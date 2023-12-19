from StenLib.StenUtils import Utils


def test_rstr():
    """
    Test the rstr method of Utils.
    """
    result = Utils.rstr('Hello, World!')
    assert result == '!dlroW ,olleH'


def test_alphanumeric_id_generator():
    """
    Test the alphanumeric_id_generator method of Utils.
    """
    result = Utils.alphanumeric_id_generator()
    assert len(result) == 6
    assert result.isalnum()

    result_10_chars = Utils.alphanumeric_id_generator(10)
    assert len(result_10_chars) == 10
    assert result_10_chars.isalnum()

    result_negative_chars = Utils.alphanumeric_id_generator(-10)
    assert len(result_negative_chars) == 10
    assert result_negative_chars.isalnum()

    original_result = Utils.alphanumeric_id_generator(reversed=False)
    result_reversed = original_result[::-1]
    assert result_reversed == original_result[::-1]
    assert result_reversed.isalnum()


def test_alphanumeric_id_generator_secrets():
    """
    Test the alphanumeric_id_generator method of Utils with secrets module.
    """
    result = Utils.alphanumeric_id_generator(use_secrets=True)
    assert len(result) == 6
    assert result.isalnum()

    result_10_chars = Utils.alphanumeric_id_generator(10, use_secrets=True)
    assert len(result_10_chars) == 10
    assert result_10_chars.isalnum()

    result_negative_chars = Utils.alphanumeric_id_generator(
        -10, use_secrets=True
    )
    assert len(result_negative_chars) == 10
    assert result_negative_chars.isalnum()

    original_result = Utils.alphanumeric_id_generator(
        reversed=True, use_secrets=True
    )
    result_reversed = original_result[::-1]
    assert result_reversed == original_result[::-1]
    assert result_reversed.isalnum()
