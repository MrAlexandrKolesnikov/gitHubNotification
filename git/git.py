import os


class Git:
    @staticmethod
    def number_of_commit(branch):
        return os.popen("git rev-list --count HEAD " + branch).read()

    @staticmethod
    def get_last_commit_author(branch):
        print(os.popen("git log " + branch + " --pretty=format:'%an'").read())