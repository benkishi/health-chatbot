import re
import json
import random_responses
import long_responses as long



bot_name="BEN: "
print("Lets Chat! (type 'quit' to exit)")

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)


        # Longer responses
    response(random_responses.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(random_responses.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    #response(random_responses.R_HEALTH, ['feel', 'you', 'need'], required_words=['feel', 'need'])e

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return random_responses.random_string() if highest_prob_list[best_match] < 1 else best_match

def get_responses(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    respond = check_all_messages(split_message)
    return respond



def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


response_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        if required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1

        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response)


    if input_string == "":
        return "Please type something so we can chat :("
    
    if best_response != 0:
        return response_data[response_index]["bot_response"]   

    return random_responses.random_string()
    
    
while True:
    
    user_input= input('You: ')

    if user_input == "quit":
        print((bot_name) + "goodbye")
        break
 
    print((bot_name) + get_response(user_input))
