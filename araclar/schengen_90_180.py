#!/usr/bin/env python3
"""Schengen 90/180 hesaplayıcı.

Kaynak: takip/schengen-90-180.md içindeki "Seyahatler" tablosu.
Kullanım:
  python3 araclar/schengen_90_180.py            # bugünkü durum
  python3 araclar/schengen_90_180.py 2027-01-10 # o tarihteki durum
  python3 araclar/schengen_90_180.py --xlsx cikti.xlsx  # Google Sheets'e yüklenecek tablo

Kural: herhangi bir günde, o gün dahil son 180 günde Schengen'de geçen gün
sayısı 90'ı geçemez. Giriş ve çıkış günleri tam gün sayılır.
"""
import re
import sys
from datetime import date, timedelta
from pathlib import Path

TAKIP = Path(__file__).resolve().parent.parent / "takip" / "schengen-90-180.md"
SINIR, PENCERE = 90, 180


def seyahatleri_oku(yol=TAKIP):
    """Tablodaki satırlar: | giriş | çıkış | ülke | nasıl | not |  (çıkış boşsa hâlâ içeride)."""
    satirlar = []
    for line in yol.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(\d{4}-\d{2}-\d{2})?\s*\|", line)
        if m:
            g = date.fromisoformat(m.group(1))
            c = date.fromisoformat(m.group(2)) if m.group(2) else None
            satirlar.append((g, c))
    return satirlar


def gun_kumesi(seyahatler, bugun):
    gunler = set()
    for g, c in seyahatler:
        son = c or bugun
        d = g
        while d <= son:
            gunler.add(d)
            d += timedelta(days=1)
    return gunler


def kullanilan(gunler, gun):
    bas = gun - timedelta(days=PENCERE - 1)
    return sum(1 for d in gunler if bas <= d <= gun)


def en_gec_cikis(seyahatler, bugun):
    """Bugün içerideysen kalmaya, dışarıdaysan bugün girmeye devam edersen
    kuralı bozmadan kalabileceğin son gün. None: bugün giremezsin."""
    gecmis = {d for d in gun_kumesi(seyahatler, bugun) if d < bugun}
    son_iyi = None
    d = bugun
    while True:
        gecmis.add(d)
        if kullanilan(gecmis, d) > SINIR:
            return son_iyi
        son_iyi = d
        d += timedelta(days=1)


def ozet(bugun=None):
    bugun = bugun or date.today()
    s = seyahatleri_oku()
    gunler = gun_kumesi(s, bugun)
    k = kullanilan(gunler, bugun)
    iceride = any(c is None or g <= bugun <= c for g, c in s if g <= bugun)
    return {
        "bugun": bugun,
        "pencere_basi": bugun - timedelta(days=PENCERE - 1),
        "kullanilan": k,
        "kalan": SINIR - k,
        "iceride": iceride,
        "en_gec_cikis": en_gec_cikis(s, bugun),
    }


def xlsx_yaz(cikti):
    """Formüllü tablo: satır eklendikçe Google Sheets kendisi hesaplar."""
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.worksheet.datavalidation import DataValidation

    s = seyahatleri_oku()
    notlar = {}
    for line in TAKIP.read_text(encoding="utf-8").splitlines():
        p = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(p) >= 5 and re.match(r"\d{4}-\d{2}-\d{2}$", p[0]):
            notlar[p[0]] = p[2:5]

    wb = Workbook()
    oz = wb.active
    oz.title = "Özet"
    sy = wb.create_sheet("Seyahatler")
    tk = wb.create_sheet("Hesap")
    N = 300  # seyahat satırı kapasitesi
    bold = Font(bold=True)
    head_fill = PatternFill("solid", fgColor="DDE7F0")

    # Seyahatler
    basliklar = ["Giriş", "Çıkış (içerideysen boş)", "Ülke", "Nasıl", "Not",
                 "Gün", "Son 180 günde sayılan", "_bitiş (hesap)"]
    for i, b in enumerate(basliklar, 1):
        c = sy.cell(1, i, b)
        c.font, c.fill = bold, head_fill
    for r, (g, c) in enumerate(s, 2):
        sy.cell(r, 1, g)
        if c:
            sy.cell(r, 2, c)
        ulke, nasil, notu = notlar.get(g.isoformat(), ["", "", ""])
        sy.cell(r, 3, ulke)
        sy.cell(r, 4, nasil)
        sy.cell(r, 5, notu)
    for r in range(2, N + 2):
        sy.cell(r, 6, f'=IF(A{r}="","",IF(B{r}="",TODAY(),B{r})-A{r}+1)')
        sy.cell(r, 7, f'=IF(A{r}="","",MAX(0,MIN(IF(B{r}="",TODAY(),B{r}),TODAY())'
                      f'-MAX(A{r},TODAY()-179)+1))')
        # geçmiş günler bugünden önce kesilir; "bugün" Hesap sekmesinde ayrıca sayılır
        sy.cell(r, 8, f'=IF(A{r}="",0,MIN(IF(B{r}="",TODAY(),B{r}),TODAY()-1))')
        for col in (1, 2):
            sy.cell(r, col).number_format = "DD.MM.YYYY"
    dv = DataValidation(type="list", formula1='"Uçak,Araba,Otobüs,Diğer"', allow_blank=True)
    sy.add_data_validation(dv)
    dv.add(f"D2:D{N + 1}")
    sy.column_dimensions["H"].hidden = True
    for col, w in zip("ABCDEFG", (13, 22, 8, 9, 30, 6, 20)):
        sy.column_dimensions[col].width = w
    sy.freeze_panes = "A2"

    # Hesap: bugünden itibaren 120 gün, her gün için "o güne kadar kalırsam" toplamı
    A = f"Seyahatler!$A$2:$A${N + 1}"
    H = f"Seyahatler!$H$2:$H${N + 1}"
    for i, b in enumerate(["Gün", "Geçmişten sayılan", "Bugünden o güne", "Toplam", "Uygun mu"], 1):
        tk.cell(1, i, b).font = bold
    for k in range(120):
        r = k + 2
        tk.cell(r, 1, f"=TODAY()+{k}").number_format = "DD.MM.YYYY"
        lo = f"($A{r}-179)"
        a = f"(({A}>{lo})*{A}+({A}<={lo})*{lo})"
        b = f"(({H}<$A{r})*{H}+({H}>=$A{r})*$A{r})"
        x = f"({b}-{a}+1)"
        tk.cell(r, 2, f"=SUMPRODUCT(({A}<>\"\")*({x}>0)*{x})")
        tk.cell(r, 3, k + 1)
        tk.cell(r, 4, f"=B{r}+C{r}")
        tk.cell(r, 5, f"=D{r}<=90")

    # Özet
    oz.column_dimensions["A"].width = 44
    oz.column_dimensions["B"].width = 16
    satir = [
        ("Bugün", "=TODAY()", "DD.MM.YYYY"),
        ("180 günlük pencere başlangıcı", "=TODAY()-179", "DD.MM.YYYY"),
        ("Son 180 günde kullanılan gün", "=SUM(Seyahatler!G2:G301)", "0"),
        ("Kalan gün", "=90-B4", "0"),
        ("Şu an Schengen içinde mi?",
         '=IF(COUNTIFS(Seyahatler!A2:A301,"<="&TODAY(),Seyahatler!B2:B301,"")'
         '+COUNTIFS(Seyahatler!A2:A301,"<="&TODAY(),Seyahatler!B2:B301,">="&TODAY())>0,"EVET","Hayır")', None),
        ("Bugün girersen / içerideysen en geç çıkış",
         '=IF(Hesap!E2=FALSE,"Bugün giremezsin",IF(COUNTIF(Hesap!E2:E121,FALSE)=0,'
         '"120+ gün sonra",INDEX(Hesap!A2:A121,MATCH(FALSE,Hesap!E2:E121,0))-1))', "DD.MM.YYYY"),
    ]
    oz.cell(1, 1, "Schengen 90/180 — yeşil pasaport (vizesiz)").font = Font(bold=True, size=14)
    for i, (et, f, fmt) in enumerate(satir, 2):
        oz.cell(i, 1, et).font = bold
        c = oz.cell(i, 2, f)
        c.alignment = Alignment(horizontal="right")
        if fmt:
            c.number_format = fmt
    oz["B5"].font = Font(bold=True, size=14, color="1F6F3F")
    oz.cell(9, 1, "Nasıl kullanılır: 'Seyahatler' sekmesine her seyahat için bir satır ekle.")
    oz.cell(10, 1, "Giriş ve çıkış günleri tam gün sayılır. İçerideyken 'Çıkış'ı boş bırak.")
    oz.cell(11, 1, "Sayılmayan yerler: Türkiye, Kıbrıs, İngiltere, Gürcistan vb. (Schengen dışı).")
    oz.cell(12, 1, "Bulgaristan ve Romanya 2025'ten beri Schengen: oradaki günler SAYILIR.")
    wb.save(cikti)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--xlsx"]:
        xlsx_yaz(args[1])
        print("yazıldı:", args[1])
        sys.exit()
    o = ozet(date.fromisoformat(args[0]) if args else None)
    egc = o["en_gec_cikis"]
    print(f"Tarih: {o['bugun']:%d.%m.%Y}  (pencere: {o['pencere_basi']:%d.%m.%Y} – {o['bugun']:%d.%m.%Y})")
    print(f"Kullanılan: {o['kullanilan']} gün · Kalan: {o['kalan']} gün · İçeride: {'evet' if o['iceride'] else 'hayır'}")
    print("En geç çıkış (bugün girersen / içerideysen):",
          f"{egc:%d.%m.%Y}" if egc else "bugün giremezsin")
