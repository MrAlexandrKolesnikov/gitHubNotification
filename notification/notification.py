import os
import platform


class Notification:
    _os = ""
    _notification_method = ""

    def __init__(self):
        _os = platform.system()
        if _os == "Darwin":
            self._notification_method = self._mac_notification
        elif _os == "Windows":
            self._notification_method = self._windows_notification

    def rise(self, title, subtitle, message):
        self._notification_method(title, subtitle, message)

    def _mac_notification(self, title, subtitle, message):
        t = '-title {!r}'.format(title)
        s = '-subtitle {!r}'.format(subtitle)
        m = '-message {!r}'.format(message)
        os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

    def _windows_notification(self, title, subtitle, message):
        print("Notification for windows in Progress")
