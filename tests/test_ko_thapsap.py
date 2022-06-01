import unittest
from wunsen import ThapSap

GENERAL = {
    "한국말, han'gugeo, कोरियाई भाषा": '한국말, ฮันกูกอ, कोरियाई भाषा',
    'Koreanische Sprache': 'Koreanische Sprache'
}

RI55_EXAMPLE = {
    "baji": "พาจี",
    "haengbok": "แฮ็งบก",
    "bap": "พับ",
    "cheonji": "ช็อนจี",
    "Chungcheong": "ชุงช็อง",
    "kkot": "กด",
    "Daegu": "แทกู",
    "daedap": "แทดับ",
    "natgari": "นัดการี",
    # "Gangwon": "คังว็อน",
    "Hanguk": "ฮันกุก",
    "goguk": "โคกุก",
    "hobak": "โฮบัก",
    "gonghang": "คงฮัง",
    "jido": "ชีโด",
    "jujeonja": "ชูจ็อนจา",
    "bit": "พิด",
    "jjari": "จารี",
    "gajja": "คาจา",
    "kal": "คัล",
    "mankeum": "มันคึม",
    "bueok": "พูอ็อก",
    "chukha": "ชูคา",
    "kkangtong": "กังทง",
    "eokkae": "ออแก",
    "bak": "พัก",
    # "maeum": "มาอึม",
    "nonmun": "นนมุน",
    "gim": "คิม",
    "na": "นา",
    "nuna": "นูนา",
    "Namdaemun": "นัมแดมุน",
    "Gangneung": "คังนึง",
    "madang": "มาดัง",
    "pal": "พัล",
    "apeuda": "อาพือดา",
    "yeopsaram": "ย็อบซารัม",
    "iphak": "อีพัก",
    "ppallae": "ปัลแล",
    "ippal": "อีปัล",
    "ramyeon": "รามย็อน",
    "haru": "ฮารู",
    "mal": "มัล",
    "Jeolla": "ช็อลลา",
    "sada": "ซาดา",
    "saengsan": "แซ็งซัน",
    "sutso": "ซุดโซ",
    "sijang": "ชีจัง",
    "dosi": "โทชี",
    "ssal": "ซัล",
    "bulssuk": "พุลซุก",
    # "ssaetta": "แซ็ดตา",
    "Taebaek": "แทแบ็ก",
    "gita": "คีทา",
    "Hanbat": "ฮันบัด",
    "mathyeong": "มาทย็อง",
    "ttukkeong": "ตูก็อง",
    "heoritti": "ฮอรีตี",

    "ai": "อาอี",
    "nara": "นารา",
    "ap": "อับ",
    "bap": "พับ",
    "aein": "แออิน",
    "gae": "แค",
    "aengmusae": "แอ็งมูแซ",
    "naemsae": "แน็มแซ",
    "e": "เอ",
    "nemo": "เนโม",
    "enganhada": "เอ็นกันฮาดา",
    "sem": "เซ็ม",
    "eomeoni": "ออมอนี",
    "seoda": "ซอดา",
    "eonni": "อ็อนนี",
    "deoreopta": "ทอร็อบทา",
    "euro": "อือโร",
    "seuseuro": "ซือซือโร",
    # "maeum": "มาอึม",
    "ireum": "อีรึม",
    "ima": "อีมา",
    "si": "ชี",
    # "Yongin": "ยงอิน",
    "sil": "ชิล",
    "o": "โอ",
    "podo": "โพโด",
    "ot": "อด",
    "don": "ทน",
    "ugi": "อูกี",
    "dubu": "ทูบู",
    "undong": "อุนดง",
    "sul": "ซุล",

    "oeguk": "เวกุก",
    "goeroum": "คเวโรอุม",
    "oenson": "เว็นซน",
    "hoengdan": "ฮเว็งดัน",
    "uisa": "อึยซา",
    "Yeouido": "ยออีโด",
    "huin saek": "ฮีน แซ็ก", # "ฮีนแซ็ก"
    "wa": "วา",
    "gwaja": "ควาจา",
    "wang": "วัง",
    "Gwangju": "ควังจู",
    "wae": "แว",
    "dwaeji": "ทแวจี",
    # "waengwaeng": "แว็งแว็ง",
    "kkwaengnamu": "กแว็งนามู",
    "weiteo": "เวอีทอ",
    "gwebeom": "คเวบ็อม",
    "wennil": "เว็นนิล",
    "wi": "วี",
    "gwi": "ควี",
    "witsaram": "วิดซารัม",
    "swin": "ชวิน",
    "areumdawo!": "อารึมดาวอ!", # "อารึมดาวอ"
    "jwo": "ชวอ",
    "wollae": "ว็อลแล",
    "yeogwon": "ยอกว็อน",
    "yagu": "ยากู",
    "chyawo": "ชยาวอ",
    "yak": "ยัก",
    "dalgyal": "ทัลกยัล",
    "yaegi": "แยกี",
    "gyae": "คแย",
    "yejeol": "เยจ็อล",
    "sigye": "ชีกเย",
    "yennal": "เย็นนัล",
    "gyetnal": "คเย็ดนัล",
    "yeohaeng": "ยอแฮ็ง",
    "byeo": "พยอ",
    "yeonmal": "ย็อนมัล",
    "ramyeon": "รามย็อน",
    "yori": "โยรี",
    "hakgyo": "ฮักกโย",
    "yong": "ยง",
    "gongryong": "คงรยง",
    "uyu": "อูยู",
    "hyuji": "ฮยูจี",
    "yuk": "ยุก",
    "gyul": "คยุล"
}

COUNTRIES = {
    """beurunai
kambodia
indonesia
raoseu
malleisia
miyanma
pillipin
singgaporeu
taeguk
beteunam

dongtimoreu, papuanyugini

jungguk, ilbon, daehanmin'guk
oseuteureillia, indo, nyujillaendeu, reosia, miguk""":
"""พือรูนาอี
คัมโบดีอา
อินโดเนชีอา
ราโอซือ
มัลเลอีชีอา
มียันมา
พิลลีพิน
ชิงกาโพรือ
แทกุก
เพทือนัม

ทงทีโมรือ, พาพูอานยูกีนี

ชุงกุก, อิลบน, แทฮันมินกุก
โอซือทือเรอิลลีอา, อินโด, นยูจิลแล็นดือ, รอชีอา, มีกุก"""
}

class TestSpellWord(unittest.TestCase):

    def test_general(self):
        thap_sap = ThapSap('ko')
        for case in GENERAL:
            self.assertEqual(thap_sap.thap(case), GENERAL[case])

    def test_ri55_example(self):
        thap_sap = ThapSap('ko')
        for case in RI55_EXAMPLE:
            self.assertEqual(thap_sap.thap(case), RI55_EXAMPLE[case])

    def test_countries(self):
        thap_sap = ThapSap('ko')
        for case in COUNTRIES:
            self.assertEqual(thap_sap.thap(case), COUNTRIES[case])

if __name__ == '__main__':
    unittest.main()