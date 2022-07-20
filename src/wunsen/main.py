from typing import Any

from .vietnamese import ThapVi
from .japanese import ThapJa
from .korean import ThapKo
from .mandarin import ThapZh

class ThapSap:
    def __init__(self, lang: str, **setting: Any) -> None:
        """Setting
        
        :param lang: Specify language to use ('ja' Japanese |
                    'ko' Korean | 'vi' Vietnamese |
                    'zh' Standard Chinese)
        
        The rest are not required.
        
        :key str system: Specify system of transcription/
                    transliteration to use. Available system:
                    ja: 'ORS61', 'RI35' | ko: 'RI55' | vi: 'RI55' |
                    zh: 'RI49', 'THC43'
        :key str input: Specify input type
                    ja: 'Hepburn-macron', 'Hepburn-no diacritic' |
                    ko: 'RR' | vi: 'VA' | zh: 'Pinyin-number'
        :key dict option: (Standard Chinese only) Specify option
                    zh: {'sandhi': True/False} (for third tone sandhi)
        """
        if lang == 'ja':
            self._transcriber = ThapJa(**setting)
        elif lang == 'ko':
            self._transcriber = ThapKo(**setting)
        elif lang == 'vi':
            self._transcriber = ThapVi(**setting)
        elif lang == 'zh':
            self._transcriber = ThapZh(**setting)
        else:
            raise ValueError('Language not found')

    def thap(self, text: str) -> str:
        return self._transcriber.thap(text)