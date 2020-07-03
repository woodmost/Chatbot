# Chatbot
Chatbot Based on Python

### Requirements
    Python = 2.x.x
    Flask
    Aiml
    pip

# As per easy to run I've created a venv inside the folder.
1. Clone the whole project in /var/www/html

2. Run the command :
	$ sudo chmod -R 777 /var/www/html/Chatbot/*

3. Activate the venv
	$ cd /var/www/html/Chatbot
	$ source venv/bin/activate

4. Run the API
	$ python chat_api.py

# Getting Output
you can get output by using the curl request to url <your_ip>:5000/api/chatbot?message=<your_message>
example if you're having IP : 192.168.1.22

request for 192.168.1.22:5000/api/chatbot?message=Hello
response  --> json in which it contains a status and an output.
