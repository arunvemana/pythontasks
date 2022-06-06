# dict.popitems(), dict,clear(), dict.items(), dict.fromkeyes(),dict.update(), any(), all()

from typing import Union
import re

class SampleBulitinUse:
    def __init__(self,students):
        self._dict = self.load_up(students)

    def load_up(self, students: Union[list, tuple]) -> dict:
        return dict.fromkeys(students, 0)

    def add_student(self, student: dict) -> dict:
        self._dict.update(student)
        return self._dict

    def get_info(self) -> list[tuple]:
        return self._dict.items()

    def remove_latest_student(self):
        return self._dict.popitem()

    def all_present(self, names: list) -> bool:
        present = []
        for i in self._dict.keys():
            if i in names:
                present.append(True)
            else:
                present.append(False)
        return all(present)

    def any_zero(self):
        zero = []
        for i in self._dict.values():
            if i == 0:
                zero.append(True)
            else:
                zero.append(False)
        return any(zero)

student_names = ['abc','nca','csr']
# loading up the students with default value 0 using dict.fromkeys()
sample = SampleBulitinUse(student_names)
# adding new student with dict.update()
sample.add_student({'csb':0})
# printing the listing of student using dict.items()
print(sample.get_info())
# removed newly added student with dict.popitem()
sample.remove_latest_student()
# checking again to conform is removed
print(sample.get_info())
# check with all()
print(sample.all_present(student_names))
student_names = ['abc','nca']
# check with all() for false
print(sample.all_present(student_names))
# check with any()
print(sample.any_zero())


