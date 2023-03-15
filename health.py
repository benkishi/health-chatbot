import re
import json
import random_responses


def load_json(file):
    with open(file) as bot_responses:
       
        return json.load(bot_responses)


response_datas = load_json("health.json")

def get_response(input_varchar):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_varchar.lower())
    score_lists = []

    for response in response_datas:
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

        score_lists.append(response_score)
        
    best_responses = max(score_lists)
    response_index = score_lists.index(best_responses)
    
    if best_responses != 0:
        return response_datas[response_index]["bot_response"]
    
    if input_varchar =="pain":    
        return random_responses.health_varchar()
    
    if input_varchar =="gerd":    
        return random_responses.health_var()
    
    return random_responses.random_string()



while True:
    user_input = input("You: ")
    print("Bot: " + get_response(user_input))
    