from abc import ABCMeta
from enum import Enum

# -----------------------------
# Message Status Enum
# -----------------------------
class MessageStatus(Enum):
    SENT = 0
    DELIVERED = 1
    READ = 2

# -----------------------------
# UserService with messaging logic
# -----------------------------
class UserService(object):

    def __init__(self):
        self.users_by_id = {}  # key: user id, value: User

    def add_user(self, user_id, name, pass_hash):
        user = User(user_id, name, pass_hash)
        self.users_by_id[user_id] = user
        return user

    def remove_user(self, user_id):
        if user_id in self.users_by_id:
            del self.users_by_id[user_id]

    def send_message(self, from_user_id, to_user_id, content):
        if from_user_id not in self.users_by_id or to_user_id not in self.users_by_id:
            return False
        message = Message(message_id=101, message=content, timestamp="2024-05-20")
        message.status = MessageStatus.DELIVERED
        sender = self.users_by_id[from_user_id]
        receiver = self.users_by_id[to_user_id]
        print(f"Message sent from {sender.name} to {receiver.name}. Status: {message.status.name}")
        return True

# -----------------------------
# User class
# -----------------------------
class User(object):

    def __init__(self, user_id, name, pass_hash):
        self.user_id = user_id
        self.name = name
        self.pass_hash = pass_hash
        self.friends_by_id = {}  
        self.friend_ids_to_private_chats = {}  
        self.group_chats_by_id = {}  
        self.received_friend_requests_by_friend_id = {}  
        self.sent_friend_requests_by_friend_id = {}  

    def message_user(self, friend_id, message):
        pass

    def message_group(self, group_id, message):
        pass

# -----------------------------
# Chat classes
# -----------------------------
class Chat(metaclass=ABCMeta):

    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.users = []
        self.messages = []

class PrivateChat(Chat):

    def __init__(self, first_user, second_user):
        super(PrivateChat, self).__init__()
        self.users.append(first_user)
        self.users.append(second_user)

class GroupChat(Chat):

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

# -----------------------------
# Message class with status
# -----------------------------
class Message(object):

    def __init__(self, message_id, message, timestamp):
        self.message_id = message_id
        self.message = message
        self.timestamp = timestamp
        self.status = MessageStatus.SENT

    def update_status(self, new_status):
        self.status = new_status

# -----------------------------
# AddRequest and RequestStatus
# -----------------------------
class AddRequest(object):

    def __init__(self, from_user_id, to_user_id, request_status, timestamp):
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.request_status = request_status
        self.timestamp = timestamp

class RequestStatus(Enum):
    UNREAD = 0
    READ = 1
    ACCEPTED = 2
    REJECTED = 3
