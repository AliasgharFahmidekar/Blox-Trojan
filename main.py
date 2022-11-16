import os

import colorama
import requests
import time
from colorama import *

colorama.init()


class Client:
    """
    clint-side app for running external commands.
    """

    def __init__(self, addr):
        """
        constructor of the class - creating base class values.
        :param addr: address to looping for get command and run it.
        """
        self.com = None
        self.addr = addr

    def run_command(self, command):
        """
        get a command from internal function <get> to run command.
        run commands by OS library
        :param command: command for running
        :return: bool - True
        """
        if self.com is None:  # Function Started for first time
            os.system(command)
        elif self.com == command:  # Command already used
            pass
        else:
            os.system(command)  # run command with OS library
            return True

    def get(self):
        """
        Looping function for getting data
        :return: Nothing
        """
        print(Fore.BLUE + "Function-get")
        while True:
            print(Fore.GREEN + "Looping...")
            time.sleep(5)
            t = str(requests.get(self.addr).text)
            self.run_command(t)


c = Client(input(Fore.RED + "Addr? >>> "))
c.get()
