# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./story.txt", 'r') as tst:
        contents = tst.read()
        return contents
        


def count_words():
    text = read_file_content("./story.txt")
    use_text = text.lower().split()
    counts = {}

    # [assignment] Add your code here
    for word in use_text:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] =1
    return counts

    
#print(read_file_content('./story.txt'))

print(count_words())