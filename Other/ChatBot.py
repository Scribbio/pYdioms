from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from ProcessText import ProcessText

chatbot = ChatBot(
    'IdiomsBot',

    #The SQLStorageAdapter is Chatterbot's default adapter. If you do
    #not specify one, SQLStorageAdapter will be used automatically
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./database.sqlite3',

    logic_adapters=[
    #    'chatterbot.logic.MathematicalEvaluation'
    #    'chatterbot.logic.TimeLogicAdapter'
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_compaison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method" : "chatterbot.response_selection.get_first_response"
        },
        #Low confidence response adapter
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand'
        }
    ],
)

chatbot.set_trainer(ChatterBotCorpusTrainer)

# Train based on the english corpus
chatbot.train(
    #"chatterbot.corpus.english.greetings",
    #"chatterbot.corpus.english.conversations"
    "chatterbot.corpus.english"
)

while True:
    request = input("You: ")
    response = chatbot.get_response(request)
    print(response)

    textProcessor = ProcessText()
    processedResponse = textProcessor.process(str(response))



    print('Bot: ', processedResponse)
    if request.strip() == 'Bye':
        print('Bot : Bye')
        break
