import re

from khanaa import SpellWord

from .vi_mapping import RI55
from .vi_splitter import NotVietnamese, SplitSyl

_VI_ALPHABET = (r'a-zA-Zàáãạảăắằẳẵặâấầẩẫậèéẹẻẽêềếểễệđìíĩỉịòóõọỏôốồổỗộơớờởỡợ'
    r'ùúũụủưứừửữựỳỵỷỹýÀÁÃẠẢĂẮẰẲẴẶÂẤẦẨẪẬÈÉẸẺẼÊỀẾỂỄỆĐÌÍĨỈỊÒÓÕỌỎÔỐỒỔỖỘƠỚỜỞỠỢ'
    r'ÙÚŨỤỦƯỨỪỬỮỰỲỴỶỸÝ')

_VI_DIACRITIC = ''.join([u'\u0300', u'\u0303', u'\u0309', u'\u0301',
    u'\u0323', u'\u0302'])

_VI_ALL = ''.join(f'[{_VI_ALPHABET}{_VI_DIACRITIC}]+')

class ViRi55:

    vi_dict = RI55

    def __init__(self) -> None:
        pass

    def thap_kham(self, word: str) -> str:
        try:
            split_syl = SplitSyl(self.vi_dict)
            self.split = split_syl.split_syl(word)
        except NotVietnamese:
            return word

        self.shorten = False
        self.pref = {'clear_vowel': False, 'vowel_pair_form': {'อาย': 'อัย',
            'โอย': 'โอย'}}

        self.select_onset()
        self.select_vowel()
        self.select_coda()
        self.select_tone()
        self.tone_shorten()
        syl_info = {
            'onset': self.onset, 'vowel': self.vowel,
            'coda': self.coda, 'tone': self.tone
            }
        spell = SpellWord(**self.pref)
        result = spell.spell_out(**syl_info)
        return result

    def select_onset(self) -> None:
        self.onset = self.vi_dict['onset'][self.split[0]]
        self.check_gi(self.split[0], self.split[1])
        vowel_onset = self.vi_dict['vowel'][self.split[1]][0]
        if vowel_onset != 'อ':
            if self.split[0] == '':
                self.onset == vowel_onset
            else:
                self.onset = ''.join([self.onset, vowel_onset])

    def check_gi(self, original_onset: str, original_vowel: str) -> None:
        """Check for gi with (reduced) i as a vowel.
        
        gì should be สี่ not กี่"""
        if original_onset == 'g' and original_vowel == 'i':
            self.onset = self.vi_dict['onset']['gi']

    def select_vowel(self) -> None:
        self.vowel = self.vi_dict['vowel'][self.split[1]][1]
        if ((self.split[1] == 'a' and self.split[2] == 'nh') or
            (self.split[1] in ['ê', 'i', 'o', 'ô', 'u', 'ư', 'y'] and
            self.split[2] in ['c', 'ch', 'k', 'ng', 'nh'])):
            self.shorten = True

    def select_coda(self) -> None:
        if self.split[2] == '':
            self.coda = ''
        else:
            self.coda = self.vi_dict['coda'][self.split[2]]

    def select_tone(self) -> None:
        if self.split[3] == '':
            self.tone = ''
        else:
            self.tone = self.vi_dict['tone'][self.split[3]][0]
            if self.vi_dict['tone'][self.split[3]][1]:
                self.shorten = True

    def tone_shorten(self) -> None:
        if self.shorten == True:
            self.pref.update({'vowel_length': 'short'})

class ThapVi:
    def __init__(self, system: str = 'RI55', input: str = 'VA') -> None:
        """Setting
        
        :param system: Select thapsap system.
            - 'RI55' for the Royal Institute (2012/2555) system

        :param input: Select input type.
            - 'VA' for Vietnamese Alphabet
        """
        if system == 'RI55' and input == 'VA':
            self._transcript = ViRi55()
        else:
            raise NotAvailableSystem

    def thap(self, text: str) -> str:
        pattern = re.compile(_VI_ALL)
        def replace(match):
            return self._transcript.thap_kham(match.group())
        return re.sub(pattern, replace, text)

class NotAvailableSystem(Exception):
    pass