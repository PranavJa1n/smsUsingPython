from flask import Flask
app = Flask(__name__)

@app.route("/sms/<msgbody>")
def sms_(msgbody):
    from twilio.rest import Client
    accountsid = input("Enter your Twilio accountsid: ")
    authtoken = input("Enter your Twilio authtoken: ")
    client = Client(accountsid,authtoken)
    from_phno = input("Enter your Twilio number: ")
    to_phno = input("Enter the phone number you want to send message to: ")
    message = client.messages.create(body = msgbody, from_ = from_phno, to = to_phno)
    return "Done"

app.run(port="80",host="0.0.0.0")
