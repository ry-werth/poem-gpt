# source bin/activate 
import pickle
from dotenv import load_dotenv
import os
import openai
import random
import time

def fake_poem(poet):
    # Load your API key from an environment variable or secret management service
    load_dotenv()  # take environment variables from .env.
    openai.api_key = os.getenv("OPENAI_API_KEY")


    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a poem in the style of {poet} less than 100 words",
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
        )

    return(response)


def real_poem(poet):

    pickle_off = open(f"poems/{poet}/corpus.pkl","rb")
    corpus = pickle.load(pickle_off)

    random_poem = random.choice(corpus)

    return(random_poem.replace('\n ','\n'))
    

def get_poem(poet):
    poet_to_file_path = {
        "Rupi Kaur": "rupi"
    }

    decider = random.randint(0, 1)

    if decider == 0:
        poem_dict = fake_poem(poet)
        poem = poem_dict["choices"][0]["text"]

    else:
        time.sleep(5)
        poem = real_poem(poet_to_file_path[poet])

    return(
        {
            "poem":poem,
            "real_bool":decider
        })


if __name__ == "__main__":

    
    poem_info = get_poem("Rupi Kaur")
    




