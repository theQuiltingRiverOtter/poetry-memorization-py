import re
from poems import poems
from poem import Poem


print("Please type in the name of a poem and a difficulty level")
print(
    "The harder levels go through more iterations of the poem, taking out more words each round"
)
has_poem = False

while not has_poem:
    poem_title = input("Please type in the title of the poem: ").lower()
    if poems.get(poem_title):
        poem = poems[poem_title]["file_name"]
        has_poem = True
    else:
        print("we don't have that poem")

has_difficulty = False
while not has_difficulty:
    difficulty = input("Please input a difficulty level (easy, medium, hard): ")
    if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
        has_difficulty = True


my_poem = Poem(poem)
my_poem.set_difficulty(difficulty)
my_poem.memorize_poem()
