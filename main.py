class SpellChecker:
    def __init__(self):
        self.sozlar = {
            "apple": "elma",
            "banana": "banan",
            "cherry": "cherry",
            "date": "date",
            "elderberry": "elderberry"
        }

    def tozalash(self, soz):
        soz = soz.lower()
        soz = soz.replace(" ", "")
        return soz

    def tekshirish(self, soz):
        tozalangan_soz = self.tozalash(soz)
        if tozalangan_soz in self.sozlar:
            return self.sozlar[soz]
        else:
            return soz

    def spell_check(self, matn):
        sozlar = matn.split()
        tozalangan_matn = ""
        for soz in sozlar:
            tozalangan_soz = self.tozalash(soz)
            tozalangan_matn += self.tekshirish(tozalangan_soz) + " "
        return tozalangan_matn.strip()

spell_checker = SpellChecker()
matn = "Men elma, banan va cherry istayman. Lekin men date va elderberry bilan ham tanishaman."
print(spell_checker.spell_check(matn))
```

Kodda quyidagi funksiyalar mavjud:

- `tozalash` funksiyasi sozni tozalaydi, ya'ni uni kichik harfga o'zgartiradi va bo'shliqlarni olib tashlaydi.
- `tekshirish` funksiyasi sozni so'zlar ro'yxatida qidirib topadi. Agar topilsa, unga mos keladigan so'zni qaytaradi, aks holda sozni o'zi qaytaradi.
- `spell_check` funksiyasi matnni sozlar ro'yxatida qidirib topadi va to'g'ri so'zlar bilan almashtiradi.

Kodni ishga tushirganda, matnga mos keladigan so'zlar bilan almashtiriladi.
