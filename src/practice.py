import pickle

if __name__ == "__main__":
    pickle_off = open(f"poems/rupi/corpus.pkl","rb")
    corpus = pickle.load(pickle_off)
    limit = 100

    word_counter = 0

    for poem in corpus[:limit]:
        word_counter += len(poem.split())

    print(word_counter)

    corpus_tokens = (word_counter / .75)
    prompt_tokens = 12 * limit

    total_token = corpus_tokens+prompt_tokens

    print("Total Tokens: ", total_token)
    print("Training Price: ", total_token*.03)
