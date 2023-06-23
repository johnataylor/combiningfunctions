
from descriptions import functionDescriptions
from implememtations import functionImplementations
from openAIClient import chat_completion_request
import json

model = "gpt-3.5-turbo-0613"
api_key = ""

def run(utterance):

    messages = []
    messages.append({"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."})
    messages.append({"role": "user", "content": utterance})

    while (True):

        chat_response = chat_completion_request(model, api_key, messages, functions=functionDescriptions)

        assistant_message = chat_response.json()["choices"][0]["message"]
        messages.append(assistant_message)

        if assistant_message["content"] == None :

            function_call = assistant_message["function_call"]
            function_name = function_call["name"]
            func = functionImplementations.get(function_name)

            if func != None :
                arguments = json.loads(function_call["arguments"])
                functionResponse = func(arguments)
                messages.append({"role": "user", "content": "result from function:```" + functionResponse + "```"})
            else:
                return "unable to answer the question because function '" + function_name + "' doesn't exist"
        else:
            return assistant_message["content"]


#print(run("What is the summary for work order 00052?"))
#print(run("When was work order 00052 created?"))
#print(run("What work orders do I have for account 01234?"))
#print(run("what is the status for each work order for account 01234?"))
print(run("what are the 'in progress' work orders for account 01234?"))
