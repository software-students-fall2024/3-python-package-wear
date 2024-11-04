#created another file and vir env an installed thepackage using pip install to check if actually workde
#it worked


from codeshakespeare.shakespeare import (
    to_shakespeare,
    to_shakespeare_error,
    get_random_shakespeare_quote,
    generate_shakespearean_commit_message
)

# Testing the `to_shakespeare` function with different formalities
print("Testing `to_shakespeare` function:")
comment = "This function loads data."
print("Dramatic:", to_shakespeare(comment, formality="dramatic"))

comment = "This is a simple comment."
print("Simple:", to_shakespeare(comment, formality="simple"))

comment = "This is a test."
print("Default (noble):", to_shakespeare(comment))

print("\n---------------------------\n")

# Testing the `to_shakespeare_error` function with different severities
print("Testing `to_shakespeare_error` function:")
error_msg = "Syntax error."
print("History severity:", to_shakespeare_error(error_msg, severity="history"))

error_msg = "Connection lost."
print("Default severity (tragedy):", to_shakespeare_error(error_msg))

error_msg = "File corrupted."
print("Invalid severity:", to_shakespeare_error(error_msg, severity="unknown"))

print("\n---------------------------\n")

# Testing the `get_random_shakespeare_quote` function with different styles
print("Testing `get_random_shakespeare_quote` function:")
print("Serious quote:", get_random_shakespeare_quote(style="serious"))
print("Melancholic quote:", get_random_shakespeare_quote(style="melancholic"))
print("Default quote (playful):", get_random_shakespeare_quote())

print("\n---------------------------\n")

# Testing the `generate_shakespearean_commit_message` function with different emotions
print("Testing `generate_shakespearean_commit_message` function:")
print("Defeat emotion:", generate_shakespearean_commit_message(emotion="defeat"))
print("Reflection emotion:", generate_shakespearean_commit_message(emotion="reflection"))
print("Default emotion (victory):", generate_shakespearean_commit_message())
