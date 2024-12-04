import random
from collections import defaultdict

def train_markov_chain(text, n=2):
    """
    Train a Markov chain on the given text.
    
    Parameters:
        text (str): The input text to train on.
        n (int): The size of the n-grams to use. Default is 2 (bigrams).
        
    Returns:
        dict: A dictionary representing the Markov chain.
    """
    words = text.split()
    markov_chain = defaultdict(list)
    
    # Create the n-grams and store the transitions
    for i in range(len(words) - n):
        prefix = tuple(words[i:i+n])
        next_word = words[i+n]
        markov_chain[prefix].append(next_word)
    
    return markov_chain

def generate_text(markov_chain, start_words, length=50):
    """
    Generate text using a trained Markov chain.
    
    Parameters:
        markov_chain (dict): The trained Markov chain.
        start_words (list): A list of starting words to begin generation.
        length (int): The number of words to generate. Default is 50.
        
    Returns:
        str: The generated text.
    """
    generated_words = list(start_words)
    prefix = tuple(start_words)
    
    for _ in range(length - len(start_words)):
        if prefix in markov_chain:
            next_word = random.choice(markov_chain[prefix])
            generated_words.append(next_word)
            prefix = tuple(generated_words[-len(prefix):])
        else:
            break
    
    return ' '.join(generated_words)

# Example usage
if _name_ == "_main_":
    # Input text to train on
    input_text = """
    Markov chains are mathematical systems that experience transitions from one state to another
    according to certain probabilistic rules. They are often used for text generation, where the
    next word is predicted based on the previous word(s).
    """
    
    # Train the Markov chain
    n_grams = 2  # Using bigrams
    markov_chain = train_markov_chain(input_text, n=n_grams)
    
    # Generate text
    start_words = ["Markov", "chains"]
    generated_text = generate_text(markov_chain, start_words, length=30)
    print("Generated Text:")
    print(generated_text)
