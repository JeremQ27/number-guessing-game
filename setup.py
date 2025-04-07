from setuptools import setup
from setuptools.config.expand import entry_points

setup(
    name='number_guessing_game',
    version='1.0.0',
    description='A CLI application of a number guessing game.',
    author='Jeremiah',
    author_email='jeremiahquinto0627@gmail.com',
    url='https://github.com/JeremQ27/number-guessing-game',
    py_modules=['app', 'set_high_score'],
    entry_points={
        'console_scripts': [
            'number_guess=app:main'
        ]
    },
    test_require=[
        'pytest'
    ]
)