import re
from typing import Any, Dict, List, Pattern, Tuple

class NotInDict(Exception):
    pass

class SplitSyl:
    def __init__(self, transcription_dict: Dict[str, Any]):
        self.ts_dict = transcription_dict

    def split_syl(self, word: str) -> List[List[str]]:
        word = word.lower()
        group_split = SplitSyl.grouping(SplitSyl.split_vowel(self, word), 2)
        con_exp = self.find_con_exp()
        result = []

        for syl in group_split[:-1]:
            con_split = SplitSyl.split_con(self, con_exp, syl[0])
            con_split = SplitSyl.find_coda_onset(self, con_split)
            result.extend([con_split[0], con_split[1], syl[1]])

        SplitSyl.check_coda(self, group_split[-1][0])
        result.append(group_split[-1][0])
        SplitSyl.check_first(result)
        del result[0]
        return SplitSyl.grouping(result, 3)

    @staticmethod
    def grouping(list: List[str], group_length: int) -> List[List[str]]:
        return [list[i:i+group_length]
            for i in range(0, len(list), group_length)]

    def split_vowel(self, word: str) -> List[str]:
        vowel_pattern = '|'.join(sorted(
            self.ts_dict['vowel'],
            key=lambda x: len(x),
            reverse=True))
        vowel_pattern = f'({vowel_pattern})'

        expression = re.compile(vowel_pattern)

        return re.split(expression, word)

    def find_con_exp(self) -> Pattern[str]:
        all_onset = '$|'.join(sorted(self.ts_dict['onset'],
            key=lambda con: len(con), reverse=True))
        con_pattern = rf'({all_onset}$)'
        return re.compile(con_pattern)

    def split_con(self, con_pattern: Pattern[str], con: str) -> List[str]:
        if con == '' or con == "'":
            return ['', '']
        elif con.find("'") != -1:
            return SplitSyl.comma_case(self, con)
        else:
            con_split = re.split(con_pattern, con)
            con_split = [found for found in con_split if found]
            return con_split

    def comma_case(self, con: str) -> List[str]:
        parts = con.partition("'")
        if ((parts[0] == ''
                or parts[0] in self.ts_dict['coda'])
                and (parts[2] == ''
                or parts[2] in self.ts_dict['onset'])):
            return [parts[0], parts[2]]
        else:
            raise NotInDict

    def find_coda_onset(self, con_split: List[str]) -> Tuple[str, str]:
        if len(con_split) > 2:
            raise NotInDict
        elif len(con_split) == 2:
            if (con_split[0] != ''
                    and con_split[0] not in self.ts_dict['coda']
                    or (con_split[1] != ''
                    and con_split[1] not in self.ts_dict['onset'])):
                raise NotInDict
            coda = con_split[0]
            onset = con_split[-1]
        else:
            if (con_split[0] != ''
                    and con_split[0] not in self.ts_dict['onset']):
                if con_split[0] not in self.ts_dict['coda']:
                    raise NotInDict
                else:
                    coda = con_split[0]
                    onset = ''
            else:
                coda = ''
                onset = con_split[0]
        return coda, onset

    def check_coda(self, con: str) -> None:
        if con not in self.ts_dict['coda'] and con != '':
            raise NotInDict
        else:
            return

    def check_first(syl_list: List[str]) -> None:
        if syl_list[0] != '':
            raise NotInDict
        else:
            return