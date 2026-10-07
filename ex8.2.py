feedback = input("Enter your feedback: ")

target_words = ["badword", "spam", "abuse"]

for word in target_words:
    feedback = feedback.replace(word, "****")
    feedback = feedback.replace(word.capitalize(), "****")

print("Filtered Feedback:")
print(feedback)