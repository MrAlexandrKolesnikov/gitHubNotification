import platform
from utils.utils import Executor


def mac_install():
    print("Install requirements. Please wait!")
    Executor.run(["sudo", "gem", "install", "terminal-notifier"])


def windows_install():
    print("Your os is windows")


def linux_install():
    print("Your platform is linux")


platform_map = {"Windows": windows_install, "Darwin" : mac_install, "Linux":linux_install}

if __name__ == '__main__':
    try:
        platform_map[platform.system()]()
    except KeyError:
        print("Your platform is not supported")






