import time
import random

sen = ["Python makes programming fun and interesting.",
       "Practice every day to become a better developer.",
       "The sun rises in the east and sets in the west.",
       "I love learning new things about technology.",
       "Coding is a skill that improves with practice.",
       "Never stop exploring new ideas.",
       "Today is a great day to learn something new.",
       "Small steps lead to big achievements.",
       "Keep calm and solve the problem.",
       "Reading books improves your knowledge.",

       # Medium
       "Programming teaches us how to break complex problems into smaller pieces.",
       "A good developer writes code that is easy to understand and maintain.",
       "Technology continues to transform the way people communicate and work.",
       "Learning a programming language requires patience and consistent practice.",
       "Debugging is an important part of the software development process.",
       "Every expert programmer was once a beginner who refused to give up.",
       "The best way to learn coding is by building real world projects.",
       "Artificial intelligence is changing the future of modern technology.",
       "Writing clean code makes collaboration between developers much easier.",
       "Problem solving skills are valuable in almost every technical field.",

       # Hard
       "The difference between an ordinary programmer and a great developer is attention to detail.",
       "Although programming languages have different syntax, their underlying concepts are often similar.",
       "Developing reliable software requires careful planning, testing, debugging, and continuous improvement.",
       "Consistency matters more than motivation when you are learning a challenging new skill.",
       "Artificial intelligence, machine learning, and automation are reshaping industries across the world.",
       "A well structured algorithm can significantly improve the performance of a complex application.",
       "Understanding why something works is far more valuable than simply memorizing its implementation.",
       "Successful software engineers combine technical knowledge with creativity and problem solving abilities.",
       "The ability to adapt quickly is essential in an industry where technology evolves constantly.",
       "Building something from scratch teaches lessons that tutorials alone cannot provide."]

print("Welcome to speed typing test!")
print("Type the folllowing sentence")
sentence = random.choice(sen)
print(sentence)
start_time = time.perf_counter()
user_input = input()
end_time = time.perf_counter()

time_taken = end_time - start_time

print(user_input, "in", time_taken, "seconds")
wpm = (len(user_input) * 12) / time_taken

corr_char = 0
for i in range(min(len(sentence), len(user_input))):
    if user_input[i] == sentence[i]:
        corr_char += 1

accuracy = (corr_char * 100) / len(sentence)
print("Your typing speed in WPM is ", wpm, "with accuracy", accuracy)
