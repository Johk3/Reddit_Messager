import praw
from os import system

if raw_input("Theboysxx or Blazejohk\n").lower() == "theboysxx":
    reddit = praw.Reddit(client_id='WwIsoVyRgqOKmQ',
                         client_secret='tgGQkIIS6Oa8pkJP9WBKbqbXqFI',
                         password='6bEZkox56bvaXauS36nbJd14HnpzD',
                         user_agent='testscript by /u/fakebot3',
                         username='theboysxx')
    user = "Theboysxx"
else:
    reddit = praw.Reddit(client_id='NW8OLOjmojgpag',
                         client_secret='vlNBaN-UMFucIeZWM6rLRAAq_40',
                         password='johannes2003',
                         user_agent='testscript by /u/fakebot3',
                         username='blazejohk')
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
            reddit = praw.Reddit(client_id='WwIsoVyRgqOKmQ',
                                 client_secret='tgGQkIIS6Oa8pkJP9WBKbqbXqFI',
                                 password='6bEZkox56bvaXauS36nbJd14HnpzD',
                                 user_agent='testscript by /u/fakebot3',
                                 username='theboysxx')
            user = "Theboysxx"
        elif key.lower() == "exit":
            exit(0)
        else:
            reddit = praw.Reddit(client_id='NW8OLOjmojgpag',
                                 client_secret='vlNBaN-UMFucIeZWM6rLRAAq_40',
                                 password='johannes2003',
                                 user_agent='testscript by /u/fakebot3',
                                 username='blazejohk')
            user = "Blazejohk"

        system("cls")
        print("Waiting for messages as {}".format(user))




