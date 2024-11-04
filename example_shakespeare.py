# Example Shakespeare Prose
import os
terminal_width = os.get_terminal_size().columns # get terminal width for line breaks

# package modules
from codeshakespeare.shakespeare import (
    to_shakespeare,
    to_shakespeare_error,
    get_random_shakespeare_quote,
    generate_shakespearean_commit_message
)

# Testing `to_shakespeare` function with different formalities
comments = ["This function loads data.", "This is a simple comment.", "This is a test."]
print("TESTING `TO_SHAKESPEARE()`...\n")
print("DRAMATIC:       ", to_shakespeare(comments[0], formality="dramatic"))
print("SIMPLE:         ", to_shakespeare(comments[1], formality="simple"))
print("DEFAULT (NOBLE):", to_shakespeare(comments[2]))
print("\n" + "-" * terminal_width + "\n") # print terminal width

# Testing `to_shakespeare_error` function with different severities
error_msg =[ "Syntax error.", "Connection lost.", "File corrupted."]
print("TESTING `TO_SHAKESPEARE_ERROR`...\n")
print("HISTORY SEVERITY: ", to_shakespeare_error(error_msg[0], severity="history"))
print("DEFAULT (TRAGEDY):", to_shakespeare_error(error_msg[1]))
print("INVALID SEVERITY: ", to_shakespeare_error(error_msg[2], severity="unknown"))
print("\n" + "-" * terminal_width + "\n") # print terminal width

# Testing `get_random_shakespeare_quote` function with different styles
print("TESTING `GET_RANDOM_SHAKESPEARE_QUOTE`...\n")
print("SERIOUS QUOTE:    ", get_random_shakespeare_quote(style="serious"))
print("MELANCHOLY QUOTE: ", get_random_shakespeare_quote(style="melancholic"))
print("DEFAULT (PLAYFUL):", get_random_shakespeare_quote())
print("\n" + "-" * terminal_width + "\n") # print terminal width

# Testing `generate_shakespearean_commit_message` function with different emotions
print("TESTING `GENERATE_SHAKESPEAREAN_COMMIT_MESSAGE`...\n")
print("DEFEAT EMOTION:    ", generate_shakespearean_commit_message(emotion="defeat"))
print("REFLECTION EMOTION:", generate_shakespearean_commit_message(emotion="reflection"))
print("DEFAULT (VICTORY): ", generate_shakespearean_commit_message())
