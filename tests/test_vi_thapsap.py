import unittest
from wunsen import ThapSap

GENERAL = {
    # composed form
    'tiếng Việt': 'เตี๊ยง เหวียต',
    # decomposed form
    'tiếng Việt': 'เตี๊ยง เหวียต',
    'ベトナム語': 'ベトナム語',
    '越南语': '越南语',
    'ภาษาเวียดนาม': 'ภาษาเวียดนาม',
    'Từ Hán Việt詞漢越': 'ตื่อ ฮ้าน เหวียต詞漢越'
}

RS55_EXAMPLE = {
    # 'quốc ngữ': 'โกว๊กหงือ', => กว๊กหงือ
    'ngang': 'งาง',
    'ma': 'มา',
    'câm': 'เกิม',
    'cơm': 'เกิม',
    'huyền': 'ฮเหวี่ยน',
    'mà': 'หม่า',
    'bà': 'บ่า',
    'xã': 'สา',
    'rõ': 'สอ',
    'mả': 'หมา',
    'rẻ': 'แส',
    'má': 'ม้า',
    'mát': 'ม้าต',
    'mạ': 'หมะ',
    'chị': 'จิ',
    'mạn': 'หมั่น',
    'hữu': 'หืว',
    'hưu': 'ฮืว',
    'ngoan': 'งวาน',
    'ngoãn': 'งหวาน',
    'ngoen': 'แงวน',
    'ngoẻn': 'งแหวน',
    'Hội An': 'โห่ย อาน', # 'โห่ยอาน'
    'Gia Long': 'ซา ล็อง', # 'ซาล็อง'
    'Võ Nguyên Giáp': 'หวอ เงวียน ซ้าป',
    'Bà Rịa-Vũng Tàu': 'บ่า เสียะ-หวุง เต่า', # 'บ่าเสียะ-หวุงเต่า'
    'Cao Bá Quát': 'กาว บ๊า กว๊าต', # 'กาวบ๊า-กว๊าต'
    'khuây': 'เคว็ย',
    'khuấy': 'เคว้ย',

    'bay': 'บัย',
    'các': 'ก๊าก',
    'bác': 'บ๊าก',
    'cha': 'จา',
    'thích': 'ทิก',
    'da': 'ซา',
    'dậy': 'เส่ย',
    'đình': 'ดิ่ญ',
    'gà': 'ก่า',
    'ghe': 'แก',
    'già': 'ส่า',
    'giá': 'ซ้า',
    'họ': 'เหาะ',
    'ho': 'ฮอ',
    'kể': 'เก๋',
    'khi': 'คี',
    'khỉ': 'ขี',
    'lo': 'ลอ',
    'mẹ': 'แหมะ',
    'cằm': 'กั่ม',
    'no': 'นอ',
    'ăn': 'อัน',
    'ngà': 'หง่า',
    'ông': 'อง',
    'nghi': 'งี',
    'nhà': 'หญ่า',
    'sinh': 'ซิญ',
    'nhanh': 'ญัญ',
    'khép': 'แค้ป',

    'Pháp': 'ฟ้าป',
    'phở': 'เฝอ',
    'quan': 'กวาน',
    'ra': 'ซา',
    'rổ': 'โส',
    'sư': 'ซือ',
    'sả': 'สา',
    'tôi': 'โตย',
    'bút': 'บู๊ต',
    'thu': 'ทู',
    'thả': 'ถา',
    'trà': 'จ่า',
    'vui': 'วูย',
    'xa': 'ซา',
    'xã': 'สา',
    'gì': 'สี่',

    'màn': 'หม่าน',
    'nhanh': 'ญัญ',
    'ta': 'ตา',
    'mặn': 'หมั่น',
    'tân': 'เติน',
    'em': 'แอม',
    'mẹ': 'แหมะ',
    'lệnh': 'เหล่ญ',
    'bên': 'เบน',
    'tê': 'เต',
    'lịch': 'หลิก',
    'in': 'อีน',
    'đi': 'ดี',
    'Mỹ': 'หมี',
    'xong': 'ซ็อง',
    'con': 'กอน',
    'có': 'ก๊อ',
    'sông': 'ซง',
    'bốn': 'โบ๊น',
    'cô': 'โก',
    'lớn': 'เลิ้น',
    'mở': 'เหมอ',
    'chúc': 'จุ๊ก',
    'núp': 'นู้ป',
    'tủ': 'ตู๋',
    'nhưng': 'ญึง',
    'như': 'ญือ',
    'xoong': 'ซอง',
    'lôông tôông': 'โลง โตง', # 'โลงโตง'

    'ai': 'อาย',
    'bài': 'บ่าย',
    'ao': 'อาว',
    'cao': 'กาว',
    'nhau': 'เญา',
    'sáu': 'เซ้า',
    'đâu': 'เดิว',
    'cay': 'กัย',
    'cây': 'เก็ย',
    'mèo': 'แหม่ว',
    'đều': 'เด่ว',
    'bia': 'เบีย',
    'tiếng': 'เตี๊ยง',
    'dìu': 'สี่ว',
    'dịu': 'สิ่ว',
    'hoa': 'ฮวา',
    'hoặc': 'ฮหวัก',
    'khoét': 'แคว้ต',
    'nói': 'น้อย',
    'tôi': 'โตย',
    'chơi': 'เจย',
    'mua': 'มัว',
    'đưa': 'เดือ',
    'xuân': 'ซวน',
    'thuê': 'เทว',
    'vui': 'วูย',
    'gửi': 'กื๋ย',
    'buồn': 'บ่วน',
    'thuở': 'ถัว',
    'đường': 'เดื่อง',
    'hưu': 'ฮืว',
    'quý': 'กวี๊',
    'kiểu': 'เกี๋ยว',
    'yếu': 'เอี๊ยว',
    'ngoài': 'งหว่าย',
    'ngoao': 'งวาว',
    'ngoáy': 'งวั้ย',
    'khuấy': 'เคว้ย',
    'khuây': 'เคว็ย',
    'muối': 'ม้วย',
    'tuổi': 'ต๋วย',
    'nuôi': 'นวย',
    'khuya': 'เควีย',
    'duyên': 'เซวียน',
    'khuỷu': 'ขวีว',
    'tươi': 'เตือย',
    'hươu': 'เฮือว',
    'rượu': 'เสื่อว'
}

COUNTRIES = {"""Hiệp hội các quốc gia Đông Nam Á:
    - Nhà nước Brunei Darussalam
    - Vương quốc Campuchia
    - Cộng hòa Indonesia
    - Cộng hoà Dân chủ Nhân dân Lào
    - Liên bang Malaysia
    - Cộng hòa Liên bang Myanmar
    - Cộng hòa Philippines
    - Cộng hòa Singapore
    - Vương quốc Thái Lan
    - Cộng hòa Xã hội chủ nghĩa Việt Nam
    """:
    """เหียป โห่ย ก๊าก กว๊ก ซา ดง นาม อ๊า:
    - หญ่า เนื้อก Brunei Darussalam
    - เวือง กว๊ก Campuchia
    - ก่ง ฮหว่า Indonesia
    - ก่ง ฮหว่า เซิน จู๋ เญิน เซิน หล่าว
    - เลียน บาง Malaysia
    - ก่ง ฮหว่า เลียน บาง Myanmar
    - ก่ง ฮหว่า Philippines
    - ก่ง ฮหว่า Singapore
    - เวือง กว๊ก ท้าย ลาน
    - ก่ง ฮหว่า สา โห่ย จู๋ เหงีย เหวียต นาม
    """
}

class TestSpellWord(unittest.TestCase):

    def test_general(self):
        thap_sap = ThapSap('vi')
        for case in GENERAL:
            self.assertEqual(thap_sap.thap(case), GENERAL[case])

    def test_rs55_example(self):
        thap_sap = ThapSap('vi')
        for case in RS55_EXAMPLE:
            self.assertEqual(thap_sap.thap(case), RS55_EXAMPLE[case])

    def test_countries(self):
        thap_sap = ThapSap('vi')
        for case in COUNTRIES:
            self.assertEqual(thap_sap.thap(case), COUNTRIES[case])

if __name__ == '__main__':
    unittest.main()