# Wunsen

Wunsen provides 'thai-ization' of different languages.

Currently support:

- Standard Chinese (from Hanyu Pinyin)
- Japanese (from Hepburn romanization)
- Korean (from Revised Romanization)
- Vietnamese (Latin script)

Demo [here](https://wunsen.herokuapp.com/).

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

# Chinese (Pinyin with tone diacritics is not supported yet.)
thap_zh = ThapSap('zh', system='RI49')
thap_zh.thap('ni3 hao3')
# => 'หนี ห่าว'

thap_zh = ThapSap('zh', system='THC43')
thap_zh.thap('ni3 hao3')
# => 'หนี เห่า'

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

- Chinese =>
    - หลักเกณฑ์การทับศัพท์ภาษาจีน (ราชบัณฑิตยสถาน พ.ศ. 2549) 'RI49'
    - เกณฑ์การถ่ายทอดเสียงภาษาจีนแมนดารินด้วยอักขรวิธีไทย (คณะกรรมการสืบค้นประวัติศาสตร์ไทยในเอกสารภาษาจีน พ.ศ. 2543) 'THC43'
- Japanese => หลักเกณฑ์การทับศัพท์ภาษาญี่ปุ่น (สำนักงานราชบัณฑิตยสภา พ.ศ. 2561) 'ORS61'
- Korean => หลักเกณฑ์การทับศัพท์ภาษาเกาหลี (ราชบัณฑิตยสถาน พ.ศ. 2555) 'RI55'
- Vietnamese => หลักเกณฑ์การทับศัพท์ภาษาเวียดนาม (ราชบัณฑิตยสถาน พ.ศ. 2555) 'RI55'

### Notes

#### Syllabification Issues

Wunsen might break syllables in incorrect place. You might have to add apostrophe:

```python
thap_ja.thap("honya | hon'ya")
# => "โฮเนีย | ฮงยะ"

thap_ko.thap("waengwaeng, maeum | waeng'waeng, ma'eum")
# => "แว็นกแว็ง, แมอุม | แว็งแว็ง, มาอึม"
```

#### Chinese Tone Sandhi

For Standard Chinese, both Thai-ization systems specify that we should apply third tone sandhi rule to the Thai result. Wunsen will automatically apply it, but you can turn it off.

```python
thap_zh_no_sandhi = ThapSap('zh', option={'sandhi': False})
thap_zh_no_sandhi.thap('ni3 hao3')
# => 'หนี่ เห่า' / ni3 hao3

# if we turn it on
thap_zh_with_sandhi = ThapSap('zh', option={'sandhi': True})
thap_zh_with_sandhi.thap('ni3 hao3')
# => 'หนี เห่า' / ni2 hao3

thap_zh_with_sandhi.thap('ni3hao3')
# => 'หนีเห่า' / ni2hao3

# examples from wikipedia
thap_zh_with_sandhi.thap('bao3guan3 hao3')
# => 'เป๋าก๋วน เห่า' / bao2guan2 hao3

thap_zh_with_sandhi.thap('lao3 bao3guan3')
# => 'เหล่า เป๋าก่วน' / lao3 bao2guan3
```

Wunsen doesn't apply 不 (bù) and 一 (yī) tone rules as they are difficult to recognize in Pinyin.

#### Japanese long vowels

Although we should transcribe two short vowels from different origins, that are next to each other, as two short vowels (not one long vowel), Wunsen cannot cover this case entirely.

```python
thap_ja.thap("公子 kōshi | 子牛 koushi | 石井 Ishii | ただいま tadaima")
# => "公子 โคชิ | 子牛 โคอูชิ | 石井 อิชิอิ | ただいま ทาไดมะ"
# kōshi, koushi, Ishii are fine but tadaima is ta-dai-ma in Wunsen instead of ta-da-i-ma

thap_ja_no_macron.thap("公子 koushi | 子牛 koushi | 石井 Ishii | ただいま tadaima")
# => "公子 โคชิ | 子牛 โคชิ | 石井 อิชี | ただいま ทาไดมะ"
# they're transcribed as kou-shi | kou-shi | i-shii | ta-dai-ma so they're incorrect except 公子
```

#### Spacing in Thai

If we want to follow the actual transcription/transliteration system, in some cases, space between syllables or words might have to be deleted in Thai result.

For example, หลักเกณฑ์การทับศัพท์ภาษาเวียดนาม (ราชบัณฑิตยสถาน พ.ศ. 2555) (Vietnamese system) specifies that space in Vietnamese place names should be deleted, but in personal name, the space should still be there as in Vietnamese.

Because it depends on the situation, Wunsen will leave spacing as it is.