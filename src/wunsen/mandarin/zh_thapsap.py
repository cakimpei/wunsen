import re
from typing import Any, Dict, List

from khanaa import SpellWord

from wunsen.splitutils.splitter import NotInDict
from wunsen.splitutils.exception import NotAvailableSystem
from .zh_splitter import SplitZh
from .zh_mapping import RI49, THC43
from .zh_sandhi import AlterThird, SPLIT_EXP

class ZhRi49:

    zh_dict = RI49
    short_forth_list = ['ai', 'an', 'ang', 'ao', 'uai', 'uang']
    aao_aang = {
        'w': ['u'],
        'y': ['i']
    }

    def __init__(self) -> None:
        pass

    def thap_kham(self, word: str) -> str:
        try:
            splitter = SplitZh(self.zh_dict)
            splitter.sys_dict = self.zh_dict
            self.split = splitter.split_syl(word)
        except NotInDict:
            return word
        result_list = []
        self.pref = {}
        spell = SpellWord(**{
            'clear_vowel': False,
            'obvious_h_low_single': False})
        for index, syl in enumerate(self.split):
            if self.is_erhua(syl):
                if len(self.split) == 1:
                    return word
                else:
                    continue
            self.is_erhua_next(index)
            self.shorten = False
            pattern = self.turn_thai(syl)
            self.select_pref(syl)
            spell.option.update(**self.pref)
            result_list.append(spell.spell_out(**pattern))

        result = ''.join(result_list)

        return result

    @staticmethod
    def is_erhua(syl: List) -> bool:
        return syl[0] == 'r' and syl[1] == ''
    
    def is_erhua_next(self, index) -> None:
        self.erhua_next = False
        if (index < len(self.split) - 1
                and self.is_erhua(self.split[index+1])):
            self.erhua_next = True

    def turn_thai(self, syl: List) -> Dict[str, Any]:
        self.select_rime(syl)
        self.select_onset(syl)
        self.select_tone(syl)
        self.short_fifth(syl)
        pattern = {
            'onset': self.onset,
            'vowel': self.rime[1],
            'silent_before': self.rime[2],
            'coda': self.rime[3],
            'tone': self.tone
        }
        if self.erhua_next:
            pattern = self.add_erhua(pattern)
        return pattern

    def select_rime(self, syl: List) -> None:
        self.rime = self.zh_dict['rime'][syl[1]]

        self.short_fourth_a(syl)

        self.rime_dict = 'rime'
        if (syl[1] in self.zh_dict['cond_rime']
                and syl[0] in self.zh_dict['cond_rime'][syl[1]]):
            self.rime = self.zh_dict['rime_cond'][syl[1]]
            self.rime_dict = 'rime_cond'

    def short_fourth_a(self, syl: List) -> None:
        if (syl[1] in self.short_forth_list
                and syl[2] == 4):
            self.shorten = True

    def select_onset(self, syl: List) -> None:
        self.onset = self.zh_dict['onset'][syl[0]]
        vowel_onset = self.zh_dict[self.rime_dict][syl[1]][0]

        if (syl[0] in self.aao_aang
                and syl[1] in self.aao_aang[syl[0]]):
            self.onset = 'อ'
        if vowel_onset != 'อ':
            if syl[0] == '':
                self.onset = vowel_onset
            else:
                self.onset = ''.join([self.onset, vowel_onset])

    def select_tone(self, syl: List) -> None:
        self.tone = self.zh_dict['tone'][syl[2]]

    def short_fifth(self, syl: List) -> None:
        if (syl[2] in [0, 5]
                and (syl[1] == 'a'
                or (syl[1] == 'i'
                and syl[0] in self.zh_dict['cond_rime'][syl[1]]))):
            self.shorten = True
            self.tone = 1

    @staticmethod
    def add_erhua(pattern: Dict[str, Any]) -> Dict[str, Any]:
        return pattern

    def select_pref(self, syl: List) -> None:
        if self.shorten == True:
            self.pref.update({'vowel_length': 'short'})
        else:
            self.pref.update({'vowel_length': 'input'})
        if (self.rime[4]
                or (self.onset == 'ฮว' and self.tone in [1, 4])):
            self.pref.update({'onset_style': 'phinthu'})
        else:
            self.pref.update({'onset_style': 'plain'})

class ZhThc43(ZhRi49):
    
    zh_dict = THC43
    short_forth_list = ['an']
    aao_aang = {
        'w': ['u'],
        'y': ['i', 'in', 'ing', 'u', 'un', 'v', 'vn']
    }

    def short_fifth(self, syl: List) -> None:
        pass

    @staticmethod
    def add_erhua(pattern: Dict[str, Any]) -> Dict[str, Any]:
        if pattern['silent_before']:
            new_silent_before = ''.join([
                pattern['silent_before'], 'ร'])
            pattern['silent_before'] = new_silent_before
        else:
            pattern.update({'silent_after': 'ร'})
        return pattern

    def select_pref(self, syl: List) -> None:
        super().select_pref(syl)
        if syl[0] == 'w' and syl[1] == 'an':
            self.pref.update({'vowel_length': 'short'})
        elif syl[1] == 'ei' and not self.erhua_next:
            self.pref.update({'silent_before_style': 'plain'})

class ThapZh:
    def __init__(
        self, system: str = 'THC43',
        input: str = 'Pinyin-number',
        option: Dict[str, Any] = {'sandhi': True}) -> None:
        """Setting
        
        :param system: Select thapsap system.
            - 'RI49' for the Royal Institute (2006/2549) system
            - 'THC43' for เกณฑ์การถ่ายทอดเสียงภาษาจีนแมนดาริน
            ด้วยอักขรวิธีไทย (2000/2543)

        :param input: Select input type.
            - 'Pinyin-number' for Hanyu Pinyin with tone number
            (ex. xie4xie5)
        
        :param option: Select option
            - for third tone sandhi
                - {'sandhi': True} for automatic third tone sandhi
                (ex. ni3 hao3 => หนีห่าว (ni2 hao3))
                - {'sandhi': False}
                (ex. ni3 hao3 => หนี่ห่าว (ni3 hao3))
        """
        if system == 'RI49' and input == 'Pinyin-number':
            self.transcript = ZhRi49()
            self.sys_dict = RI49
        elif system == 'THC43' and input == 'Pinyin-number':
            self.transcript = ZhThc43()
            self.sys_dict = THC43
        else:
            raise NotAvailableSystem
        self.option = option

    def thap(self, text: str) -> str:
        if self.option['sandhi']:
            alter_third = AlterThird(self.sys_dict)
            text = alter_third.third_alter(text)
        def replace(match):
            return self.transcript.thap_kham(match.group())
        return re.sub(SPLIT_EXP, replace, text)