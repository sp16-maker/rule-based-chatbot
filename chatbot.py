rules = {
    "greeting": {
        "keywords": ["hello", "hi", "hey"],
        "response": "Hello! How can I help you?"
    },

    "courses": {
        "keywords": ["course", "courses", "program"],
        "response": "We offer B.Tech programs in CSE, AI/ML, ECE and Mechanical Engineering."
    },

    "fees": {
        "keywords": ["fee", "fees", "cost"],
        "response": "The course fee depends on the program. Please contact the admission office for details."
    },

    "admission": {
        "keywords": ["admission", "apply", "application"],
        "response": "Admissions are based on the required eligibility and entrance examination."
    },

    "goodbye": {
        "keywords": ["bye", "goodbye"],
        "response": "Goodbye! Have a great day."
    }
}


def get_response(user_message):

    user_message = user_message.lower()

    for rule in rules.values():

        for keyword in rule["keywords"]:

            if keyword in user_message:
                return rule["response"]

    return "Sorry, I don't understand. Please ask about courses, fees or admission."