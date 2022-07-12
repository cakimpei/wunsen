import unittest
from wunsen import ThapSap

SANDHI_ON = {
    'ni3 hao3': 'หนี ห่าว',
    'ni3hao3': 'หนีห่าว',
    'bao3guan3 hao3': 'ป๋าวกวั๋น ห่าว',
    'lao3 bao3guan3': 'หล่าว ป๋าวกวั่น'
}

SANDHI_OFF = {
    'ni3 hao3': 'หนี่ ห่าว',
    'ni3hao3': 'หนี่ห่าว',
    'bao3guan3 hao3': 'ป่าวกวั่น ห่าว',
    'lao3 bao3guan3': 'หล่าว ป่าวกวั่น'
}

RI49_GENERAL = {
    'กขคงzhong1': 'กขคงจง',
    'zai4jian4': 'ไจ้เจี้ยน',
    '[[zai4jian4]]': '[[ไจ้เจี้ยน]]',
    '55 a1 a23 a4 a5 a6 abcd1 1': '55 อา a23 อ้า อะ a6 abcd1 1',
    'ben3r5': 'เปิ่น'
}

RI49_EXAMPLE = {
    'ba1': 'ปา',
    'can2': 'ฉาน',
    'cang1': 'ชาง',
    'cha2': 'ฉา',
    'chi1': 'ชือ',
    'da4': 'ต้า',
    'fen2': 'เฝิน',
    'fan4': 'ฟั่น',
    'ge1': 'เกอ',
    'hao3': 'ห่าว',
    'he1': 'เฮอ',
    'jiang1': 'เจียง',
    'kui2': 'ขุย',
    'kan4': 'คั่น',
    'lai2': 'หลาย',
    'ma1': 'มา',
    'nan2': 'หนาน',
    'pa2': 'ผา',
    'po1': 'พัว',
    'qian2': 'เฉียน',
    'qiang1': 'เชียง',
    'ren2': 'เหริน',
    'san1': 'ซาน',
    'sao3': 'ส่าว',
    'sheng2': 'เฉิง',
    'shu1': 'ชู',
    'Tang2': 'ถาง',
    'ta1': 'ทา',
    'wan4': 'วั่น',
    'wo3': 'หวั่ว',
    'wu3': 'อู่',
    'xiang1': 'เซียง',
    'xie2': 'เสีย',
    'yin2': 'หยิน',
    'yi1': 'อี',
    'zou3': 'โจ่ว',
    'zhan4': 'จั้น',
    
    'ma5': 'หมะ',
    'ma1': 'มา',
    'tai4': 'ไท่',
    'mai3': 'หม่าย',
    'kan4': 'คั่น',
    'lan2': 'หลาน',
    'chang4': 'ชั่ง',
    'chang2': 'ฉาง',
    'bao4': 'เป้า',
    'gao1': 'กาว',
    'le4': 'เล่อ',
    'ye4': 'เย่',
    # 'ê2': 'เอ๋',
    'fei1': 'เฟย์',
    'ben3': 'เปิ่น',
    'deng3': 'เติ่ง',
    'er4': 'เอ้อร์',
    'ni3': 'หนี่',
    'er2zi5': 'เอ๋อร์จึ',
    'shi3': 'ฉื่อ',
    'jia1': 'เจีย',
    'tian1': 'เทียน',
    'niang2': 'เหนียง',
    'biao3': 'เปี่ยว',
    'jie4': 'เจี้ย',
    'lin2': 'หลิน',
    'ding1': 'ติง',
    'xiong1': 'ซฺยง',
    'xiong2': 'สฺยง',
    'qiong2': 'ฉฺยง',
    'jiong3': 'จฺย่ง',
    'niu2': 'หนิว',
    'mo1': 'มัว',
    'o1yo1': 'โอโย',
    'long2': 'หลง',
    'lou2': 'โหลว',
    'bu4': 'ปู้',
    'yu2': 'ยฺหวี',
    'nü3': 'นฺหวี่',
    'gua1': 'กวา',
    'guai1': 'กวาย',
    'duan4': 'ตวั้น',
    'quan4': 'เชฺวี่ยน',
    'guang1': 'กวาง',
    'yue4': 'เยฺว่',
    'nüe4': 'เนฺว่',
    'hui2': 'หุย',
    'dun4': 'ตุ้น',
    'yun2': 'ยฺหวิน',
    'guo2': 'กั๋ว'
}

RI49_COUNTRIES = {"""wen2lai2
jian3pu3zhai4
yin4ni2
lao3wo1
ma3lai2xi1ya4
mian3dian4
fei1lü4bin1
xin1jia1po1
tai4guo2
yue4nan2""":
"""เหวินหลาย
เจี๋ยนผู่ไจ้
ยิ่นหนี
หล่าววัว
หม่าหลายซีย่า
เหมี่ยนเตี้ยน
เฟย์ลฺวี่ปิน
ซินเจียพัว
ไท่กั๋ว
เยฺว่หนาน"""
}

THC43_GENERAL = {
    'กขคงzhong1': 'กขคงจง',
    'zai4jian4': 'ไจ้เจี้ยน',
    '[[zai4jian4]]': '[[ไจ้เจี้ยน]]',
    '55 a1 a23 a4 a5 a6 abcd1 1': '55 อา a23 อ้า อา a6 abcd1 1',
    'ben3r5': 'เปิ่นร์'
}

THC43_EXAMPLE = {
    'ba1': 'ปา',
    'pa1': 'พา',
    'ma1': 'มา',
    'fa1': 'ฟา',
    'da1': 'ตา',
    'ta1': 'ทา',
    'na1': 'นา',
    'la1': 'ลา',
    'zi1': 'จือ',
    'ci1': 'ชือ',
    'si1': 'ซือ',
    'zhi1': 'จือ',
    'chi1': 'ชือ',
    'shi1': 'ซือ',
    'ji1': 'จี',
    'qi1': 'ชี',
    'xi1': 'ซี',
    'ri4': 'รื่อ',
    'ga1': 'กา',
    'ka1': 'คา',
    'ha1': 'ฮา',

    'ba4': 'ป้า',
    'bo4': 'ปั้ว',
    'bai4': 'ไป้',
    'bei4': 'เป้ย',
    'bao4': 'เป้า',
    'pou3': 'โผ่ว',
    'ban4': 'ปั้น',
    'ben4': 'เปิ้น',
    'bang4': 'ปั้ง',
    'beng4': 'เปิ้ง',
    'bi4': 'ปี้',
    'biao4': 'เปี้ยว',
    'bie4': 'เปี้ย',
    'miu4': 'มิ่ว',
    'bian4': 'เปี้ยน',
    'bin4': 'ปิ้น',
    'bing4': 'ปิ้ง',
    'bu4': 'ปู้',

    'de2': 'เต๋อ',
    'dong1': 'ตง',
    'duo1': 'ตัว',
    'dui1': 'ตุย',
    'duan1': 'ตวน',
    'dun1': 'ตุน',

    'jia3': 'จย่า',
    'jiang3': 'เจี่ยง',
    'jiong3': 'จย่ง',
    'zhu1': 'จู',
    'zhua1': 'จวา',
    'zhuo1': 'จัว',
    'zhuai1': 'ไจว',
    'zhui1': 'จุย',
    'zhuan1': 'จวน',
    'zhun1': 'จุน',
    'zhuang1': 'จวง',
    'ju1': 'จีว์',
    'jue1': 'เจวีย',
    'juan1': 'เจวียน',
    'jun1': 'จวิน',
    
    'a1': 'อา',
    'e1': 'เออ',
    'er2': 'เอ๋อร์',
    'ai1': 'ไอ',
    'ao1': 'เอา',
    'ou1': 'โอว',
    'an1': 'อาน',
    'en1': 'เอิน',
    'ang1': 'อัง',
    'yi2': 'อี๋',
    'ya2': 'หยา',
    'yao2': 'เหยา',
    'ye2': 'เหยีย',
    'you2': 'โหยว',
    'yan2': 'เหยียน',
    'yin2': 'อิ๋น',
    'yang2': 'หยัง',
    'ying2': 'อิ๋ง',
    'yong2': 'หยง',
    'wu4': 'อู้',
    'wa4': 'ว่า',
    'wo4': 'วั่ว',
    'wai4': 'ไว่',
    'wei4': 'เว่ย',
    'wan4': 'วั่น',
    'wen4': 'เวิ่น',
    'wang4': 'วั่ง',
    'weng4': 'เวิ่ง',
    'yu4': 'อี้ว์',
    'yue4': 'เย่ว์',
    'yuan4': 'ย่วน',
    'yun4': 'อวิ้น'
}

class TestSpellWord(unittest.TestCase):

    def test_sandhi_on(self):
        thap_sap = ThapSap('zh', system='RI49')
        for case in SANDHI_ON:
            self.assertEqual(thap_sap.thap(case), SANDHI_ON[case])

    def test_sandhi_off(self):
        thap_sap = ThapSap('zh', system='RI49', option={'sandhi': False})
        for case in SANDHI_OFF:
            self.assertEqual(thap_sap.thap(case), SANDHI_OFF[case])

    def test_ri49_general(self):
        thap_sap = ThapSap('zh', system='RI49')
        for case in RI49_GENERAL:
            self.assertEqual(thap_sap.thap(case), RI49_GENERAL[case])

    def test_ri49_example(self):
        thap_sap = ThapSap('zh', system='RI49')
        for case in RI49_EXAMPLE:
            self.assertEqual(thap_sap.thap(case), RI49_EXAMPLE[case])

    def test_countries(self):
        thap_sap = ThapSap('zh', system='RI49')
        for case in RI49_COUNTRIES:
            self.assertEqual(thap_sap.thap(case), RI49_COUNTRIES[case])

    def test_thc43_general(self):
        thap_sap = ThapSap('zh', system='THC43')
        for case in THC43_GENERAL:
            self.assertEqual(thap_sap.thap(case), THC43_GENERAL[case])

    def test_thc43_example(self):
        thap_sap = ThapSap('zh', system='THC43')
        for case in THC43_EXAMPLE:
            self.assertEqual(thap_sap.thap(case), THC43_EXAMPLE[case])

if __name__ == '__main__':
    unittest.main()