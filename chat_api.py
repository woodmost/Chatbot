import aiml
import os
from flask import Flask, jsonify, request

# initializing kernel
kernel = aiml.Kernel()

# check whether there is a pre-trained brain there or not. 
# if yes then read from brain otherwise create one.
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")


# initializing flask 
app = Flask(__name__)
app.config['DEBUG'] = False

# route path defined here
@app.route("/api/chatbot", methods=['GET'])
def get_msg_output():
    """
    this function will work once API is called.
    It finds out the message from the request and
    returns the bot reply in the json format.
    """
    response_val = {
        "status" : True
    }
    if 'message' in request.args:
        message = str(request.args['message'])

        # Quit chatbot 
        if message == "quit":
            response_val["output"] = "Bye"

        # Save chatbot
        elif message == "save":
            response_val["output"] = "Saved"
            kernel.saveBrain("bot_brain.brn")
        
        # revert response.
        else:
            response_val.update({
                'output' : kernel.respond(message)
                })

    return jsonify(response_val)


if __name__ == "__main__":
    # define your running host and ip here.
    app.run(host='0.0.0.0', port=5000)
