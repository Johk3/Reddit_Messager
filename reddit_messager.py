import praw
from os import system

if raw_input("Theboysxx or Blazejohk\n").lower() == "theboysxx":
    reddit = praw.Reddit(client_id='id',
                         client_secret='secret',
                         password='password',
                         user_agent='testscript by /u/fakebot3',
                         username='username')
    user = "Theboysxx"
else:
    reddit = praw.Reddit(client_id='id',
                         client_secret='secret',
                         password='password',
                         user_agent='testscript by /u/fakebot3',
                         username='username')
    user = "Blazejohk"
system("cls")
print("Waiting for messages as {}".format(user))

while True:
    try:
        inbox = reddit.inbox.unread()

        for message in inbox:
            print("{}:\n{}\n\n\"{}\"".format(message.author, message.subject, message.body))
            quickreply = raw_input("\n->")
            if quickreply == "":
                continue
            else:
                message.reply(str(quickreply))
            message.mark_read()
            system("cls")
            print("Waiting for messages as {}".format(user))

    except KeyboardInterrupt:
        key = raw_input("Theboysxx or Blazejohk? Or just exit?\n")
        if key.lower() == "theboysxx":
            reddit = praw.Reddit(client_id='id',
                                 client_secret='secret',
                                 password='password',
                                 user_agent='testscript by /u/fakebot3',
                                 username='username')
            user = "Theboysxx"
        elif key.lower() == "exit":
            exit(0)
        else:
            reddit = praw.Reddit(client_id='id',
                                 client_secret='secret',
                                 password='password',
                                 user_agent='testscript by /u/fakebot3',
                                 username='username')
            user = "Blazejohk"

        system("cls")
        print("Waiting for messages as {}".format(user))




