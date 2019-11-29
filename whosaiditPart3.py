import math

#This code is written by Ann and the given format in the prompt
#This code is to determine how many times each word is repeated
#in the literary artwork samples by Shakespeare and Austen
# normalize
# -----
# This function takes a word and returns the same word
# with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# get_counts
# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
def get_counts(filename):
    result_dict = {"_total": 0}
    text = open(filename, 'r')
    text = text.read()
    text = text.split()
    for word in text:
        word = normalize(word)
        if word not in result_dict:
            result_dict[word] = 1
        elif word in result_dict:
            result_dict[word] = result_dict[word] + 1
        result_dict["_total"] = result_dict["_total"] + 1
    return result_dict

# Get the counts for the two shortened versions
# of the texts
shakespeare_counts = get_counts("hamlet-short.txt")
austen_counts = get_counts("pride-and-prejudice-short.txt")
del austen_counts[""]
austen_counts["_total"] = austen_counts["_total"] - 1

# get_score
# -----
# This function takes a word and a dictionary of
# word counts, and it generates a score that
# approximates the relevance of the word
# in the document from which the word counts
# were generated. The higher the score, the more
# relevant the word.
#
# In many cases, the score returned will be
# negative. Note that the "higher" of two
# negative scores is the one that is less
# negative, or the one that is closer to zero.
def get_score(word, counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)

user_input = input("Enter text: ")
user_input = user_input.split()
for i in range(len(user_input) - 1):
    user_input[i] = normalize(user_input[i])

def predict(string,s_counts,a_counts):
    shakespeare_score = 0.0
    austen_score = 0.0
    for i in range(len(string) - 1):
        shakespeare_score = shakespeare_score + get_score(string[i],s_counts)
        austen_score = austen_score + get_score(string[i],a_counts)

    if shakespeare_score > austen_score:
        print("I think this was written by William Shakespeare.")
    elif austen_score > shakespeare_score:
        print("I think this was written by Jane Austen.")
    else:
        print("I think this was written neither by William Shakespeare nor Jane Austen.")

predict(user_input,shakespeare_counts,austen_counts)
