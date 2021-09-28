from problems import chars_in_sonnets


def test_chars_in_sonnets():
    num_chars = chars_in_sonnets()
    assert num_chars == 94084, f"Expected 94084 total characters, but chars_in_sonnets returned {num_chars}"
