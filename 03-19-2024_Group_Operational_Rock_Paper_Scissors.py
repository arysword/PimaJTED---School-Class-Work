# Balneo CSC 03/19/2024 - Logan White, Nick Russell, Zachary Jenkins, Brody Villaman, Harry Barsiwal 
# 03-19-2024_Group_Operational_Rock_Paper_Scissors.py
# Rock Paper Scissors Game
# CC BY-NC-SA 4.0
# Imports
import random


# Variables 
players = []


# Functions
"""def run():
    player_amount()


def player_amount():
    print("Singleplayer Or Multiplayer \n\t 1) SinglePlayer \n\t 2) MultiPlayer")
    s_or_p = input("\t\t► ")
    try:
        if "1" in s_or_p:
            print("Initializing AI")
            for i in range(random.randint(10,100)):
               print("...")
            print("AI initialized")
            singleplayer_start()
    except:
        print("Try Again")


def play_again():  # asks the user if they want to replay
    play_again = input("would you like to play again?  Y/N ")
    try:
        if "Y" in play_again.upper():
            player_amount()
        elif "N" in play_again.upper():
            print("Thank you for playing")
    except:
        print("That Seems To Be A No, Thank You For Playing")


def singleplayer_start():
    
    rounds = int(input("How Many Rounds \n\t ► "))
    #while (<) or (<):



# Code
#run()




#“"""

### Global Input Handler Module ###


def input_handler(entity, prompts, valid_responses, clarification_text):
    """
    Handles user input with dynamic prompts and validation.

    Parameters:
    - entity: The name or identifier of the entity (e.g., player).
    - prompts: A list of prompts to display to the user.
    - valid_responses: A list of valid responses or a custom validation function.
    - clarification_text: A text to display for '?' input for clarification.

    Returns:
    - user_input: The validated input from the user.
    """
    while True:
        # Choose a random prompt from the list and display it
        prompt = random.choice(prompts).format(entity)
        user_input = input(prompt).strip().lower()

        # Provide clarification if the user requests it
        if user_input == '?':
            print(clarification_text)
            continue

        # Check if the input is valid
        if isinstance(valid_responses, list):
            if user_input in valid_responses:
                return user_input
            else:
                print(f"Invalid input. Please enter one of the following: {', '.join(valid_responses)} or '?' for help.")
        elif isinstance(valid_responses, str):
            if user_input :
                return user_input
            else:
                print(f"Invalid input. Please enter one of the following: {', '.join(valid_responses)} or '?' for help.")
        # Assuming valid_responses is a validation function    
        else:
            if valid_responses(user_input):
                return user_input
            else:
                print("Invalid input. Please try again or enter '?' for help.")

### Player Management Module ###

def add_player(name):
    """
    Registers a new player with the given name.
    
    Parameters:
    - name: The name of the player to add.
    """
    global players
    if name not in [player['name'] for player in players]:
        players.append({"name": name, "score": 0})
    else:
        print(f"Player {name} already exists.")

def update_score(name, points=1):
    """
    Updates the score of the specified player.
    
    Parameters:
    - name: The name of the player whose score is to be updated.
    - points: The number of points to add to the player's score.
    """
    for player in players:
        if player['name'] == name:
            player['score'] += points
            print(player)
            break

def get_player_data(name):
    """
    Retrieves the data for a specific player.
    
    Parameters:
    - name: The name of the player.
    
    Returns:
    - A dictionary containing the player's data.
    """
    for player in players:
        if player['name'] == name:
            return player
    return None

def reset_scores():
    """
    Resets the scores of all players to zero.
    """
    for player in players:
        player['score'] = 0

def list_players():
    """
    Lists all players and their scores.
    """
    for player in players:
        print(f"{player['name']}: {player['score']}")

### Game Logic Module ###

def process_choices(player_one_choice, player_two_choice):
    """
    Compares the choices of two players to determine the round outcome.
    
    Parameters:
    - player_one_choice: The choice of player one (rock, paper, or scissors).
    - player_two_choice: The choice of player two (rock, paper, or scissors).
    
    Returns:
    - A string indicating the outcome ('win', 'lose', or 'tie').
    """
    outcomes = {
        ('rock', 'scissors'): 'win',
        ('scissors', 'paper'): 'win',
        ('paper', 'rock'): 'win',
        ('scissors', 'rock'): 'lose',
        ('paper', 'scissors'): 'lose',
        ('rock', 'paper'): 'lose',
    }
    
    if player_one_choice == player_two_choice:
        return 'tie'
    return outcomes.get((player_one_choice, player_two_choice), 'tie')

def determine_winner(player_one, player_two, player_one_choice, player_two_choice):
    """
    Determines the winner of a round and updates the score.
    
    Parameters:
    - player_one: The name of player one.
    - player_two: The name of player two.
    - player_one_choice: The choice of player one.
    - player_two_choice: The choice of player two.
    """
    outcome = process_choices(player_one_choice, player_two_choice)
    if outcome == 'win':
        print(f"{player_one} wins the round!")
        update_score(player_one)
    elif outcome == 'lose':
        print(f"{player_two} wins the round!")
        update_score(player_two)
    else:
        print("It's a tie!")

### Match and Round Management Module ###

def initialize_match(num_rounds):
    """
    Prepares the game for the specified number of rounds by resetting scores.
    
    Parameters:
    - num_rounds: The total number of rounds to be played in the match.
    """
    global total_rounds, rounds_played
    total_rounds = num_rounds
    rounds_played = 0
    reset_scores()

def play_round():
    """
    Conducts a single round of the game, collecting choices and determining the round winner.
    """
    global rounds_played
    # Example player choice collection - in practice, this would use the Global Input Handler
    player_one_choice = input_handler("Player 1", ["Player 1 Choose: rock, paper, scissors? "], ["rock", "paper", "scissors"], "Enter 'rock', 'paper', or 'scissors'.")
    player_two_choice = input_handler("Player 2", ["Player 2 Choose: rock, paper, scissors? "], ["rock", "paper", "scissors"], "Enter 'rock', 'paper', or 'scissors'.")

    # Assuming the existence of 'determine_winner' function from the Game Logic Module
    determine_winner("Player 1", "Player 2", player_one_choice, player_two_choice)
    rounds_played += 1

def match_completion():
    """
    Checks if the match has reached its conclusion based on the number of rounds played.
    
    Returns:
    - True if the match is complete, False otherwise.
    """
    return rounds_played >= total_rounds

def declare_match_winner():
    """
    Analyzes player scores to declare the match winner.
    """
    # Example scoring logic
    scores = [(player['name'], player['score']) for player in players]
    print(scores)
    scores.sort(key=lambda x: x[1], reverse=True)  # Sort players by score
    print(scores)
    if scores[0][1] == scores[1][1]:  # Check for a tie
        print("The match ends in a tie!")
    else:
        print(f"The match winner is {scores[0][0]} with {scores[0][1]} wins!")

### Cheeky Text Generator Module ###

# Sample messages dictionary
messages = {
    "start": [
        "Let's get this party started! Rock, Paper, Scissors - What will it be?",
        "Prepare yourselves for the ultimate showdown of Rock, Paper, Scissors!",
        "May the odds be ever in your favor. Rock, Paper, Scissors!",
    ],
    "win": [
        "Victory is sweet, isn't it? Enjoy the glory!",
        "You're on fire! Another win in the bag.",
        "Is it skill, or is it luck? Either way, you're winning!",
    ],
    "lose": [
        "Ouch, that one hurt. But there's always the next round!",
        "Defeat is just a stepping stone to success. Or so they say.",
        "Maybe try not to lose next time? Just a suggestion.",
    ],
    "tie": [
        "A tie? Come on, you can do better than that!",
        "Looks like you're evenly matched. This just got interesting.",
        "It's a draw! Both of you are too good at this.",
    ],
    "end": [
        "And that's a wrap! Hope you enjoyed playing.",
        "Game over! Thanks for playing. Rematch?",
        "The end is here. But every end is a new beginning, right? Another round?",
    ],
}

def generate_text(context):
    """
    Generates a cheeky text message based on the provided context.
    
    Parameters:
    - context: The game context for which a message is needed (start, win, lose, tie, end).
    
    Returns:
    - A string containing the selected message.
    """
    if context in messages:
        return random.choice(messages[context])
    else:
        return "Oops, something went wrong. Let's play!"

### Overall Game Controller Module ###

def setup_game():
    print(generate_text("start"))
    num_players = int(input_handler("Setup", ["How many warriors step into the arena today? "], "*" , "Enter the number of players"))
    for i in range(num_players):
        player_name = input(f"Enter Player {i+1}'s name: ")
        add_player(player_name)
    initialize_match(int(input_handler("Setup", ["How many rounds shall we play? "], "*", "Enter the total number of rounds for the match.")))

def play_game():
    while not match_completion():
        play_round()
    declare_match_winner()

def main():
    while True:
        setup_game()
        play_game()
        if input_handler("Game Over", [generate_text("end")], ["yes", "no"], "Play again? (yes/no)") != "yes":
            break
    print("Thank you for playing. Goodbye!")


main()


hello
