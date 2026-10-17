from project import check_answer , count , percentage , message

def test_check_answer():
    assert check_answer("paris","paris") == True
    assert check_answer("paris","london") == False

def test_count():
    assert count("paris","paris") == 1
    assert count("paris","london") == 0

def test_percentage():
    assert percentage(2) == 40
    assert percentage(5) == 100

def test_message():
    assert message(20) == "Not Bad! But you can improve a lot. Keep Practicing 😄"
    assert message(100) == "Excellent!! You got highest. Here is my bow to you 🙌"
