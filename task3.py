import tkinter as tk
import random
import time

# Sample text for typing test
sample_text = """
This is a typing speed test.
Type this text as fast as you can.
Press the 'Start' button to begin.
"""
import random
import time

# Sample text for typing test
sample_text = "The quick brown fox jumps over the lazy dog."

def main():
    print("Welcome to the Typing Speed Test!")
    print("You will be presented with a random sentence to type.")
    print("Type the sentence as fast as you can and press Enter.")
    print("Press Enter to start...")

    input()  # Wait for user to press Enter to start the test

    # Generate a random sentence from the sample text
    words = sample_text.split()
    random.shuffle(words)
    random_sentence = " ".join(words)

    print("\nType the following sentence:")
    print(random_sentence)

    input("\nPress Enter to start typing...")

    start_time = time.time()  # Record the start time

    # Get user input
    user_input = input("\nStart typing here: ")

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time

    # Calculate typing speed
    words_typed = len(user_input.split())
    typing_speed = words_typed / (elapsed_time / 60)  # Words per minute

    # Calculate accuracy
    accuracy = calculate_accuracy(random_sentence, user_input)

    print("\nTyping test results:")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Words typed: {words_typed}")
    print(f"Typing speed: {typing_speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(original_text, user_text):
    original_words = original_text.split()
    user_words = user_text.split()

    correct_word_count = sum(1 for ow, uw in zip(original_words, user_words) if ow == uw)
    accuracy = (correct_word_count / len(original_words)) * 100

    return accuracy

if __name__ == "__main__":
    main()


