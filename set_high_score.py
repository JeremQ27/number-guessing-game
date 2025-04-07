import json
import os

HIGH_SCORE_PATH = 'high_score.json'
high_score_db = {}



def reset_high_score():
    with open(HIGH_SCORE_PATH, 'w') as f:
        db = {
            'easy':1000,
            'medium':1000,
            'hard':1000
        }
        json.dump(db, f)


def create_highscore_json():
    if not os.path.exists(HIGH_SCORE_PATH):
        reset_high_score()


def load_high_score():
    global high_score_db
    create_highscore_json()
    with open(HIGH_SCORE_PATH, 'r') as f:
        high_score_db = json.load(f)

def view_high_score():
    print(f'Score leaderboard')
    print(f'Easy: {high_score_db['easy']}')
    print(f'Medium: {high_score_db['medium']}')
    print(f'Hard: {high_score_db['hard']}')

def save_new_high_score(num_chances, score):
    if num_chances == 10:
        high_score_db['easy'] = min(high_score_db['easy'], score)
    elif num_chances == 5:
        high_score_db['medium'] = min(high_score_db['medium'], score)
    elif num_chances == 3:
        high_score_db['hard'] = min(high_score_db['hard'], score)
    with open(HIGH_SCORE_PATH, 'w') as f:
        json.dump(high_score_db, f)