import re
from typing import List

from khanaa import SpellWord

from wunsen.splitutils.exception import NotAvailableSystem
from wunsen.splitutils.splitter import SplitSyl, NotInDict
from .ko_mapping import RI55

class KoRi55:

    ko_dict = RI55

    def __init__(self) -> None:
        pass

    def thap_kham(self, word: str) -> str:
        try:
            splitter = SplitSyl(self.ko_dict)
            self.split = splitter.split_syl(word)
        except NotInDict:
            return word
        thai_transcript = []
        for index, syl in enumerate(self.split):
            self.pref = {'clear_vowel_onset': 'all'}
            syl_info = {
                'onset': self.select_onset(index, syl),
                'vowel': self.select_vowel(index, syl),
                'coda': self.select_coda(syl)
            }
            spell = SpellWord(**self.pref)
            thai_transcript.append(spell.spell_out(**syl_info))
        return ''.join(thai_transcript)

    def select_onset(self, index: int, syl: List[str]) -> str:
        vowel_onset = self.ko_dict['vowel'][syl[1]][0]
        if syl[0] == '':
            return vowel_onset
        elif syl[0] == 's' and syl[1] in ['i', 'wi']:
            onset = 'ช'
        else:
            if index == 0:
                onset = self.ko_dict['onset'][syl[0]][0]
            else:
                onset = self.ko_dict['onset'][syl[0]][1]
        if vowel_onset != 'อ':
            onset = ''.join([onset, vowel_onset])
        return onset
    
    def select_vowel(self, index: int, syl: List[str]) -> str:
        if syl[1] == 'ui':
            if syl[0] == '' and index == 0:
                vowel = self.ko_dict['vowel'][syl[1]][1]
            else:
                vowel = 'อี'
        else:
            vowel = self.ko_dict['vowel'][syl[1]][1]
            if syl[2] != '':
                self.pref.update({'vowel_length': 'short'})
        return vowel

    def select_coda(self, syl: List[str]) -> str:
        if syl[2] == '':
            coda = ''
        else:
            coda = self.ko_dict['coda'][syl[2]]
        return coda

class ThapKo:
    def __init__(self, system: str = 'RI55', input: str = 'RR') -> None:
        """Setting
        
        :param system: Select thapsap system.
            - 'RI55' for the Royal Institute (2012/2555) system

        :param input: Select input type.
            - 'RR' for Revised Romanization
        """
        if system == 'RI55' and input == 'RR':
            self.transcript = KoRi55()
        else:
            raise NotAvailableSystem

    def thap(self, text: str) -> str:
        def replace(match):
            return self.transcript.thap_kham(match.group())
        return re.sub(
            r"([a-zA-Zāēīōū]|(?<=[a-zA-Zāēīōū])'(?=[a-zA-Zāēīōū]))+",
            replace, text)