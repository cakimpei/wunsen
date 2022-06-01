import re
import unicodedata
from typing import Any, Dict, List

class NotVietnamese(Exception):
    pass

class SplitSyl:
    """As Vietnamese syllables are usually divided by space or hyphen,
    we will assume that the input (after the first split) has
    only one syllable.
    """
    def __init__(self, system: Dict[str, Any]) -> None:
        self.sys_dict = system

    def split_syl(self, syl) -> List[str]:
        self.syl = unicodedata.normalize('NFC', syl.lower())
        self.find_structure()
        self.find_tone()
        self.check_vowel()
        return [self.onset, self.vowel, self.coda, self.tone]

    def find_structure(self) -> None:
        pattern = f'({self.find_onset_pattern()}|{self.find_coda_pattern()})'
        expression = re.compile(pattern)
        split = re.split(expression, self.syl)
        
        self.onset = split[1]
        self.vowel = split[2]
        self.coda = split[3]

    def find_onset_pattern(self) -> str:
        onset_pattern = '|^'.join(sorted(
            self.sys_dict['onset'],
            key=lambda onset_char: len(onset_char),
            reverse=True))
        onset_pattern = f'^{onset_pattern}'
        return onset_pattern

    def find_coda_pattern(self) -> str:
        coda_pattern = '$|'.join(sorted(
            self.sys_dict['coda'],
            key=lambda coda_char: len(coda_char),
            reverse=True))
        coda_pattern = f'{coda_pattern}$'
        return coda_pattern

    def find_tone(self) -> None:
        self.tone = ''
        self.vowel = unicodedata.normalize('NFD', self.vowel)
        pattern = re.compile('|'.join(self.sys_dict['tone']))
        finding = re.search(pattern, self.vowel)
        if finding:
            self.vowel = self.vowel.replace(finding.group(0), '')
            self.tone = finding.group(0)
        self.vowel = unicodedata.normalize('NFC', self.vowel)
    
    def check_vowel(self) -> None:
        if self.vowel not in self.sys_dict['vowel']:
            raise NotVietnamese