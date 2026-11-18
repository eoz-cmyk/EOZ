# Robot kollu kiosklar (barista / sandviç / tost robotu) — pasif gelir olarak yatırım değerlendirmesi

**Tarih:** 2026-11-18 · **Mod:** YATIRIM · **Hazırlayan:** Araştırmacı ajan
**Varsayılan zemin:** Eskişehir'de AVM veya açık alan (ana senaryo); Bulgaristan (Sofya, Varna) kıyas için. Kur: 1 USD ≈ 50,3 TL, 1 EUR ≈ 55,8 TL (Kasım 2026, serbest piyasa).

---

## 1. Yönetici özeti

- **[Gerçek]** Robotlu kahve kiosku gerçek ve büyüyen bir niş. Ama pazar raporları birbiriyle tutarsız: 2025 dünya pazarı için 285 milyon ile 1 milyar USD arasında rakamlar veriliyor. Kesin olan tek şey küçük bir niş olduğu.
- **[Gerçek]** Makine maliyeti: Alibaba'daki orta sınıf kiosklar adet başı ~23.500 USD, COFE+ (Hi-Dolphin) dış mekân kioskları 53–59 bin USD FOB. Türkiye'de kurulu toplam maliyet **~35 bin – 73 bin USD (≈1,8 – 3,7 milyon TL)** tutuyor [Varsayım: nakliye, gümrük, ek mali yükümlülük, montaj ve POS/marka giderleri ekli].
- **[Hesap]** Eskişehir'de 120 TL fincan fiyatı ile başa baş (FAVÖK=0) **~35–37 fincan/gün**. Yatırımın 24 ayda geri dönmesi için **66–107 fincan/gün**, 12 ayda dönmesi için **100–187 fincan/gün** gerekiyor. Üreticilerin "4–8 ayda geri dönüş" iddiası günde 400–500 fincanlık havalimanı ve metro gibi lokasyonlar için geçerli.
- **[Gerçek]** Bu iş **pasif değil**: her gün dolum ve temizlik gerekiyor, arızada makine tamamen duruyor, AVM ile kira ve ciro payı pazarlığı yapılıyor. "Show" etkisi de zamanla sönüyor. San Francisco'da Cafe X ve Singapur'daki benzer projeler, havalimanı ve metro gibi yoğun geçiş noktalarının dışında tutunamadı.
- **[Gerçek]** Sandviç, tost ve burger robotları kahveden çok daha olgunlaşmamış durumda. RoboBurger yıllar sonra hâlâ pilot aşamasında. Bozulabilir gıda israfı ve gıda mevzuatı riski de daha yüksek.

### KARAR: **Robot satın alarak: YAPMA (şimdi). Sermaye koymadan veri toplamak için: ÖNCE TEST ET.**
Kahve robotu, ancak (a) günde 120+ fincan doğrulanmış bir lokasyonda ve (b) tercihen sıfır sermayeli bir ciro paylaşım modeliyle mantıklı olur. Sandviç/tost robotu → **YAPMA**.

---

## 2. Pazar büyüklüğü ve müşteri sorunu

**Pazar (küresel):**
- [Gerçek] Raporlar arasında büyük fark var. SkyQuest: 2024'te 328,6 milyon USD, yıllık bileşik büyüme %5,6. Intel Market Research: 2025'te 820 milyon USD. MarkWide: 2026'da 285,4 milyon USD, büyüme %24,7. Asya-Pasifik pazarın ~%42'sini oluşturuyor.
- [Varsayım] Bu raporlar ücretli ve doğrulanması zor. Kesin söylenebilecek tek şey küçük, parçalı ve Çin üreticilerinin hâkim olduğu bir niş olduğu. Pazar büyüklüğü bu fikrin kararını belirlemez; belirleyici olan lokasyon başına satış.

**Türkiye:**
- [Gerçek] Yerli oyuncular var. Thud e-Robotics'in "X Barista" ürünü 2025 sonunda Türkiye'de ticari olarak satışa çıktı ve CES 2026'da sergilendi. Coffeetropic + E-Commint, Kozzy AVM'de saatte 40 kahve yapan bir pilot yürüttü. Pluspay, X Barista'ya ödeme entegrasyonu sağlıyor.
- [Gerçek] Kahve fiyatı yüksek: Starbucks Türkiye'de latte 175 TL (Ocak 2026), zincirlerde orta boy latte ~165–195 TL, mahalle kafelerinde latte 90–120 TL.
- [Gerçek] Kişi başı kahve tüketimi on yılda ~350–400 g'dan ~1,5 kg'a çıktı.
- [Gerçek] AVM'lerde reel ciro daralıyor: AYD verilerine göre üç aydır reel daralma var. ECE portföyünde 2026'nın ilk sekiz ayında ciro artışı %30 ile enflasyonun (%31,7) altında kaldı.

**Müşteri sorunu:** Asıl sorun tüketicinin değil, işletmecinin sorunu (kira + personel maliyeti). Tüketici açısından robot (1) biraz daha ucuz kahve ve (2) gösteri sunuyor. Çin'deki deneyimin dersi: gösteri değeri birkaç ay içinde sönüyor [Gerçek: Momentum Asia gözlemi; konut sitesinde yapılan bir akademik saha çalışması da "merakla denenen ama tekrar gelinmeyen" kullanım, teknik arızalar ve düşük tekrar ziyaret bildiriyor].

---

## 3. Nasıl para kazanılır — birim ekonomi

### Gelir modelleri
1. **Sahip-işletmeci:** Makineyi alırsın, AVM'ye kira veya ciro payı ödersin, satışın tamamı senin. (Bu raporda modellenen.)
2. **Ciro paylaşımı / yer sağlayıcı:** Üretici veya marka makineyi koyar, sen lokasyonu bulursun ve işletirsin; ciro bölüşülür. Sermaye düşük, kazanç da düşük.
3. **Bayilik / distribütörlük:** Makine satarsın (Türkiye veya Bulgaristan'da). Pasif değildir, bir satış işidir.
4. **Kiralama (HaaS):** Ella (Crown Digital) 60 aylık donanım kiralama modeli kullanıyor [Gerçek]. Türkiye'de kurumsal ofis veya kampüse kiralama da bir seçenek.

### Varsayımlar (model 1)
| Kalem | Değer | Etiket |
|---|---|---|
| Satış fiyatı | 120 TL (KDV %10 dahil) | Varsayım: zincirlerin %30 altında |
| Hammadde + bardak + kapak | 30 TL/fincan | Varsayım (üretici beyanı ciro %15–20; Türkiye'de çekirdek ve süt pahalı) |
| Kart komisyonu | %2 | Varsayım |
| AVM kirası | max(35.000 TL sabit, cironun %12'si) | Varsayım: ciro payı genelde %10–15 [Gerçek: YL Vending] |
| Dolum/temizlik personeli | 25.000 TL/ay (yarı zamanlı) | Varsayım |
| Elektrik | 3.500 TL/ay | Varsayım |
| Yazılım/uzaktan yönetim | 150 USD/ay | Varsayım |
| Bakım/yedek parça | yatırımın yıllık %4'ü | Varsayım |
| Kurulu yatırım — orta (COFE+ sınıfı) | ~73.250 USD ≈ 3,68 M TL | Varsayım (55k makine + 4k nakliye + %15 vergi yükü + 6k montaj) |
| Kurulu yatırım — düşük (Alibaba orta sınıf) | ~35.000 USD ≈ 1,76 M TL | Varsayım |

### Sonuçlar (vergi öncesi, arıza/duruş hariç — iyimser)
| Fincan/gün | Aylık ciro (KDV hariç) | Aylık FAVÖK | Geri dönüş (orta yatırım) | Geri dönüş (düşük yatırım) |
|---|---|---|---|---|
| 40 | 131 bin TL | 7–14 bin TL | dönmez | dönmez |
| 80 | 262 bin TL | ~100–106 bin TL | 37 ay | 17 ay |
| 120 | 393 bin TL | ~180–186 bin TL | 20 ay | 9,5 ay |
| 200 | 655 bin TL | ~333–339 bin TL | 11 ay | 5 ay |
| 350 | 1,15 M TL | ~620 bin TL | 6 ay | 3 ay |

**Eşikler:** Başa baş ~35–37 fincan/gün · 24 ayda geri dönüş: 66 (düşük) / 107 (orta) fincan/gün · 12 ayda geri dönüş: 100 / 187 fincan/gün.

**Bulgaristan kıyası** (3 € fincan, KDV %20, orta yatırım): 120 fincan/gün → aylık FAVÖK ~4.400 €, geri dönüş ~15 ay. Türkiye'den kötü değil ama daha iyi de değil; kahve fiyatı Türkiye'ye göre düşük, kira ve personel maliyeti benzer [Varsayım].

**Kritik okuma:** Ekonomi tamamen günlük fincan sayısına bağlı. [Gerçek] Bir üretici bile "muhafazakâr" senaryoda günde 60–80 fincan ve 12–18 ay geri dönüş varsayıyor. 4–8 ay iddiaları 400–500 fincan/gün varsayımına dayanıyor. Eskişehir'de orta ölçekli bir AVM'de, yenilik etkisi geçtikten sonra günde 80–120 fincan sürdürmek **[Spekülasyon]** gerçekçi bir üst sınır gibi görünüyor. Bu da düşük yatırımla 1,5 yıl, orta yatırımla 2–3 yıllık bir geri dönüş demek. Makinenin ömrü ~5 yıl (COFE+ ömür boyu 400.000+ fincan beyan ediyor). Kur riski de var: makine dolarla alınıyor, satış TL ile yapılıyor.

---

## 4. Sermaye ihtiyacı ve nakit akışı riski
- Başlangıç: 1,8 – 3,7 M TL (tek makine). 2–3 aylık işletme sermayesi ve stok için +250–400 bin TL [Varsayım].
- Nakit riski: Arıza = %100 gelir kaybı, teknisyen gelene kadar makine durur [Gerçek: YL Vending]. Çinli tedarikçilerde garanti genelde 1 yıl ve yerinde servis 72 saat içinde (Dobot); Türkiye'de bu süre pratikte daha uzun olabilir [Varsayım].
- Gümrük: Çin menşeli bazı makine pozisyonlarına ek mali yükümlülük uygulanıyor. Bazı kalemlerde Çin için "%40 veya adet başı minimum 7.000 USD" gibi çok ağır oranlar görülüyor [Gerçek: farklı GTİP'ler için örnek]. **Robot kioskun GTİP'i ve gerçek vergi yükü bir gümrük müşavirine sorulmadan bütçe kesinleşmez.** Bu raporda %15 varsayıldı; gerçek oran çok daha yüksek çıkabilir.

## 5. Rekabet ve savunulabilir avantaj (moat)
- Teknolojide moat **yok**: makineler Alibaba'dan herkesin alabileceği emtia ürünler. Hi-Dolphin, 7. nesil ürünüyle 65 ülkeye satış yaptığını açıklıyor [Gerçek].
- Türkiye'de yerli rakipler (X Barista, Coffeetropic) zaten AVM'lere girmeye çalışıyor [Gerçek].
- Tek gerçek moat **lokasyon sözleşmesi**: münhasırlık maddesi olan yoğun bir nokta (havalimanı, hastane, üniversite, büyük AVM girişi). Bu da AVM yönetimi pazarlığına bağlı ve kopyalanabilir bir avantaj.
- Zincir kafeler (Starbucks, Kahve Dünyası vb.) ve mahalle kafeleri rakip; 90–120 TL'lik mahalle kafesi fiyatıyla robotun rekabet etmesi zor.

## 6. Uygulama zorluğu
- Gerekenler: AVM kira veya ciro sözleşmesi; vergi levhası; Tarım ve Orman İl/İlçe Müdürlüğü'nden gıda işletmesi kaydı (otomatik satış makineleri için makine başına ayrı kayıt sistemi bulunuyor [Gerçek: zenginleştirilmiş su otomatları talimatında makine başı kayıt; kahve için kapsam il müdürlüğüne teyit ettirilmeli]); CE uygunluğu ve elektrik/su bağlantısı; günlük dolum yapacak bir kişi; teknik servis anlaşması.
- Süre: Sipariş → üretim (~25 gün) → deniz nakliyesi (~30–40 gün) → gümrük ve kurulum. Toplam **~2,5–4 ay** [Varsayım].
- Sandviç/tost robotu: bozulabilir ürün (et, peynir, sebze) nedeniyle soğuk zincir, israf ve gıda denetimi riski çok daha yüksek. Hazırlık işlemi "satış yeri" yerine "üretim/hazırlama" sayılırsa mevzuat ağırlaşır [Spekülasyon — teyit edilmeli]. RoboBurger sabit lokasyon başarısı gösteremedi, yeniden tasarıma ve birleşmeye gitti [Gerçek].

## 7. Neden işe yarayabilir / Neden başarısız olabilir
**İşe yarayabilir çünkü:**
- Türkiye'de kahve pahalı ve personel/kira maliyeti yüksek; robot 2–4 m²'de 24 saat çalışabilir.
- Doğru lokasyonda (günde 150+ fincan) birim ekonomi güçlü: %45–50 FAVÖK marjı, ~1 yılda geri dönüş [Hesap].
- AVM'ler "deneyim" ve trafik yaratan konseptler arıyor; robot boş bir koridoru değerlendirebilir.

**Başarısız olabilir çünkü:**
- **Yenilik etkisi sönüyor;** ilk 2–3 ayın rakamları yanıltıcı.
- Cafe X (San Francisco) oturma alanlı lokasyonlarını kapattı, havalimanına geçti; pandemide orayı da kapattı [Gerçek]. Robot kahvenin dünyada kanıtlanmış tek lokasyon tipi yoğun geçiş noktaları.
- Arıza = sıfır gelir; Türkiye'de Çin makinesine yedek parça ve servis zayıf.
- AVM ciroları reel olarak daralıyor; ciro payı ve sabit kira ile marj kolayca eriyor.
- Kur riski: yatırım dolar, gelir TL.
- "Pasif gelir" beklentisi yanlış; günlük operasyon şart.

## 8. En büyük bilinmeyenler
1. Eskişehir AVM'lerinde (Espark, Kanatlı, Vega vb.) kiosk alanının gerçek kira ve ciro payı koşulları. **Bilmiyorum.**
2. Türkiye'deki mevcut robot kiosk pilotlarının (Kozzy AVM, X Barista noktaları) 3. aydan sonraki gerçek günlük satışları. **Bilmiyorum.**
3. Robot kioskun GTİP'i ve gerçek gümrük + ek mali yükümlülük yükü. **Bilmiyorum.**
4. Türkiye'de servis ve yedek parça desteği veren yetkili tedarikçi olup olmadığı.

## 9. Alternatifler (aynı parayla)
- **Robot kolsuz süper-otomatik kahve otomatı** (Franke/WMF/Schaerer sınıfı makine + şık bir kiosk): Kahve kalitesi aynı, robot kolun bakım karmaşıklığı yok. Yatırım muhtemelen 1/2 – 1/3 [Varsayım]. Bir sektör kaynağı da robot kolun gerçek kurulumlarda işleri yavaşlattığını ve bakımı zorlaştırdığını söylüyor [Gerçek].
- **Ciro paylaşımlı yer sağlayıcılık:** Yerli bir üreticinin (X Barista vb.) makinesini kendi bulduğun lokasyona koyup komisyon almak; sermaye ~0.
- **Kurumsal kiralama (HaaS):** Hastane, üniversite veya büyük ofis lobisine aylık sabit kira + fincan başı ücretle koymak; trafik riski daha düşük.

## 10. En hızlı doğrulama deneyi (≤2 hafta, ~0 TL)
1. **Eskişehir'de 3 AVM'nin kiralama müdürüyle görüş:** 4–6 m² kiosk alanının kira ve ciro payı, günlük ziyaretçi sayısı, münhasırlık.
2. **X Barista (Thud e-Robotics) ve Coffeetropic'e yaz:** Makine fiyatı, ciro paylaşım modeli var mı, mevcut noktalarda 3. aydan sonraki ortalama günlük fincan sayısı.
3. **Hi-Dolphin (COFE+) ve 1 Alibaba tedarikçisine yaz:** Türkiye'ye CIF fiyatı, garanti, Türkiye'de servis ortağı, GTİP kodu.
4. **Gümrük müşavirinden** o GTİP için toplam vergi yükünü yazılı iste.
5. **Saha gözlemi:** Bir AVM'de seçilen noktada hafta içi ve hafta sonu 2'şer saat yaya trafiğini say. Kahve dönüşüm oranını %3 kabul ederek günlük fincan tahmini çıkar.

## 11. Öldürme kriterleri
- Yaya trafiği × %3 dönüşüm < **100 fincan/gün** → vazgeç.
- Mevcut Türk pilotlarının 3. aydan sonraki ortalaması < 80 fincan/gün (veya veri paylaşmıyorlarsa) → vazgeç.
- Toplam kurulu maliyet > **45 bin USD** ve ciro paylaşım modeli yok → vazgeç.
- AVM kirası + ciro payı tahmini cironun %18'inden fazla → vazgeç.
- Türkiye'de 72 saat içinde yerinde servis garantisi yok → vazgeç.

## 12. Başlanırsa ilk 30 gün
1–7. gün: 10. bölümdeki 1–4 numaralı adımlar (görüşmeler ve teklifler).
8–14. gün: Trafik sayımı ve modelin gerçek kira ve vergi rakamlarıyla güncellenmesi.
15–21. gün: Öldürme kriterlerinin kontrolü. Geçerse önce **ciro paylaşımlı veya kiralık tek makine** müzakeresi; satın alma son seçenek.
22–30. gün: Gıda işletmesi kaydı ön başvurusu, AVM ile niyet mektubu. Satın almaya ancak bu adımdan sonra karar verilir.

## 13. Güven tahmini
- Birim ekonomi hesabının yönü (eşikler): **%75** — matematik sağlam, girdiler varsayım.
- Türkiye'deki gümrük yükü ve AVM kira rakamları: **%40** — doğrulanmadı.
- "Pasif gelir olarak şimdi robot almak yanlış" kararı: **%70.**

---

## CEO özeti (paylaşım için)

**Konu:** AVM ve açık alanlara konan robot kollu kiosklar (kahve, sandviç, tost) yatırım olarak mantıklı mı?

- **Pazar:** Küresel robotlu kahve kiosku pazarı küçük bir niş (raporlara göre 0,3–1 milyar USD) ve Çinli üreticilerin hâkimiyetinde. Türkiye'de yerli üreticiler AVM pilotlarına yeni başladı.
- **Maliyet:** Tek kahve robotu Türkiye'de kurulu olarak ~1,8–3,7 milyon TL (35–73 bin USD). Gümrük yükü henüz netleşmedi.
- **Ekonomi:** 120 TL fincan fiyatıyla başa baş ~35–40 fincan/gün. Yatırımın 2 yılda dönmesi için 70–110, 1 yılda dönmesi için 100–190 fincan/gün gerekiyor. Üreticilerin "4–8 ayda geri dönüş" vaadi havalimanı ve metro gibi günde 400+ fincanlık noktalar için geçerli.
- **Riskler:** Bu iş pasif değil (günlük dolum ve temizlik, arızada sıfır gelir). Yenilik etkisi birkaç ayda sönüyor. AVM ciroları reel olarak daralıyor. Yatırım dolar, gelir TL. Teknolojide rekabet avantajı yok; tek avantaj lokasyon sözleşmesi. Sandviç ve tost robotları henüz olgun değil, gıda riski yüksek.
- **Görüş:** Şu an makine satın almak önerilmiyor. Önce sıfır sermayeyle 2 haftalık bir test yapılmalı: AVM kira ve ciro payı teklifleri, mevcut Türk pilotlarının gerçek satış verileri, gümrük maliyeti ve lokasyonda trafik sayımı. Ancak günde 100+ fincan doğrulanırsa ve tercihen ciro paylaşımlı veya kiralık modelle tek makineyle başlanabilir. Sandviç/tost robotu: hayır.
- **Güven:** Karar ~%70; maliyet ve kira girdileri henüz doğrulanmadı.

---

## Kaynaklar
- SkyQuest / GII — Robot Coffee Kiosk Market: https://www.skyquestt.com/report/robot-coffee-kiosk-market
- Intel Market Research — Robotic Coffee Kiosk Market: https://www.intelmarketresearch.com/robotic-coffee-kiosk-market-64373
- MarkWide Research: https://markwideresearch.com/robot-coffee-kiosk-market
- pmarketresearch (Asya-Pasifik payı): https://pmarketresearch.com/?p=2371424
- HKTDC — COFE+ Outdoor Kiosk fiyatı: https://sourcing.hktdc.com/en/Product-Detail/COFE-Coffee-Robot-Kiosk-Outdoor--1Z03OKPMH
- Alibaba — Robot kahve kiosku fiyatları: https://www.alibaba.com/product-introduction/Hot-Sale-Automatic-Coffee-Robot-Kiosk_1601036767417.html
- GCR Mag — Rise of the robot barista: https://www.gcrmag.com/rise-of-the-robot-barista
- Hi-Dolphin basın bültenleri (65 ülke, 4–8 ay geri dönüş): https://rss.globenewswire.com/news-release/2026/04/02/3267136/0/en/Record-Breaking-Black-Tech-COFE-Intelligent-Coffee-Robot-Sold-in-65-Countries.html ; https://pr.chestercounty.com/article/7th-Generation-Robot-Barista-Surpasses-Human-Competitor-in-Shanghai-Hongqiao-Robot-Coffee-Competition/6a229341e80eb70d15dfa5a3
- KrASIA — Hi-Dolphin: https://kr-asia.com/coffee-in-58-seconds-inside-hi-dolphins-global-robot-cafe-push
- YL Vending — ROI, ciro payı, arıza riski: https://www.ylvending.com/news/how-does-a-robot-coffee-machine-work-in-retail-stores/ ; https://www.ylvending.com/news/are-robotic-barista-machines-worth-the-investment/ ; https://www.ylvending.com/news/pros-and-cons-of-unattended-coffee-kiosk-solutions/
- Dobot Coffee Bar sunumu (garanti, servis): https://cdn.robotshop.com/media/D/Dot/RB-Dot-86/pdf/dobot-single-arm-coffee-bar-presentation.pdf
- Cafe X kapanışları: https://thespoon.tech/cafe-x-shuts-down-its-three-downtown-san-francisco-locations/ ; https://thespoon.tech/cafe-x-closed-its-airport-locations-and-laid-off-staff-now-its-planning-for-the-future/ ; https://grubbrr.com/what-happened-to-cafe-x-and-where-is-it-going/
- Momentum Asia — "Robotic barista will not work": https://thelowdown.momentum.asia/robotic-barista-will-not-work/
- arXiv — saha çalışması, düşük tekrar kullanım: https://arxiv.org/abs/2603.16336
- 3L3C — robot kolun bakım ve hız etkisi: https://www.3l3c.ai/us/blog/ai-in-robotics-automation/coffee-robot-vending
- Crown Digital / Ella: https://www.worldcoffeeportal.com/news/singapore-based-robot-barista-concept-ella-set-for-mass-manufacture/ ; https://www.newegg.com/p/341-00UK-00001
- RoboBurger durumu: https://www.aol.com/lifestyle/happened-roboburger-shark-tank-230300854.html ; https://www.foodrepublic.com/1931569/roboburger-shark-tank-now/
- Burger robot fiyat aralıkları: https://www.grabarobot.com/robots/cooking-robot/products/creator-burger-bot/
- DHA — Coffeetropic robotik barista, Kozzy AVM: https://www.dha.com.tr/teknoloji/kahve-sektorunde-yapay-zeka-destekli-robotik-barista-sistemi-2822079
- Para Dergi — X Barista / Thud e-Robotics: https://www.paradergi.com.tr/girisimcilik/2026/01/16/yerli-robot-barista-abdde-dikkatleri-uzerine-cekti
- Ekonomist — Pluspay & X Barista: https://www.ekonomist.com.tr/girisim-kobi/robotik-kahveye-fintek-dokunusu-77264
- Starbucks Türkiye 2026 fiyatları: https://www.24saatgazetesi.com/starbucksa-zam-geldi-mistarbucksta-en-ucuz-kahve-fiyati-2026da-kac-tl-starbucks-turkiyede-fiyatlari-guncelledi
- Zincir kahve fiyatları 2024→2026: https://www.hisse.net/haber/dunyada-kahve-ucuzluyor-turkiye-de-fiyatlar-artiyor-85579
- Kahve fiyat karşılaştırması 2026: https://www.hemenhesap.com/hesap/kahve-hesaplama
- AVM ciro endeksi: https://fintables.com/arastirma/bultenler/sektorel-gorunum/sektorel-gorunum-ekim-2026-perakende-bulteni ; https://www.ekonomigazetesi.com/sektor-haberleri/avm-kira-odemelerinde-oteleme-talepleri-artiyor-88612
- Ek mali yükümlülük örneği (Çin, %40 / min 7.000 USD): https://orgtr.org/ithalatta-ilave-gumruk-vergisi-uygulanmasina-iliskin-kararda-degisiklik-yapilmasina-dair-karar-karar-sayisi-8639/
- Otomatik satış makinesi kaydı (makine başına): https://www.lexpera.com.tr/mevzuat/talimatlar/vitamin-ve-veya-mineral-ilaveli-su-otomatik-satis-makineleri-talimati-13626392
- Kur (11–13 Kasım 2026): https://www.bloomberght.com/dolar-ve-euro-kuru-bugun-ne-kadar-oldu-11-kasim-2026-doviz-fiyatlari-pkh2-3794153
- Starbucks Sofya fiyatı (Wolt): https://wolt.com/en/bgr/sofia/restaurant/starbucks-i-ring-mall
