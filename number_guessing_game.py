import streamlit as st
import random

def initialize_game_state():
    if 'target_number' not in st.session_state:
        st.session_state.target_number = 0
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False

def set_difficulty(difficulty):
    if difficulty == "Easy":
        return 10
    elif difficulty == "Medium":
        return 7
    else:
        return 5

def reset_game():
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.target_number = random.randint(
        st.session_state.min_range, 
        st.session_state.max_range
    )

def main():
    st.title("Number Guessing Game 🎮")
    st.subheader("Made by Shahid Qasim")
    
    initialize_game_state()
    

    with st.sidebar:
        st.header("Game Settings")
        min_range = st.number_input("Minimum Range", value=1)
        max_range = st.number_input("Maximum Range", value=100)
        difficulty = st.selectbox(
            "Select Difficulty",
            ["Easy", "Medium", "Hard"]
        )
        max_attempts = set_difficulty(difficulty)
        
        if st.button("Start New Game"):
            st.session_state.min_range = min_range
            st.session_state.max_range = max_range
            reset_game()
    
  
    if 'min_range' not in st.session_state:
        st.warning("👈 Please set the game settings and start a new game!")
        return
    
    st.write(f"Guess a number between {st.session_state.min_range} and {st.session_state.max_range}")
    st.write(f"Difficulty: {difficulty} (Maximum {max_attempts} attempts)")
    

    guess = st.number_input("Enter your guess:", 
                           min_value=st.session_state.min_range,
                           max_value=st.session_state.max_range)
    
    if st.button("Submit Guess"):
        if not st.session_state.game_over:
            st.session_state.attempts += 1
            
            if guess == st.session_state.target_number:
                st.success(f"🎉 Congratulations! You found the number in {st.session_state.attempts} attempts!")
                st.session_state.game_over = True
            elif st.session_state.attempts >= max_attempts:
                st.error(f"Game Over! The number was {st.session_state.target_number}")
                st.session_state.game_over = True
            elif guess < st.session_state.target_number:
                st.warning("Too low! Try a higher number.")
            else:
                st.warning("Too high! Try a lower number.")
    

    st.write("---")
    st.write(f"Attempts: {st.session_state.attempts}/{max_attempts}")
    
 
    progress = st.session_state.attempts / max_attempts
    st.progress(progress)

if __name__ == "__main__":
    main() 