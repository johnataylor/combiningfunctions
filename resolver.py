
from openAIClient import chat_completion_request
import json

def run(utterance, model, api_key, functionDescriptions, functionImplementations):

    messages = []
    messages.append({"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."})
    messages.append({"role": "user", "content": utterance})

    while (True):

        chat_response = chat_completion_request(model, api_key, messages, functions=functionDescriptions)

        assistant_message = chat_response.json()["choices"][0]["message"]
        messages.append(assistant_message)

        if assistant_message.get("function_call") != None :

            if assistant_message.get("content") != None :
                print(assistant_message["content"])

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
