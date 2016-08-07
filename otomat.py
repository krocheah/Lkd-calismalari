otomat = {
    "cay" : 3,
    "kahve" : 7,
    "cikolata" : 11,
    "oreo" : 13,
    "sigara" : 17,
    "sari gazoz" : 29,
    "notebook" : 650,
    "eti ucharfliler" : 39,
    "su" : 23,
    "jelibon" : 19,
    "yumurta" : 2
}

def makine (para, gida, adet = 1, fail_silently = False):
    """Bu fonksiyon parayi alir ve gidayi verir
    Duruma gore fazla parayi soyler veya hatalari gosterir.
    fail_silently True verirseniz paranizi iade eder."""
    urunler = []
    kalan = para
    for i in range(adet):
        if gida not in otomat:
            if fail_silently:
                return para, None
            raise ValueError("Gida yok")
        miktar = otomat[gida]
        if miktar > kalan:
            if fail_silently:
                return para, None
            raise ValueError("Para Yetmedi")
        kalan -= miktar
        urunler.append(gida)
    if len(urunler) == 1:
        return kalan, urunler[0]
    else:
        return kalan, urunler

def bot(para, indis = -1):
    fiyatlar = []
    fiyatlar += otomat.values()
    siraliFiyatlar = sorted(fiyatlar)
    alinanUrunler = []

    if para == 1:
        return ("1 lira ile hiçbirşey alınamıyor.")
    elif para <= 0:
        return ("Kaç kaç kaç!!!!")
    else:
        while para >= siraliFiyatlar[0]:
            for gida, fiyat in otomat.items():
                if siraliFiyatlar[indis] == fiyat and siraliFiyatlar[indis] <= para:
                    while para >= fiyat:
                        alinanUrunler.append(makine(para, gida))
                        para -= fiyat
            indis -= 1
            bot(para, indis)
    return alinanUrunler

#sonuc = makine(2, "eti ucharfliler", 8)
sonuc = bot(4)
print(sonuc)
