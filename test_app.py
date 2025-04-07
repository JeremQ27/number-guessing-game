from venv import create

import pytest
from set_high_score import *
from app import *

class Test_Num_Guess:

    @pytest.fixture(autouse=True)
    def setup_test(self):
        load_high_score()


    def test_easy(self, monkeypatch, capsys):
        monkeypatch.setattr('builtins.input', lambda _: 5)
        num_guess(5, 10)
        captured = capsys.readouterr()
        assert "Congratulations!" in captured.out
        assert "guessed the correct number in 1 attempts." in captured.out


    def test_easy_multiple_attempts(self, monkeypatch, capsys):
        inputs = iter(['1','7','5'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        num_guess(5, 3)
        captured = capsys.readouterr()
        assert "Congratulations" in captured.out
        assert "guessed the correct number in 3 attempts." in captured.out


    def test_easy_loss(self, monkeypatch, capsys):
        inputs = iter(['1','2','3','4','5','6','7','8','9','10'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        num_guess(11, 10)
        captured = capsys.readouterr()
        assert 'Maximum attempt reached. Sorry you lost.' in captured.out


    def test_error_output(self, monkeypatch, capsys):
        inputs = iter(['abc', '2'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        num_guess(2, 10)
        captured = capsys.readouterr()
        assert 'Input is invalid. Please try again.' in captured.out
        assert 'Congratulations' in captured.out


    def test_medium(self, monkeypatch, capsys):
        inputs = iter(['1', '99', '78', '51', '69'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        num_guess(69, 5)
        captured = capsys.readouterr()
        assert "Congratulations" in captured.out
        assert "guessed the correct number in 5 attempts." in captured.out


    def test_hard(self, monkeypatch, capsys):
        inputs = iter(['22','33','44'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        num_guess(44, 3)
        captured = capsys.readouterr()
        assert "Congratulations" in captured.out
        assert "guessed the correct number in 3 attempts." in captured.out


    def test_reset_high_score(self):
        reset_high_score()
        load_high_score()
        print(f'high_scored_db {high_score_db}')
        assert high_score_db['easy'] == 0
        assert high_score_db['medium'] == 0
        assert high_score_db['hard'] == 0