import re
from typing import Any, Dict, List

from wunsen.splitutils.splitter import SplitSyl, NotInDict

class SplitZh(SplitSyl):
    def __init__(self, sys_dict: Dict[str, Any]) -> None:
        self.sys_dict = sys_dict

    def split_syl(self, word: str) -> List[List[str]]:
        word = word.lower()
        self.check_string(word)
        self.split_tone(word)
        self.split_rime()

        for syl in self.syls:
            self.check_rime(syl[1], syl[0])
            self.check_tone(syl[2])

        return self.syls

    @staticmethod
    def check_string(word: str) -> None:
        if not re.findall(r'[a-zü]', word):
            raise NotInDict
        else:
            return

    def split_tone(self, word: str) -> None:
        self.word = re.split(r'(\d+)', word)
        self.word = self.check_last(self.word)
        self.word = self.word[:-1]

    @staticmethod
    def check_last(syl_list: List[Any]) -> List[Any]:
        if syl_list[-1] != '':
            syl_list.extend([5, ''])
            return syl_list
        else:
            return syl_list

    def split_rime(self) -> None:

        self.syls = []
        onset_expression = re.compile(self.find_onset_pattern())

        for i, syl in enumerate(self.word):
            if i % 2 == 0:
                split_syl = re.split(onset_expression, syl)[1:]
                self.syls.extend(split_syl)
            else:
                self.syls.append(int(syl))
        
        self.syls = self.grouping(self.syls, 3)

    def find_onset_pattern(self) -> str:
        onset_pattern = '|^'.join(sorted(
            self.sys_dict['onset'],
            key=lambda chars: len(chars),
            reverse=True))
        onset_pattern = f'(^{onset_pattern})'
        return onset_pattern

    def check_rime(self, rime: str, onset: str) -> None:
        if (rime in self.sys_dict['rime']
                or (rime == '' and onset == 'r')):
            return
        else:
            raise NotInDict

    def check_tone(self, tone: str) -> None:
        if tone in self.sys_dict['tone']:
            return
        else:
            raise NotInDict