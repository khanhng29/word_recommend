import random
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle


def loading_model():
  global model
  model = tf.keras.models.load_model('./word_recommendation_Vinh')
  global tokenizer
  with open('tokenizer.picker','rb') as handle:
    tokenizer = pickle.load(handle)
  global max_seq_len
  max_seq_len = 26

def predict(seed_text, next_words):
  for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_seq_len - 1, padding='pre')
    predicted_probs = model.predict(token_list)
    predicted_word = tokenizer.index_word[np.argmax(predicted_probs)]
    seed_text += " " + predicted_word

  encoding_result = output_encoding(seed_text)
  return encoding_result


def generate_text(seed_text, next_words, num_samples):
    """
       Generate multiple text sequences based on a seed text using a language model.

       Args:
       - seed_text (str): The initial text from which generation starts.
       - next_words (int): The number of words to generate after the seed text.
       - num_samples (int): The number of text sequences to generate.

       Returns:
       - List[str]: A list of generated text sequences.

       This function generates text sequences by predicting words using the 'getPredict_2' function.
       It iteratively selects words based on predictions and constructs multiple text sequences.

       Note: Ensure 'getPredict_2' and 'output_encoding' functions are defined and accessible.
   """
    generated_texts = []
    global predicted_probs

    predicted_words = getPredict(seed_text, num_samples)

    for predicted_word in predicted_words:
        generated_text = seed_text
        generated_text += " " + predicted_word
        generated_text = generated_text.replace("_", " ")

        for _ in range(next_words - 1):
            next_word = getPredict(generated_text, num_samples)
            # Randomly select one word from the top 3
            chosen_word = random.choice(next_word)
            generated_text += " " + chosen_word
            generated_text = generated_text.replace("_", " ")
        generated_texts.append(generated_text)

    encoding_result = output_encoding(generated_texts)
    return encoding_result


def getPredict(generated_text, num_samples):
    """
    Generate predicted words based on an input text using a language model.

    Args:
    - generated_text (str): The input text for which predictions will be generated.
    - num_samples (int): The number of predicted words to generate.

    Returns:
    - List[str]: A list of the top predicted words.

    This function tokenizes the input text, pads it to match the model's input length,
    predicts the probabilities of the next word, and returns the top predicted words.

    Note: Ensure 'tokenizer', 'max_seq_len', and 'model' are defined appropriately.
    """
    # Tokenize the input generated_text
    token_list = tokenizer.texts_to_sequences([generated_text])[0]

    # Pad the token list to match the model's input length
    token_list = pad_sequences([token_list], maxlen=max_seq_len - 1, padding='pre')

    # Use the model to predict the probabilities of the next word
    predicted_probs = model.predict(token_list)

    # Get the indices of the top num_samples predicted words
    top_num_samples_indices = np.argsort(predicted_probs[0])[::-1][:num_samples]

    # Map the indices back to words using the tokenizer
    predicted_words = [tokenizer.index_word[i] for i in top_num_samples_indices]

    return predicted_words


def output_encoding(predict_words):
    data = {"status": True,
            "recommendations": predict_words,
            "error": []
            }
    return(data)

def main():
  loading_model()
  seed_text = "ngành X"
  next_words = 2
  # print(predict(seed_text, next_words))
  print(generate_text(seed_text, next_words, 5))

if __name__ == '__main__':
    main()



