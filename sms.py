# import package
import africastalking
# STEPS 
# In terminale:
# 1. create a virtual environment by typing: 
# 	py -3 -m venv .venv
# 2. activate virtual environment by typing:
#	.venv\scripts\activate
# 3. install africas tytping:
# 	pip install africastalking
# 4. Then run the app without debugging.



# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "7212bb7a58e71a7a935e9cd674a8a7a0ad31902f7d28ec4da3a99e80b2b63a98"      # use your sandbox app API key for development in the test environment in the Settings > API Key
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
# response = sms.send("Hello Message!", ["+254701020901"]) 
# print(response)

# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)
# Enter phone number of the recipient
sms.send("Hello Message!", ["+254797292290"], callback=on_finish)    