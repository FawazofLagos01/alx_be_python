adjective1 = input("Enter an adjective that suits the gap: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter another adjective: ")
adjective4 = input("Enter another adjective: ")
animal = input("Enter an animal name: ")
activity = input("Enter an activity (verb ending with -ing): ")
if animal == "lion":
	animal_sentence = "Then, I spotted a majestic lion roaring loudly."
else:
	animal_sentence = f"Then, I spotted a majestic {animal} lounging in the sun."
if activity == "dancing":
	activity_sentence = "It was dancing like nobody was watching!"
else:
	activity_sentence = f"It was busy {activity}."
print("--- Your Mad Libs Story ---")
print("On a beautiful", adjective1 , "I went to the zoo. I saw a funny", adjective2 , "monkey swinging from the trees.", animal_sentence , activity_sentence , "What a wild and", adjective3 , "experience!. Truly a", adjective4 , "adventure to remember!")

