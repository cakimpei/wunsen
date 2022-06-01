import re
from typing import List, Pattern
import unicodedata

from khanaa import SpellWord

from wunsen.splitutils.splitter import SplitSyl, NotInDict
from wunsen.splitutils.exception import NotAvailableSystem
from .ja_mapping import ORS61, ORS61_NO_DIACRITIC

class JaRs61:

    def __init__(self, input: str) -> None:
        self.ja_dict = ORS61
        if input == 'Hepburn-no diacritic':
            self.ja_dict = ORS61_NO_DIACRITIC

    def thap_kham(self, word: str) -> str:
        try:
            splitter = SplitSyl(self.ja_dict)
            word = unicodedata.normalize('NFC', word)
            self.split = splitter.split_syl(word)
        except NotInDict:
            return word
        self.last_syl_index = len(self.split) - 1
        self.split = self.adapt_split(self.split, self.last_syl_index)
        thai_transcript = []
        for index, syl in enumerate(self.split):
            self.pref = {}
            syl_info = {
                'onset': self.select_onset(index, syl),
                'vowel': self.select_vowel(index, syl),
                'coda': self.select_coda(index, syl)
                }
            spell = SpellWord(**self.pref)
            thai_transcript.append(spell.spell_out(**syl_info))
        return ''.join(thai_transcript)

    @staticmethod
    def adapt_split(
            old_syl: List[List[str]],
            last_syl_index: int) -> List[List[str]]:
        new_split = []
        for index, syl in enumerate(old_syl):
            new_syl = syl
            # ya = ยา not เอีย, เยีย
            if new_syl[0] == '' and new_syl[1][0] == 'y':
                new_syl = ['y', new_syl[1][1:], new_syl[2]]
            # mitsu = มิตสึ
            if (index != last_syl_index
                    and new_syl[2] == ''
                    and old_syl[index+1][0] == 'ts'):
                new_syl[2] = 't'
            if (new_syl[1] in ['yo', 'yoo', 'you', 'yu', 'yuu', 'yō', 'yū']
                    and new_syl[2] != ''):
                new_syl[2] = ''
            new_split.append(new_syl)
        return new_split

    def select_onset(self, index: int, syl: List[str]) -> str:
        if syl[0] == '':
            onset = 'อ'
        elif syl[0] == 'ts' and syl[1] == 'u':
            onset = 'ส'
        else:
            if index == 0:
                onset = self.ja_dict['onset'][syl[0]][0]
            else:
                onset = self.ja_dict['onset'][syl[0]][1]
        return onset

    def select_vowel(self, index: int, syl: List[str]) -> str:
        if syl[0] == 'ts' and syl[1] in ['u', 'uu', 'ū']:
            if syl[1] == 'u':
                vowel = 'อึ'
            elif syl[1] in ['uu', 'ū']:
                vowel = 'อือ'
        else:
            vowel = self.ja_dict['vowel'][syl[1]]
            if (syl[1] in ['a', 'e', 'o', 'u']
                    and syl[2] == ''
                    and index != self.last_syl_index):
                self.pref.update({'vowel_length': 'long'})
        return vowel

    def select_coda(self, index: int, syl: List[str]) -> str:
        if syl[2] == '':
            coda = ''
        elif syl[2] == 's':
            coda = self.select_coda_s(index, syl)
        elif syl[2] == 'n':
            coda = self.select_coda_n(index, syl)
        else:
            coda = self.ja_dict['coda'][syl[2]]
        return coda

    def select_coda_s(self, index: int, syl: List[str]) -> str:
        if (index != self.last_syl_index
                and self.split[index+1][0] == 'sh'):
            coda = 'ช'
        else:
            coda = self.ja_dict['coda'][syl[2]]
        return coda

    def select_coda_n(self, index: int, syl: List[str]) -> str:
        if index == self.last_syl_index:
            coda = 'ง'
            return coda
        next_onset = self.split[index+1][0]
        if next_onset == '':
            coda = 'ง'
        elif next_onset in ['g', 'k', 'h', 'f', 'w', 'y']:
            coda = 'ง'
        elif next_onset in ['b', 'm', 'p']:
            coda = 'ม'
        else:
            coda = self.ja_dict['coda'][syl[2]]
        return coda

class ThapJa:

    def __init__(
            self, system: str = 'ORS61',
            input: str = 'Hepburn-macron') -> None:
        """Setting
        
        :param system: Select thapsap system.
            - 'ORS61' for the Office of the Royal Society (2018/2561)
            system

        :param input: Select input type.
            - 'Hepburn-macron' for Hepburn romanization with macron
            (ex. arigatō)
            - 'Hepburn-no diacritic' for Hepburn romanization
            without diacritic (ex. arigatou)
        """
        if system == 'ORS61':
            self.transcript = JaRs61(input)
        else:
            raise NotAvailableSystem

    def thap(self, text: str) -> str:
        def find_expression() -> Pattern[str]:
            char_list = ''.join(['a-zA-ZāēīōūĀĒĪŌŪ', u'\u00af'])
            exp = f"([{char_list}]|(?<=[{char_list}])'(?=[{char_list}]))+"
            return re.compile(exp)
        def replace(match):
            return self.transcript.thap_kham(match.group())
        return re.sub(find_expression(), replace, text)