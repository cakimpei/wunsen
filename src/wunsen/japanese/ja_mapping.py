from copy import deepcopy

ORS61 = {

    'onset': {
        'b': ['บ', 'บ'],
        'ch': ['ช', 'จ'],
        'd': ['ด', 'ด'],
        'f': ['ฟ', 'ฟ'],
        'g': ['ก', 'ง'],
        'h': ['ฮ', 'ฮ'],
        'j': ['จ', 'จ'],
        'k': ['ค', 'ก'],
        'm': ['ม', 'ม'],
        'n': ['น', 'น'],
        'p': ['พ', 'ป'],
        'r': ['ร', 'ร'],
        's': ['ซ', 'ซ'],
        'sh': ['ช', 'ช'],
        't': ['ท', 'ต'],
        'ts': ['ซ', 'ซ'], # different pattern (short vowel)
        'v': ['ว', 'ว'], # not in royal ins
        'w': ['ว', 'ว'],
        'y': ['ย', 'ย'],
        'z': ['ซ', 'ซ']
        #'': ['อ', 'อ']
    },

    'coda': {
        'f': 'ฟ',
        'k': 'ก',
        'm': 'ม',
        'n': 'น', # or ง, ม
        'p': 'ป',
        's': 'ซ', # or ช
        't': 'ต'
    },

    'vowel': {
        'a': 'อะ', # อา (not last syllable, no coda)
        'ā': 'อา',
        'ai': 'ไอ',
        'e': 'เอะ', # เอ
        'ē': 'เอ',
        'ei': 'เอ',
        'i': 'อิ',
        'ī': 'อี',
        'o': 'โอะ', # โอ
        'ō': 'โอ',
        'u': 'อุ', # อู # อึ for tsu
        'ū': 'อู', # อือ for tsuu
        'ya': 'เอีย',
        'yā': 'เอีย',
        'yo': 'เอียว', ## delete coda
        'yō': 'เอียว',
        'yu': 'อิว', ## delete coda
        'yū': 'อีว'
    }
}

NO_DIACRITIC = {
    'aa': 'อา',
    'ee': 'เอ',
    'ii': 'อี',
    'oo': 'โอ',
    'ou': 'โอ',
    'uu': 'อู', # อือ for tsuu
    'yaa': 'เอีย',
    'yoo': 'เอียว',
    'you': 'เอียว',
    'yuu': 'อีว'
}

ORS61_NO_DIACRITIC = deepcopy(ORS61)
ORS61_NO_DIACRITIC['vowel'].update(NO_DIACRITIC)

RI35 = deepcopy(ORS61)

RI35['onset'].update({
    'ch': ['ช', 'ช']
})
del RI35['vowel']['ai']
RI35['vowel'].update({
    'ya': 'เอียะ'
})
RI35['coda'].update({
    's': 'ส'
})

RI35_NO_DIACRITIC = deepcopy(RI35)
RI35_NO_DIACRITIC['vowel'].update(NO_DIACRITIC)