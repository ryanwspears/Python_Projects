# Python Version: 3.7.8
#
# Author: Ryan Spears
#


from abc import ABC, abstractmethod

class Computer(ABC):
    def process(self, time):
        print("Remaining time in current process:", time)

    @abstractmethod
    def restart(self, time):
        pass

class Laptop(Computer):
    def restart(self, time):
        print("Time until restart: {}".format(time))


com = Laptop()
com.process("30 Seconds")
com.restart("10 Seconds")
