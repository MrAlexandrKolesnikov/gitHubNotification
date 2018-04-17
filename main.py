from notification.notification import Notification as nf
from git.git import Git
import threading
import time

branch = "master"


def worker():
    number_of_commit = Git.number_of_commit(branch)
    while True:
        if number_of_commit != Git.number_of_commit(branch):
            number_of_commit = Git.number_of_commit(branch)
            notification = nf()
            notification.rise(title='New commit',
                          subtitle=Git.get_last_commit_author(branch),
                          message=Git.get_last_commit_message(branch))
        time.sleep(30)


if __name__ == '__main__':
    t = threading.Thread(name='worker', target=worker)
    t.start()