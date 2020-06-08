import datetime
import json

class Channel:
    counter = 0
    def __init__(self, name):
        self.name = name
        self.messages = []
        self.id = Channel.counter
        Channel.counter += 1
    
    def add_message(self, m):
        self.messages.append(m)

    def serialize(self):
        messages = []
        for message in self.messages:
            messages.append({"text" : message.__dict__['text'],
                            "user": message.__dict__['user'], 
                            "time": message.__dict__['time'], 
                            "filename": message.__dict__['filename']})
        return messages


class Message:
    counter = 0
    def __init__(self, user, text, filename):
        self.text = text
        self.user = user
        self.time = f'{datetime.datetime.now().strftime("%X")}'
        self.filename = filename

        self.id = Message.counter
        Message.counter += 1


def serialize_channels(channels):
    serialize_channels = []
    for channel in channels:
        serialize_channels.append(channel.__dict__['name'])
    return serialize_channels


# from flask documentation: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#upload-progress-bars
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        
# general = Channel(name = 'general')
# new = Channel(name = 'new')

# print(general.__dict__['name'])
# channels = [general, new]
# print(serialize_channels(channels))



# general = Channel(name = 'general')
# message = Message(text = 'hello', user = 'parth')
# general.add_message(message)
# general.serialize()
# print(f"{general.messages_serialized}")


# example:
# parth = User(user = 'parth')
# hello = Message(user = parth, text = 'hello')
# general = Channel(name = 'general')
# general.add_message(hello)

# for message in general.messages:
#     if message.user = parth:
#         #all the messages submitted  by Parth in his channel