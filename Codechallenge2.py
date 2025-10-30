#c
def main():
    sentence = input().strip()
    vowels ={'a','e','i','o','u'}
    words = sentence.split()
    count = 0
    for word in words:
        if word and word[0].lower() in vowels:
            count += 1
            #i want to count only the number of words starts from vowel
            print(count)
if __name__ == "__main__":
    main()