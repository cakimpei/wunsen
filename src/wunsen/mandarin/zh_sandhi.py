import re
from typing import Any, Dict, List, Tuple

from wunsen.splitutils.splitter import NotInDict
from .zh_splitter import SplitZh

SPLIT_EXP = re.compile(r'([A-Za-zü0-9]+)')

class AlterThird:
    def __init__(self, sys_dict: Dict[str, Any]):
        self.sys_dict = sys_dict

    def third_alter(self, text: str) -> str:
        self.original = re.split(SPLIT_EXP, text)
        self.words = [y for x, y in enumerate(self.original) if x % 2 != 0]
        self.not_words = [y for x, y in enumerate(self.original) if x % 2 == 0]

        valids, valids_tone = self.split_word()
        new_tone = self.alter_third(valids_tone)
        new_valids = self.merge_new_tone(valids, new_tone)

        return self.merge_all(new_valids)

    def split_word(self) -> Tuple[List[List[List[str]]], List[List[int]]]:
        valids = []
        valids_tone = []
        splitter = SplitZh(self.sys_dict)
        splitter.sys_dict = self.sys_dict
        for word in self.words:
            try:
                split = splitter.split_syl(word)
                if split:
                    valids.append(split)
                    valids_tone.append([x[2] for x in split])
            except NotInDict:
                valids.append([])
                valids_tone.append([])
        return valids, valids_tone

    def alter_third(self, valids_tone: List[List[int]]) -> List[List[int]]:
        reversed_tone = self.tone_reverse(valids_tone)
        new_reversed_tone = []
        for index, word_group in enumerate(reversed_tone):
            if not word_group:
                new_reversed_tone.append(word_group)
            else:
                if index == 0:
                    third = False
                else:
                    third = self.check_third(new_reversed_tone[-1])
                new_syl, third = self.alter_inner_third(word_group, third)
                new_reversed_tone.append(new_syl)
        new_tone = self.tone_reverse(new_reversed_tone)
        return new_tone

    @staticmethod
    def alter_inner_third(
            word_group: List[int],
            third: bool) -> Tuple[List[int], bool]:
        new_syl = []
        for syl in word_group:
            tone = syl
            if syl == 3:
                if third == True:
                    tone = 2
                third = True
            else:
                third = False
            new_syl.append(tone)
        return new_syl, third

    @staticmethod
    def tone_reverse(tones: List[List[int]]) -> List[List[int]]:
        tones = [list(reversed(sublist)) for sublist in reversed(tones)]
        return tones

    @staticmethod
    def check_third(tones: List[int]) -> bool:
        return tones and tones[-1] == 3

    @staticmethod
    def merge_new_tone(
            valids: List[List[List[str]]],
            new_tone: List[List[int]]) -> List[List[List[str]]]:
        new_valids = []
        for index, valid in enumerate(valids):
            new_valid = []
            if valid:
                for syl_index, syl in enumerate(valid):
                    new_syl = syl
                    new_syl[2] = new_tone[index][syl_index]
                    new_valid.append(new_syl)
            new_valids.append(new_valid)
        return new_valids

    def merge_all(self, new_valids: List[List[List[str]]]) -> str:
        new_text = [self.not_words[0]]
        for index, valid in enumerate(new_valids):
            if not valid:
                new_text.append(self.words[index])
            else:
                new_valid = []
                for syl in valid:
                    new_valid.append(''.join([str(char) for char in syl]))
                new_text.append(''.join(new_valid))
            new_text.append(self.not_words[index+1])
        new_text = ''.join(new_text)
        return new_text