# Restoran Self-Servis Kiosk ve Masadan QR Sipariş Sistemi — Yatırım Raporu

**Tarih:** 18 Kasım 2026 · **Mod:** YATIRIM · **Hazırlayan:** Araştırmacı Ajan
**Soru:** Türkiye'de restoran/kafe için kiosk + QR/app sipariş sistemini (yazılım + donanım, anahtar teslim) geliştirip satmak mantıklı mı?

**Bütçe ve zaman ufku belirtilmedi.** Bu yüzden iki senaryo ayrı hesaplandı: (A) kendi yazılımını geliştirip satmak, (B) mevcut bir markanın bayisi ya da entegratörü olmak. Kur varsayımı: **1 € ≈ 50 TL [Varsayım]**.

---

## 1. Yönetici özeti

**KARAR:**
- **Senaryo A (kendi yazılımı): YAPMA.**
- **Senaryo B (bayilik): ÖNCE TEST ET.** Bu testi de ancak HPP ve Vitrexia'dan zaman çalmayacaksa yap.

- **Varsayımın kısmen yanlış.** Türkiye'de kiosk ve QR sipariş teknolojisi zaten var ve satılıyor. robotPOS, Simpra ve Menulux gibi 13–22 yıllık yerli oyuncular kiosk, QR sipariş, mutfak ekranı (KDS), ÖKC ve e-Adisyon entegrasyonunu tek pakette satıyor. Pazardaki boşluk teknoloji değil, KOBİ'lerin bunu benimseme oranı.
- **Asıl giriş engeli yazılım değil, mevzuat ve entegrasyon.** Türkiye'de her satış GİB onaylı yeni nesil ÖKC (yazar kasa POS) ile kayda geçmek zorunda. Masaya servis yapan işletmelerde bir de e-Adisyon zorunluluğu var. Yeni bir oyuncunun bu entegrasyonları sıfırdan kurması pahalı ve yavaş.
- **Restoran tarafında değer gerçek ama dar.** Sistem, kasa kuyruğu yaşayan yüksek hacimli fast food işletmelerinde kendini 7–15 ayda geri ödüyor. Masaya servis yapan klasik restoranda kiosk anlamsız; orada QR sipariş yeterli ve bu pazar ucuz, hatta ücretsiz rakiplerle dolu.
- **Kendi yazılımını geliştirmenin maliyeti** yaklaşık €115k geliştirme artı €15k/ay sabit gider. Bu model ancak sıfırdan başlayıp **ayda 20 kiosk** satarsan 14 ayda geri dönüyor. Ayda 10 kiosk satarsan 36 ayın sonunda hâlâ yaklaşık −€113k zarardasın.
- **Daha makul yol:** Eskişehir ya da Bulgaristan'da mevcut bir markanın bayisi olmak. Sermaye ihtiyacı düşük, ama kazanç da sınırlı: ayda 5 kiosk satışla yaklaşık €2.500/ay net. Ayrıca bu iş seni sahaya bağlar.

---

## 2. Pazar büyüklüğü ve müşteri sorunu

**Pazar**
- **[Gerçek]** Türkiye yeme-içme hizmetleri pazarı 2025 itibarıyla yaklaşık **22 milyar $**. Hızlı servis restoranlarının bu pazardaki payı 2019'da %22'ydi, 2025'te %38'e çıktı (Bianet).
- **[Gerçek]** TÜRYİD sektörü 1 trilyon TL'nin üzerinde ve yaklaşık **150 bin işyeri** olarak tarif ediyor (Ekonomi Gazetesi).
- **[Gerçek]** McDonald's Türkiye'nin 306 restoranı var; 5 yılda 500 restorana çıkmayı hedefliyor. Yeni konsept restoranlarında **dijital sipariş ekranları zaten kullanılıyor** (Sabah, Şubat 2025; Capital, Şubat 2026).
- **[Gerçek]** Dünyada McDonald's'ın 143 binden fazla kiosku kurulu (Datos Insights, Wavetec aracılığıyla).

**Müşterinin sorunu**
- **[Gerçek]** Personel maliyeti: 2026'da asgari ücretlinin işverene teşviksiz maliyeti **40.874,63 TL/ay**.
- **[Gerçek]** Sektör maliyet baskısı altında: şirket kuruluşları %10,2 azaldı, kapananlar %21,4 arttı (Dünya).
- **[Varsayım]** Bu tablo "personelden tasarruf" önerisini çekici kılıyor. Ancak aynı baskı, işletmelerin yatırım iştahını da düşürüyor.
- **[Gerçek, satıcı iddiası]** Kiosk sepet tutarını %15–25 artırıyor (robotPOS). Fransa'da 2,3 milyon fiş üzerinden yapılan bir analizde kiosk siparişi tezgâh siparişinden %34 daha yüksek çıkmış (Innovorder). Bu verileri yayımlayanların hepsi kiosk satıcısı; bağımsız değil.

**Hedeflenebilir segment [Varsayım]**
- Kasa kuyruğu yaşayan kişiler: AVM yemek katları, fast food, kahve zincirleri, havalimanları. Bu segment Türkiye'de birkaç bin noktayla sınırlı ve büyük kısmı zaten bir POS markasına bağlı.
- Klasik masaya servis restoranı kiosk istemez; olsa olsa QR sipariş ister.

---

## 3. Nasıl para kazanılır

**Gelir modeli:**
- Donanım satışı (kiosk ve kurulum)
- Kiosk başı aylık yazılım aboneliği
- Opsiyonel olarak ödeme komisyonu payı. Bu genelde banka ya da ödeme kuruluşunda kalır.

**Fiyat referansları:**
- **[Gerçek]** Clover kiosku $3.499 ve kiosk başı aylık $34,95 yazılım ücreti (ABD).
- **[Gerçek]** Tayland'da bir kiosk ilanı ฿122.600 ve yıllık ฿6.000 yazılım ücreti.
- **[Gerçek]** MenuTiger QR siparişi ayda 75 siparişe kadar ücretsiz veriyor. QR tarafında fiyat sıfıra yakın.

**Restoranın geri dönüş hesabı** (kodla hesaplandı; satış €2.500, abonelik €40/ay, kur varsayımı):

| Kiosk ne kadar kadroyu boşaltıyor | Restoranın aylık tasarrufu | Geri dönüş süresi |
|---|---|---|
| 0,25 kadro | ~€204 | ~15 ay |
| 0,5 kadro | ~€409 | ~7 ay |

**Bizim tarafımızda Senaryo A** (kendi yazılımımız; tüm girdiler varsayım):
- Kiosk başı donanım marjı ~€950, abonelik marjı ~€30/ay
- Geliştirme ~€115k, sabit gider ~€15k/ay

| Ayda yeni kiosk | 36. ay kümülatif nakit | Geri dönüş |
|---|---|---|
| 5 | −€384k | yok |
| 10 | −€113k | yok |
| 20 | +€429k | 14. ay |

**Yorum [Varsayım]:** Sıfırdan başlayan bir oyuncunun yerleşik markalara karşı ayda 20 kiosk, yani yılda 240 kiosk satması çok iddialı bir hedef.

**Senaryo B** (bayilik; %20 komisyon ve kiosk başı €300 kurulum/servis kârı varsayımıyla): ayda 3 kiosk satışla ~€900, 5 kiosk ile ~€2.500, 10 kiosk ile ~€6.500 aylık net.

---

## 4. Sermaye ihtiyacı ve nakit akışı riski

- **Senaryo A [Varsayım]:** €150–250k ve en az 18–24 ay dayanma gücü. Gereken ekip ve harcamalar:
  - 3–4 yazılımcı (kiosk ön yüzü, QR web uygulaması, KDS, yönetim paneli)
  - ÖKC/GMU ve e-Adisyon entegrasyonu
  - Ödeme kuruluşu anlaşması
  - Saha kurulumu ve 7/24 destek
- Donanım için stok bağlanır. Çin'den alınan cihazlar peşin ödenir; müşteriler ise vadeli ister.
- **Senaryo B [Varsayım]:** €5–15k yeter. Bu tutar demo cihazı, araç ve bayilik bedeli içindir; bayilik bedeli varsa öğrenilmeli.
- **Kur riski [Varsayım]:** Donanım dolar ya da euro bazlı, satış TL. Kur oynaklığı marjı eritebilir.

---

## 5. Rekabet ve savunulabilir avantaj (moat)

**Türkiye'deki rakipler [Gerçek]**

| Oyuncu | Ne sunuyor | Ölçek / referans |
|---|---|---|
| robotPOS | Kiosk, QR, KDS, ÖKC, yemek kartı ödemesi kioskta | Kahve Dünyası, Tavuk Dünyası, HD İskender grubu; 22 yıllık |
| Simpra | Kiosk (içinde sabit POS), QR, YNÖKC, GMU, e-Adisyon | 22 ülke, 4.500+ terminal, 3.000+ işletme |
| Menulux | Self-order kiosk, QR, POS, Ingenico TSM / Pavo GMU entegrasyonu | 13+ yıl, 3.000+ işletme |
| Narpos | El terminali, kiosk, paket platformu entegrasyonu | "Binlerce" işletme (kendi beyanı) |
| MenuTiger | QR sipariş + POS + KDS | Ücretsiz paketten başlıyor |

**Donanım üreticileri [Gerçek]**
- **Telpo (Çin):** McDonald's için K20 modelini geliştirdi. Alibaba'da 21,5" kiosk fiyatı $800–1.500. AB perakendesinde Telpo K1 KDV hariç €589.
- **Diğer:** Alibaba'da $502'lik numune kiosklar; Posiflex (Tayvan); Partteam/OEMkiosks (Portekiz); Acrelec (Fransa).
- **Ödeme modülü:** Worldline/Ingenico'nun self servis ödeme modülleri (iSelf, iUP250).

**Bizim avantajımız ne olurdu? [Spekülasyon]** Somut bir avantaj göremiyorum:
- Fiyatla rekabet edilemez; QR tarafında rakipler ücretsiz paket veriyor.
- Teknoloji farkı yaratılamaz; yerli rakipler zaten AI tabanlı tahmin modülleri satıyor.
- Tek olası koz yerel saha hizmeti (Eskişehir) ve Bulgaristan'a erken giriş. İkisi de yazılım değil, hizmet avantajı.

---

## 6. Uygulama zorluğu

- **Mevzuat [Gerçek]:**
  - 3100 sayılı Kanun gereği perakende satış GİB onaylı ÖKC ile kayda geçmek zorunda.
  - Kartlı ödemede fiş ve banka slipi tek belgede, EFT-POS özellikli yeni nesil ÖKC ile üretilir.
  - Masaya servis yapan, gerçek usulde vergilendirilen lokanta ve kafeler e-Adisyon kapsamında. Yalnızca self servis hizmet veren işletmeler kapsam dışı.
- **Pratik sonuç [Varsayım]:** Kiosk tek başına bir ekran değil; GİB uyumlu bir yazar kasa POS'un önyüzü. Bu entegrasyon olmadan ürün yasal olarak satılamaz.
- **Ekip:** Yazılım ekibi, ÖKC üreticileri ve TSM'lerle teknik anlaşmalar, banka/ödeme kuruluşu, saha kurulum ve servis ağı.
- **Süre [Varsayım]:** Satılabilir ilk sürüm 9–12 ay. Referans müşteri edinmek ayrıca 6+ ay.
- **Menü mevzuatı [Gerçek]:** Temmuz 2026'dan itibaren menülerde içerik, kalori ve alerjen bilgisi zorunluluğu kademeli başladı. Dijital menüler bunu kolaylaştırır; bu küçük bir satış argümanı olabilir.

---

## 7. Neden işe yarayabilir / neden başarısız olabilir

**İşe yarayabilir:**
- Personel maliyeti yüksek ve artıyor.
- Hızlı servis zincirleri payını büyütüyor (%22'den %38'e).
- Avrupa'da kiosk standart hale geldi; Türk tüketicisi bunu yurt dışında görüyor.
- Turist yoğun bölgelerde çok dilli menü gerçek bir ihtiyaç.

**Başarısız olabilir:**
- Pazar dolu ve rakipler 13–22 yıllık.
- Fiskal entegrasyon pahalı.
- KOBİ restoranlar maliyet baskısı altında; yatırım yapmıyor.
- Kioskun asıl değeri kasa kuyruğu olan yerlerde, o yerler de zaten zincirlerin elinde.
- **[Gerçek]** Kiosk deneyimi her yerde tutmuyor: müşterilerin %80'i kiosklarda sorun yaşadığını söylüyor (QSRweb raporu). UMass kiosklarını bir hafta sonra kaldırdı. Shake Shack'in kasiyersiz konsepti şikâyet aldı. Analistlere göre kiosklarla tasarruf edilen işgücü çoğu zaman paket ve online siparişe kayıyor (CNN).

---

## 8. Riskler ve en büyük bilinmeyenler

**Riskler:**
- **Mevzuat:** GİB her yıl kural değiştirebilir; entegrasyon sürekli bakım ister.
- **Fiyat savaşı:** QR tarafı zaten ücretsizleşiyor.
- **Donanım arızası ve saha servisi:** Arızalı kiosk, marka itibarını doğrudan yer.
- **Kur riski.**

**Bilmiyorum:**
- Yerli rakiplerin gerçek kiosk fiyatları. Hepsi "teklif al" diyor, açık fiyat yok. Bu verilmezse model doğrulanamaz.
- Türkiye'de kurulu kiosk sayısı. Bağımsız bir veri bulamadım.
- Bulgaristan'daki fiskal cihaz kuralları (NRA, Наредба Н-18) ve rakip yoğunluğu. Bu araştırmada Bulgaristan için anlamlı veri çıkmadı.

---

## 9. Alternatifler

Aynı para ve zamanla şunlar yapılabilir:

1. **Bayilik / entegratörlük (Senaryo B):** Simpra, Menulux ya da robotPOS için Eskişehir veya İç Anadolu bayisi olmak. Düşük sermaye, hızlı test imkânı.
2. **Bulgaristan'da Türk markasının temsilciliği:** Bulgar restoranlarına Türk POS/kiosk çözümünü uyarlayıp götürmek, Zemya Hub zemini üzerinden. Önce Bulgaristan'ın fiskal kuralları ve rakip yoğunluğu araştırılmalı. Bunlar bilinmiyor.
3. **Hiç yapmamak:** Aynı zamanı mevcut 1. kademe satışa vermek.

---

## 10. En hızlı doğrulama deneyi (≤2 hafta, ~€0–300)

1. **Talep tarafı:** Eskişehir'de 15 yüksek hacimli işletmeyle görüş (fast food, kahve zinciri bayileri, AVM yemek katı). Her birine iki soru sor:
   - "Yoğun saatte kasa kuyruğu nedeniyle müşteri kaybediyor musunuz?"
   - "Kiosk başına €2.500 ve aylık €40'a kiosk koyar mıydınız?"
2. **Arz tarafı:** Simpra, Menulux ve robotPOS'a bayi adayı olarak yaz. Bayi komisyonunu, bölge münhasırlığını ve kiosk satış fiyatını yazılı olarak iste.
3. **Bulgaristan (opsiyonel):** Varna veya Şumnu'da 5 fast food işletmesine aynı soruları sor.

## 11. Öldürme kriterleri

Aşağıdakilerden biri gerçekleşirse fikir bırakılır:
- 15 görüşmeden 3'ten azı ciddi ilgi gösterirse (fiyat sorma, demo isteme).
- Bayi komisyonu %15'in altındaysa ya da bölge münhasırlığı yoksa.
- İlgilenen işletmelerin çoğu zaten bir POS markasına sözleşmeyle bağlıysa.

## 12. Başlanırsa ilk 30 gün (yalnızca Senaryo B ve test olumluysa)

1. Bayilik sözleşmesi imzala, 1 demo kiosk al.
2. İlk referans işletmeye indirimli kurulum yap; sepet tutarı ve kuyruk süresini önce ve sonra ölç.
3. Bu ölçümleri vaka çalışmasına dönüştürüp 30 işletmeye götür.

## 13. Mevcut önceliklere etkisi

**[Varsayım]** HPP ve Vitrexia 1. kademe; aylık €10.000 satış hedefi bu ikisine bağlı.

- **Senaryo A:** Zaman ve sermaye açısından ikisini de ciddi şekilde çalar.
- **Senaryo B:** Saha satışı gerektirir. Haftada 1–2 günden fazla yer kaplarsa mevcut önceliklere zarar verir.

**Öneri:** Deneyi yap, ama yalnızca haftalık satış bloğunun dışında kalan zamanda.

## 14. Güven tahmini

| Konu | Güven |
|---|---|
| "Kendi yazılımını geliştirme" kararı | %80 |
| Bayilik modelinin kârlılığı | %40 (fiyat ve komisyon verisi yok) |
| Rakamlar | Çoğu varsayım; asgari ücret ve rakip bilgileri kaynaklı |

---

## Kaynaklar

- McDonald's Türkiye 306 restoran / 500 hedef — Capital: https://www.capital.com.tr/haberler/tum-haberler/mcdonalds-turkiye-bu-yil-2-bin-kisiyi-daha-istihdam-edecegini-duyurdu
- McDonald's Türkiye dijital sipariş ekranları — Sabah: https://www.sabah.com.tr/yazarlar/pazar/funda-karayel/2025/02/16/seffaflik-lezzet-ve-guvenin-bulusma-noktasi/amp
- McDonald's 143.000+ kiosk — Wavetec: https://www.wavetec.com/blog/mcdonalds-leveraging-self-service-technologies/
- Pazar 22 milyar $, hızlı servis payı %38 — Bianet: https://bianet.org/haber/turkiyede-disarida-yeme-pazari-tekellesiyor-322172
- 150 bin işyeri — Ekonomi Gazetesi: https://www.ekonomigazetesi.com/kose-yazisi/vergisini-biz-ustlenecegiz-neden-hala-gonullu-dijital-bahsis-yasaya-kavusmuyor-82713
- Şirket kapanışları — Dünya: https://www.dunya.com/ekonomi/restorancinin-masasinda-da-fahis-fiyat-bulunuyor-haberi-794090
- Asgari ücret işveren maliyeti 2026 — Ekonomi Gazetesi: https://www.ekonomigazetesi.com/kose-yazisi/2026-yili-asgari-ucret-sigorta-primleri-alt-ve-ust-sinirlari-69324
- robotPOS kiosk / fast food / ödeme: https://en.robotpos.com/sektorel/fast-food-otomasyon , https://en.robotpos.com/odeme-orkestrasyon
- Simpra kiosk ve entegrasyonlar: https://simprasuite.com/restaurant-software/simpra-kiosk , https://simprasuite.com/restaurant-software/pos-system/
- Menulux: https://linkedin.com/company/menulux , https://apps.apple.com/us/app/-/id6742921152
- Narpos: https://kobitime.com/narpos/
- MenuTiger ücretsiz paket: https://www.menutiger.com/tr
- Telpo fiyatları: https://telpo.en.alibaba.com/videoshow.html?d_type=cv , https://aio.lv/en/product--telpo-k1ts-464--11682456.md
- Alibaba numune $502: https://touchwo.en.alibaba.com/product/11000000744643-804408212/21_5_inch_Interactive_Self_Service_Payment_Kiosk_Automatic_Touch_Screen_Kiosk_Self_Ordering_Machine_for_Restaurant.html
- Clover fiyatı — Otter: https://blog.tryotter.com/blog/toolkit/best-self-ordering-restaurant-kiosk-systems
- Tayland fiyatı — Papaya: https://www.papaya.co.th/blog/self-order-kiosk-vs-qr-ordering
- Sepet artışı %34 — Innovorder: https://www.innovorder.com/en/blog/price-self-ordering-kiosk
- ÖKC zorunluluğu — Kobitime: https://kobitime.com/yazarkasa-pos-veren-bankalar-2026/
- e-Adisyon kapsamı — Birfatura: https://birfatura.com/e-adisyon-nedir-e-adisyon-zorunlulugu/
- Menü içerik/kalori zorunluluğu — Bursa Hakimiyet: https://www.bursahakimiyet.com.tr/ekonomi/menulerde-yeni-donem-basladi-kalori-ve-icerik-bilgisi-zorunlu-oldu-1661381
- Kiosk sorunları %80 — QSRweb: https://www.qsrweb.com/blogs/satisfying-the-hunger-for-frictionless-tech-meeting-the-needs-of-qsr-customers-franchisees
- UMass kiosk kaldırma — Vending Times: https://www.vendingtimes.com/news/umass-removes-self-order-food-kiosks-due-to-poor-performance/
- İşgücü tasarrufu tartışması — CNN/ABC17: https://abc17news.com/money/cnn-business-consumer/2024/09/20/mcdonalds-touchscreen-kiosks-were-feared-as-job-killers-instead-something-surprising-happened/
- Shake Shack kasiyersiz konsept — The Spoon: https://thespoon.tech/?p=4694
