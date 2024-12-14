def reverse_string(s):
    return s[::-1]

def test_reverse_string():

    # Arrange.
    input_string = "olleh"
    expected_output = "hello"

    # Act.
    result = reverse_string(input_string)

    # Assert.
    assert result == expected_output
