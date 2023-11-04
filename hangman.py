import random
import os

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

def read():
    words = []
    with open("files/wordlist.txt", 'r', encoding='utf-8') as f:
        for word in f:
            words.append(word.strip())
        return words

def selector(words):
    """
    docstring
    """
    index = random.randint(0, len(words)-1)
    return words[index]

def visualization(word,ans):
    """
    docstring
    """
    while True:
        if word == ans:
            break
        clear()
        print(' '.join(ans).capitalize())
        print('- '*len(word))

        letter = input('inset a letter: ')
        ans = comparator(letter, word, ans)
    
    win(ans)

def comparator(letter, word, ans):
    """
    docstring
    """
    for i in range(len(word)):
        if letter == word[i]:
            ans[i] = letter
    
    return ans

def win(ans):
    clear()
    print(f"Congrats, you won! \n word was: {''.join(ans).capitalize()}")

def run():
    """
    docstring
    """
    word = list(selector(read()))
    ans = [' ' for i in range(len(word))]
    visualization(word,ans)
    


if __name__ == "__main__":
    run()