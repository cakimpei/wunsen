from typing import Any

from .vietnamese import ThapVi
from .japanese import ThapJa
from .korean import ThapKo

class ThapSap:
    def __init__(self, lang: str, **setting: Any) -> None:
        """Setting
        
        :param lang: Specify language to use ('ja' Japanese |
                    'ko' Korean | 'vi' Vietnamese)
        
        The rest are not required.
        
        :key system: Specify system of transcription/transliteration
                    to use. Available system:
                    ja: 'ORS61' | ko: 'RI55' | vi: 'RI55'
        :key input: Specify input type
                    ja: 'Hepburn-macron', 'Hepburn-no diacritic' |
                    ko: 'RR' | vi: 'VA'
        """
        if lang == 'ja':
            self._transcriber = ThapJa(**setting)
        elif lang == 'ko':
            self._transcriber = ThapKo(**setting)
        elif lang == 'vi':
            self._transcriber = ThapVi(**setting)
        else:
            raise ValueError('Language not found')

    def thap(self, text: str) -> str:
        return self._transcriber.thap(text)