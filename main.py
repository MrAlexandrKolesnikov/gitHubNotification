import os
from notification.notification import Notification as nf


if __name__ == '__main__':
    notification = nf()
    notification.rise(title='A Real Notification',
           subtitle='with python',
           message='Hello, this is me, notifying you!')