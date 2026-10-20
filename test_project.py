import pytest
from project import check_answer , count , percentage , message , load_questions

def test_check_answer():
    assert check_answer("paris","paris") == True
    assert check_answer("paris","london") == False

def test_count():
    assert count("paris","paris") == 1
    assert count("paris","london") == 0

def test_percentage():
    assert percentage(2,5) == 40
    assert percentage(5,5) == 100
    assert percentage(3,4) == 75
def test_message():
    assert "Too bad" in message(0)
    assert "Not Bad" in message(20)
    assert "Excellent" in message(100)
    assert "Good" in message(50)

def test_load_questions(tmp_path):
    f = tmp_path / "q.csv"
    f.write_text("question,answer\nWhat is 1+1?,2\nCapital of France?,paris\n")
    assert load_questions(str(f)) == [("What is 1+1?", "2"), ("Capital of France?", "paris")]

def test_load_questions_missing():
    with pytest.raises(FileNotFoundError):
        load_questions("does_not_exist.csv")
