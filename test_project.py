import pytest
from project import check_answer , count , percentage , message , load_questions , pick_questions , read_best , save_best

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

def test_percentage_zero():
    with pytest.raises(SystemExit):
        percentage(4,0)

def test_message():
    assert "Too bad" in message(0)
    assert "Not Bad" in message(20)
    assert "Excellent" in message(100)
    assert "way ahead" in message(50)

def test_load_questions(tmp_path):
    f = tmp_path / "q.csv"
    f.write_text("question,answer\nWhat is 1+1?,2\nCapital of France?,paris\n")
    assert load_questions(str(f)) == [("What is 1+1?", "2"), ("Capital of France?", "paris")]

def test_load_questions_missing():
    with pytest.raises(FileNotFoundError):
        load_questions("does_not_exist.csv")

def test_pick_questions():
    q = [("q1","a1"),("q2","a2"),("q3","a3"),("q4","a4")]
    picked = pick_questions(q , 2)
    assert len(picked) == 2
    picked1 = pick_questions(q , 10)
    assert len(picked1) == 4
    for item in picked :
        assert item in q

def test_read_best_missing(tmp_path):
    f = tmp_path / "best.txt"
    assert read_best(str(f)) == 0

def test_read_best_bad_file(tmp_path):
    f = tmp_path / "best.txt"
    f.write_text("abc")
    assert read_best(str(f)) == 0

def test_save_and_read_best(tmp_path):
    f = tmp_path / "best.txt"
    save_best(str(f), 80)
    assert read_best(str(f)) == 80
