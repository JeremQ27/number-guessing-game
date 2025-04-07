**Number Guessing Game App**  
  
This application asks a user the difficulty of the game which controls the number of tries, generates a number from 1 - 100 and lets a user play a number guessing game through a CLI interface.  
  
**Difficulties:**  
  _Easy_ - gives you 10 maximum tries.  
  _Medium_ - gives you 5 maximum tries.  
  _Hard_ - gives you 3 maximum tries.  

**Function Descriptions**  
```_on app.py_  
    display_menu() -> displays menu for the game.  
    other_options() -> provides additional option on user.  
    pick_difficulty() -> allows option to choose the difficulty of the game.  
    num_guess() -> handles the main guessing game functionality.  

  _on set_high_score.py_  
    reset_high_score() -> resets saved high_score  
    create_highscore_json() -> creates the high_score json file if not exists.	  
    load_high_score() -> loads the high_score on the json file.  
    view_high_score() -> allows user to view the current high score.  
    save_new_high_score() -> updates the high_score json file with the score on the current session.  ```
  
To use the app, make sure to run _python setup.py install_ first on the directory.
