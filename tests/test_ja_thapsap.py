import unittest
from wunsen import ThapSap

GENERAL = {
    '日本語 にほんご Nihongo นิฮงโงะ': '日本語 にほんご นิฮงโงะ นิฮงโงะ',
    'ニホンゴ123456789': 'ニホンゴ123456789',
    """uzubekisutan
kazafusutan
kirugisu
tajikisutan
torukumenisutan

indoneshia
kanbojia
shingapōru
tai
higashitimōru
firipin
burunei
betonamu
marēshia
myanmā
raosu""":
"""อูซูเบกิซูตัง
คาซาฟูซูตัง
คิรูงิซุ
ทาจิกิซูตัง
โทรูกูเมนิซูตัง

อินโดเนชิอะ
คัมโบจิอะ
ชิงงาโปรุ
ไท
ฮิงาชิติโมรุ
ฟิริปิง
บูรูเน
เบโตนามุ
มาเรชิอะ
เมียมมา
ราโอซุ"""
}

ORS61_EXAMPLE = {
    "bon'odori": "บงโอโดริ",
    "obi": "โอบิ",
    "chīsai": "ชีไซ",
    "konnichiwa": "คนนิจิวะ",
    "denwa": "เด็งวะ",
    "Edo": "เอโดะ",
    "fune": "ฟูเนะ",
    "Gifu": "กิฟุ",
    "ginkō": "กิงโก",
    "arigatō": "อาริงาโต",
    "hashi": "ฮาชิ",
    "Hiroshima": "ฮิโรชิมะ",
    "Jōmon": "โจมง",
    "kaji": "คาจิ",
    "kao": "คาโอะ",
    "niku": "นิกุ",
    "gakkō": "กักโก",
    "mado": "มาโดะ",
    "shimbun": "ชิมบุง",
    "samma": "ซัมมะ",
    "empitsu": "เอ็มปิตสึ",
    "Nagoya": "นาโงยะ",
    "kinoko": "คิโนโกะ",
    "Nippon": "นิปปง",
    "konnichiwa": "คนนิจิวะ",
    "minchō": "มินโจ",
    "jinja": "จินจะ",
    "konnichiwa": "คนนิจิวะ",
    "konnyaku": "คนเนียกุ",
    "Endō": "เอ็นโด",
    "renraku": "เร็นรากุ",
    "hontō": "ฮนโต",
    "jinzai": "จินไซ",
    "ginnan": "กินนัง",
    "ringo": "ริงโงะ",
    "ginkō": "กิงโก",
    "kokusanhin": "โคกูซังฮิง",
    "denwa": "เด็งวะ",
    "hon'ya": "ฮงยะ", # honya => โฮเนีย
    "shinsai": "ชินไซ",
    "manshū": "มันชู",
    "bon'odori": "บงโอโดริ",
    "ichiban": "อิจิบัง",
    "pen": "เพ็ง",
    "tempura": "เท็มปูระ",
    "Nippon": "นิปปง",
    "renraku": "เร็นรากุ",
    "Nara": "นาระ",
    "sakana": "ซากานะ",
    "kissaten": "คิซซาเต็ง",
    "zasshi": "ซัชชิ",
    "Shōwa": "โชวะ",
    "sashimi": "ซาชิมิ",
    "te": "เทะ",
    "migite": "มิงิเตะ",
    "matcha": "มัตจะ",
    "kitte": "คิตเตะ",
    "tsunami": "สึนามิ",
    "mittsu": "มิตสึ",
    "mitsu": "มิตสึ",
    "tsūyaku": "ซือยากุ",
    "ittsū": "อิตซือ",
    "futsū": "ฟุตซือ",
    "watashi": "วาตาชิ",
    "Fujiwara": "ฟูจิวาระ",
    "yama": "ยามะ",
    "Yayoi": "ยาโยอิ",
    "zō": "โซ",
    "mizu": "มิซุ",

    "hyaku": "เฮียกุ",
    "kyakkan": "เคียกกัง",
    "kyā": "เคีย",
    "ryokō": "เรียวโก",
    "hyotto": "เฮียวโตะ",
    "ryōri": "เรียวริ",
    "byuffe": "บิวเฟะ",
    "kyūkō": "คีวโก",
    "Ryūkyū": "รีวกีว",

    "wasabi": "วาซาบิ",
    "yama": "ยามะ",
    "gakkō": "กักโก",
    "okāsan": "โอกาซัง",
    "haiku": "ไฮกุ",

    "eki": "เอกิ",
    "fune": "ฟูเนะ",
    "denwa": "เด็งวะ",
    "onēsan": "โอเนซัง",
    "sensei": "เซ็นเซ",

    "kaki": "คากิ",
    "kin": "คิง",
    "oishī": "โออิชี",

    "ocha": "โอจะ",
    "oto": "โอโตะ",
    "konnichiwa": "คนนิจิวะ",
    "sayōnara": "ซาโยนาระ",
    "Sōseki": "โซเซกิ",
    "Ōno": "โอโนะ",

    "Kabuki": "คาบูกิ",
    "isu": "อิซุ",
    "shimbun": "ชิมบุง",
    "jūyō": "จูโย",

    "Ichirō SUZUKI": "อิจิโร ซูซูกิ",
    "Takuya KIMURA": "ทากูยะ คิมูระ"
}

ORS61_EX_NO_DIACRITIC = {
    'okaasan': 'โอกาซัง',
    'oishii': 'โออิชี',
    'juuyoo': 'จูโย',
    'oneesan': 'โอเนซัง',
    'sensei': 'เซ็นเซ',
    'sayoonara': 'ซาโยนาระ',
    'koushi': 'โคชิ'
    # koushi (ko-ushi)
    # keito (ke-ito)
    # Ishii (Ishi-i)
}

class TestSpellWord(unittest.TestCase):

    def test_general(self):
        thap_sap = ThapSap('ja')
        for case in GENERAL:
            self.assertEqual(thap_sap.thap(case), GENERAL[case])

    def test_ors61_example(self):
        thap_sap = ThapSap('ja')
        for case in ORS61_EXAMPLE:
            self.assertEqual(thap_sap.thap(case), ORS61_EXAMPLE[case])

    def test_ors61_ex_no_diacritic(self):
        thap_sap = ThapSap('ja', input='Hepburn-no diacritic')
        for case in ORS61_EX_NO_DIACRITIC:
            self.assertEqual(thap_sap.thap(case), ORS61_EX_NO_DIACRITIC[case])

if __name__ == '__main__':
    unittest.main()