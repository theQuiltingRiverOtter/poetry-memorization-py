import re
from poems import poems


class Poem:
    def __init__(self, file_name: str):
        self._file_name = file_name
        with open(self._file_name) as file:
            self._data = file.read().split("\n")
        self._difficulty = "easy"

    def get_lines(self):
        return self._data

    def get_difficulty(self):
        return self._difficulty.title()

    def set_difficulty(self, difficulty):
        self._difficulty = difficulty

    def get_pattern(self, word_length: int):
        if word_length >= 8:
            regex = re.compile(r"\b\w{8,}\b")
        elif word_length >= 6:
            regex = re.compile(r"\b\w{6,}\b")
        elif word_length >= 4:
            regex = re.compile(r"\b\w{4,}\b")
        elif word_length >= 3:
            regex = re.compile(r"\b\w{3,}\b")
        elif word_length >= 2:
            regex = re.compile(r"\b\w{2,}\b")
        else:
            regex = re.compile(r"\b\w{1,}\b")
        return regex

    def get_words(self, start_ind: int, end_ind: int, word_length: int):
        regex = self.get_pattern(word_length)
        all_words = []
        for line in self._data[start_ind:end_ind]:
            words = regex.findall(line)
            all_words.append(words)
        return all_words

    def print_stanza(self, start_ind: int, end_ind: int, word_length: int):
        regex = self.get_pattern(word_length)
        for line in self._data[start_ind:end_ind]:
            new_line = regex.sub("________", line)
            print(new_line)
        print()

    def get_lower_limit(self):
        if self._difficulty == "medium":
            lower_limit = 3
        elif self._difficulty == "easy":
            lower_limit = 4
        else:
            lower_limit = 0
        return lower_limit

    def memorize_stanza(self, start: int, end: int, remove_word_length=8):
        memorized = False
        lower_limit = self.get_lower_limit()
        level = 1
        while not memorized:
            if remove_word_length <= lower_limit:
                return
            print(f"\n\n~~ You are on level {level} ~~\n")
            words_to_fill = self.get_words(start, end, remove_word_length)
            score = 0
            count = sum(len(words) for words in words_to_fill)
            while score < count:
                score = 0
                self.print_stanza(start, end, remove_word_length)
                for line_index, line in enumerate(words_to_fill):
                    for word_index, word in enumerate(line):
                        answer = input(f"Line {line_index +1}, Word {word_index +1}: ")
                        if answer.lower() == word.lower():
                            score += 1
                        else:
                            print("No, here are some hints")
                            print(f"It starts with {word[0]} and ends with {word[-1]}")
                            print(f"It is {len(word)} letters long")
                            continue
                print(f"\nYou got {score} words out of {count}\n\n")
            if remove_word_length > 5:
                remove_word_length -= 2
            else:
                remove_word_length -= 1
            level += 1

    def memorize_poem(self):
        stanzas_memorized = 0
        i = 0
        while i <= len(self._data) - 2:
            for j in range(i, len(self._data)):
                if self._data[j] == "":
                    total_lines = j - i
                    end = j
                    print(
                        f"\n~~ Try to fill in the words: {self._difficulty} Mode ~~",
                        end="",
                    )
                    self.memorize_stanza(i, end)
                    stanzas_memorized += 1
                    print(
                        f"You have {stanzas_memorized} stanzas memorized from the poem"
                    )
                    i += total_lines
