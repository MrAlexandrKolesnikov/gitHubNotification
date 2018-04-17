from notification.notification import Notification as nf
from git.git import Git

if __name__ == '__main__':
    Git.get_last_commit_author("master")
    notification = nf()
    notification.rise(title='A Real Notification',
                      subtitle='with python',
                      message='Hello, this is me, notifying you!')