# Python Version: 3.7.8
#
# Author: Ryan Spears
#

class ProtectedVar:
    def __init__(self):
        self._varProtected = 5
        self.__varPrivate = 7

    def getPrivate(self):
        print(self.__varPrivate)


objPro = ProtectedVar()
print(objPro._varProtected)

objPri = ProtectedVar()
objPri.getPrivate()
