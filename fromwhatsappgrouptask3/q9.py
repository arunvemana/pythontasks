from abc import ABCMeta, abstractmethod

class SampleBaseClass(metaclass=ABCMeta):
    def __init__(self,name):
        # initial methods
        self._name = name

    @abstractmethod
    def whats_my_name(self):
        pass


class FindName(SampleBaseClass):

    def whats_my_name(self):
        return self._name


name = FindName("littlecrazy2life")
print(name.whats_my_name())