import os


class Git:
    @staticmethod
    def number_of_commit(branch):
        return os.popen("git rev-list --count HEAD " + branch).read()

    @staticmethod
    def get_last_commit_author(branch):
        return os.popen("git log HEAD^.." + branch + " --pretty=format:'%an'").read()

    @staticmethod
    def get_last_commit_data(branch):
        return os.popen("git log HEAD^.." + branch + " --pretty=format:'%ad'").read()

    @staticmethod
    def get_last_commit_message(branch):
        return os.popen("git log HEAD^.." + branch + " --pretty=format:'%s'").read()