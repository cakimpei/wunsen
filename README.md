# Wunsen

Wunsen provides 'thai-ization' of different languages.

Currently support:

- Japanese (from Hepburn romanization)
- Korean (from Revised Romanization)
- Vietnamese (Latin script)

## Installation

Requirement:

Python >= 3.7

[khanaa](https://github.com/cakimpei/khanaa)

```
pip install wunsen
```

## Usage

```python
from wunsen import ThapSap

# Japanese
thap_ja = ThapSap('ja')
thap_ja.thap('ohayō')
# => 'โอฮาโย'

# without macron
thap_ja_no_macron = ThapSap('ja', input='Hepburn-no diacritic')
thap_ja_no_macron.thap('ohayou')
# => 'โอฮาโย'

# Korean
thap_ko = ThapSap('ko')
thap_ko.thap('annyeonghaseyo')
# => 'อันนย็องฮาเซโย'

# Vietnamese
thap_vi = ThapSap('vi')
thap_vi.thap('xin chào')
# => 'ซีน จ่าว'
```

## Transcription/Transliteration System in Wunsen

There might be some differences between Wunsen result and the intended result from the actual system, so please review the results.

- Japanese => หลักเกณฑ์การทับศัพท์ภาษาญี่ปุ่น (สำนักงานราชบัณฑิตยสภา พ.ศ. 2561)
- Korean => หลักเกณฑ์การทับศัพท์ภาษาเกาหลี (ราชบัณฑิตยสถาน พ.ศ. 2555)
- Vietnamese => หลักเกณฑ์การทับศัพท์ภาษาเวียดนาม (ราชบัณฑิตยสถาน พ.ศ. 2555)

### Notes

Wunsen might break syllables in incorrect place:

```python
thap_ja.thap("honya | hon'ya")
# => "โฮเนีย | ฮงยะ"

thap_ko.thap("waengwaeng, maeum | waeng'waeng, ma'eum")
# => "แว็นกแว็ง, แมอุม | แว็งแว็ง, มาอึม"
```