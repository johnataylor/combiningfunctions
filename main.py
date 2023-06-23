
from descriptions import functionDescriptions
from implememtations import functionImplementations
import resolver

model = "gpt-3.5-turbo-0613"
api_key = ""

def run(utterance):
    return resolver.run(utterance, model, api_key, functionDescriptions, functionImplementations)

#print(run("What is the summary for work order 00052?"))
#print(run("When was work order 00052 created?"))
#print(run("What work orders do I have for account 01234?"))
#print(run("what is the status for each work order for account 01234?"))
print(run("what are the 'in progress' work orders for account 01234?"))
