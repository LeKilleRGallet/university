import random




def read():
    words = []
    with open("files/wordlist.txt", 'r', encoding='utf-8') as f:
        # words = f.readlines()
        for word in f:
            words.append(word.strip())
        #print(words)
        #print(len(words))
        #print(words[0])
        #print(words[len(words)-1])
        return words

def selector(words):
    """
    docstring
    """
    index = random.randint(0, len(words)-1)
    #print(words[index])
    #print(len(words[index]))
    return words[index]

def visualization(wlen):
    """
    docstring
    """
    print('-'*wlen)




def run():
    """
    docstring
    """
    word = selector(read())
    print(f"{word}\n {len(word)}")
    print(list(word))
    


if __name__ == "__main__":
    run()