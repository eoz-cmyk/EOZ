# Ucuzgez uygulaması — ütopya proje çalışması

**Tarih:** 2026-11-21 · **Mod:** YATIRIM (hayali senaryo) · **Kademe:** 2. kademe (bkz. öncelikler)

**Çerçeve [Varsayım]:** Bu çalışma "kaynak ve zaman sınırı olmasaydı Ucuzgez uygulaması nasıl olurdu" sorusunun cevabıdır. Ucuzgez bugün statik bir haftalık fırsat sayfası ve bir Telegram kanalından ibaret. Trafik verisi henüz yok. Bütün rakamlar euro cinsinden, kur ve kullanıcı davranışı varsayımlarına dayanıyor.

---

## 1. Yönetici özeti

- Türkiye'de "uçak bileti arama" pazarı dolu: Enuygun, Obilet, Turna, Skyscanner ve Google Flights ücretsiz ve güçlü. **Bir arama motoru daha yapmak kaybettirir.**
- Boş olan alan şu: **Türk pasaportuyla seyahatin gerçek sorunları.** Bunlar Schengen vize krizi, vizesiz rotalar, yurt dışı çıkış harcı ve bayram/köprü planlaması. Global fırsat servisleri (Going, Jack's Flight Club) bunlarla ilgilenmiyor. Yerel OTA'lar da fırsatı "pasaportuna göre" süzmüyor.
- Ütopya Ucuzgez'in adı: **"Pasaportuna göre fırsat."** Türk yolcuya, gidebileceği ve gerçek toplam maliyeti belli fırsatları gösteren bir kürasyon uygulaması.
- Para; affiliate (bilet, otel, eSIM, seyahat sağlık sigortası) ve ücretli "Pro" üyelikten gelir. Ama **affiliate geliri rezervasyon başına sadece 4–7 €**. Ücretli reklamla büyürsen her senaryoda zarar edersin. Ancak topluluk (Telegram/Instagram) organik büyürse kâra geçer.
- **KARAR: UYGULAMA İÇİN YAPMA, FARKLILAŞMAYI ÖNCE TEST ET.** Fark yaratacak fikri (vize filtreli fırsat) uygulama yazmadan, Telegram'da 4–6 hafta test et.

---

## 2. Pazar büyüklüğü ve müşteri sorunu

**Pazar**
- [Gerçek] 2025'te Türkiye havalimanlarında direkt transit dahil 247,1 milyon yolcu trafiği oldu; Cumhuriyet tarihi rekoru. (DHMİ / Ulaştırma Bakanlığı)
- [Gerçek] Yurt dışına çıkan Türk vatandaşı sayısı 2012'de 5,8 milyondu, 2025'te 11,8 milyona çıktı. 2026'nın ilk 6 ayında 6,3 milyon.
- [Gerçek] Türkiye, 2025'te Schengen'e en çok başvuru yapan ikinci ülke oldu (~1,3 milyon başvuru).

**Müşterinin asıl sorunu (Ucuzgez'in kapısı)**
- [Gerçek] Schengen randevuları bot hesaplarla bloke ediliyor. TÜRSAB'a göre randevular karaborsada 1.000 €'ya kadar satılıyor. İtalya'ya başvurabilenlerin sayısı %32,3 düştü.
- [Gerçek] Türk vatandaşları, vize sorunu yüzünden vizesiz veya kolay vize alınan ülkelere yöneliyor; Uzakdoğu rotaları öne çıkıyor. Vizesiz gidilebilen ülke sayısı kaynağa göre 78 ile 103 arasında değişiyor (e-vize ve kapıda vize dahil edilip edilmemesine göre).
- [Gerçek] Yurt dışı çıkış harcı 2026'da 1.250 TL. 2027'de yeniden değerleme oranıyla ~1.598 TL olması bekleniyor. Fırsat sitelerinin gösterdiği "99 €'luk bilet" fiyatında bu yok.
- [Varsayım] Tipik bir Türk yolcunun gerçek sorusu "en ucuz bilet nerede?" değil, şu: **"Elimdeki vizeyle / vizesiz, bu bayram, Türkiye'den çıkış harcı dahil, en ucuza nereye gidebilirim?"** Bu soruya bugün tek ekranda cevap veren bir ürün yok.

---

## 3. Rakipler ne yapıyor?

| Rakip | Ne yapıyor | Nasıl para kazanıyor | Ucuzgez için dersi |
|---|---|---|---|
| **Enuygun** (TR) | Bilet, otel, otobüs, araç, sigorta, finans karşılaştırma. 18 milyonun üzerinde uygulama indirmesi, ayda 20 milyon+ ziyaretçi. Kendi puan sistemi (ENCoin). | TÜRSAB A grubu acente olarak satış komisyonu, finans/sigorta çapraz satış. | Arama/satışta yenilmez. Onunla yarışma. |
| **Obilet / Turna** (TR) | Otobüs + uçak bileti satışı, kampanya bildirimleri. | Acente komisyonu. | Otobüs + uçak birleşimi var ama "fırsat kürasyonu" yok. |
| **Skyscanner / Google Flights** | Global meta-arama. Google'ın fiyat takibi ve bazı uçuşlarda ücretsiz fiyat garantisi var. | Tıklama/rezervasyon başına ücret. | "Fiyat takibi" bedava. Bunu ücretli özellik olarak satamazsın. |
| **Hopper** | Fiyat tahmini + "fintech" eklentiler (fiyat dondurma, iptal hakkı). | Gelirin %50–70'i eklentilerden geliyor. 2024'te ~850 M $ gelir (tahmini). | Asıl para eklentide. Ama FTC, gizli ücretler yüzünden 35 M $ uzlaşma aldı. Şeffaf olmayan eklenti hukuki risk. |
| **Going** (ABD) | İnsan + yazılımla seçilmiş fırsat bildirimleri, "Price Drop" (alımdan sonra fiyat düşüşü takibi). | Abonelik: Premium 49 $/yıl, 14 gün deneme. 2 milyon+ üye. | Kürasyon + abonelik modeli çalışıyor. Ama ABD'nin ödeme gücüyle. |
| **Jack's Flight Club** (İngiltere/AB) | 30 £ ile newsletter olarak başladı, 1,5–2,2 milyon üyeye ulaştı. Ücretsiz üye az fırsat alır, Premium (48 £/yıl) 4 kat fazla fırsat, kalkış havaalanı tercihi ve hafta sonu kaçamakları. | Freemium abonelik + affiliate. | **Ucuzgez'in birebir kopyalanabilecek modeli bu.** Küçük başla, ücretsizi besle, Pro'ya dönüştür. |
| **HolidayPirates** (DE ve 10 ülke) | Sosyal medya odaklı fırsat yayını. 10 milyon+ Facebook takipçisi, ayda 30 milyon+ ziyaret. | Affiliate + sponsorlu içerik. | Önce topluluk, sonra uygulama. Uygulama, topluluğun üstüne kuruldu. |
| **TR Telegram/Instagram fırsat kanalları** | Kampanya paylaşımları (THY, Pegasus, AJet kampanyaları). | Affiliate/işbirliği. | Dağınık, vize/pasaport bilgisi yok, güvenilirlik düşük. |

**Özet [Varsayım]:** Global oyuncuların hiçbiri Türk pasaportu odaklı değil. Yerel oyuncular ise satış yapmaya odaklı, kürasyon yapmıyor. Boşluk ikisinin kesişiminde.

---

## 4. Ütopya Ucuzgez — özellikler

### Çekirdek (farkı yaratan 5 özellik)
1. **Pasaport/vize filtresi ("Gidebileceğin fırsatlar"):** Kullanıcı elindeki vizeleri ve bitiş tarihlerini girer (ör. "çok girişli Schengen, 2027-08'e kadar", "ABD vizesi var", "vizem yok"). Uygulama sadece gidebileceği fırsatları gösterir: vizesiz, e-vize, kapıda vize ya da mevcut vizeyle. [Varsayım: TR'de bunu yapan ürün yok; ayrıca doğrulanmalı.]
2. **"Vizen bitmeden kullan" bildirimi:** Schengen vizesinin bitmesine 60/30 gün kala, o vizeyle gidilebilecek ucuz rotaları gönderir. Schengen randevusunun bu kadar zor bulunduğu bir ortamda, alınmış vizeyi boşa harcamamak gerçek bir değer.
3. **Gerçek toplam maliyet (TL):** Bilet + bagaj + yurt dışı çıkış harcı (1.250 TL) + varsa vize/e-vize ücreti + havalimanına ulaşım. "99 € bilet" yerine "kapıdan kapıya 6.840 TL" yazar.
4. **Bayram ve köprü planlayıcı:** Resmi tatilleri ve kullanıcının izin günü sayısını alır. "3 gün izinle 9 gün tatil + o tarihlerdeki en ucuz 5 rota" çıkarır. Türkiye'ye özel ve yılda birkaç kez yoğun talep yaratır.
5. **Çoklu çıkış noktası (Anadolu + sınır ötesi):** Eskişehir/Ankara gibi illerden YHT/otobüs + İstanbul uçuşu kombinasyonu. Edirne/Trakya için **Sofya, Plovdiv ve Selanik çıkışlı low-cost uçuşlar**: Schengen vizesi olan Türk yolcu için sınırı geçip ucuza uçma rotası. Ucuzgez'in eski "otobüs + uçak" fikrine de oturuyor. [Varsayım: Sofya'dan Avrupa low-cost fiyatları çoğu zaman İstanbul'dan ucuz; rota bazında doğrulanmalı.]

### Standart (olmazsa olmaz, fark yaratmaz)
- Haftalık seçilmiş fırsatlar (bugünkü site), kalkış havaalanı tercihi, anlık push bildirimi.
- Fiyat alarmı (Google bunu bedava veriyor, sadece temel hizmet olarak sunulur).
- Tek dokunuşla affiliate partnerine yönlendirme. Bilet satışı yapılmaz; TÜRSAB lisansı ve müşteri hizmeti yükü olmaz.
- Destinasyon kartı: giriş şartı, eSIM, sigorta, kabaca günlük harcama.

### Bilinçli olarak YAPILMAYACAKLAR
- **Vize randevu botu/alarmı:** TÜRSAB bot hesaplarla mücadele ediyor. Hukuki ve itibar riski çok yüksek.
- **Fiyat dondurma / iptal sigortası gibi fintech ürünler:** Sermaye ve risk yönetimi ister. Hopper'ın FTC cezası gösteriyor ki şeffaf yapılmazsa ceza gelir.
- **Kendi arama motoru:** Enuygun ve Skyscanner ile yarışılamaz.

---

## 5. Nasıl para kazanılır?

### Gelir kalemleri
| Kalem | Oran | Rezervasyon başına | Not |
|---|---|---|---|
| Uçak bileti (Aviasales/Travelpayouts) | Bilet fiyatının ortalama %1,1'i | ~2 € | [Gerçek] Travelpayouts verisi. Düşük. |
| Skyscanner (Impact) | Skyscanner'ın komisyonunun %20–50'si, performansa bağlı | belirsiz | [Gerçek] Sabit oran yok, düşük trafikte oran düşer veya hesap kapanabilir. |
| Otel | ~%3 (aracı üzerinden) | ~7–10 € | [Varsayım] Oran araştırılmadı, doğrulanmalı. |
| eSIM (Airalo) | %10'a kadar | ~1 € | [Gerçek] Oran Airalo'nun programından. |
| Seyahat sağlık sigortası | ~4 €/poliçe | ~4 € | [Varsayım] Schengen başvurusu için zorunlu olduğundan bağlam güçlü; TR'deki program oranları araştırılmalı. |
| **Pro üyelik** | 10–15 €/yıl (~500–750 TL) | — | [Varsayım] Going 49 $, JFC 48 £. Türk alım gücüne göre 1/4 fiyat. |
| Sponsorlu fırsat (B2B) | Kampanya başına | — | [Spekülasyon] Balkan/Bulgaristan otelleri, bölgesel havayolları. Ancak 50 bin+ takipçiden sonra mümkün. |

**Ücretsiz / Pro ayrımı (JFC modeli):** Ücretsiz kullanıcı haftalık fırsatları görür. Pro kullanıcı vize filtresi, "vizen bitmeden" bildirimi, bayram planlayıcı, kişisel kalkış noktaları ve anlık hata fiyat bildirimi alır.

### Birim ekonomi (kodla hesaplandı, tüm girdiler [Varsayım])
Rezervasyon başına harmanlanmış affiliate geliri: **3,75 € (kötü) / 5,61 € (orta) / 6,99 € (iyi)**.

| Senaryo | Kurulum (1. yıl) | Aktif kullanıcı | Rez./ay | Affiliate/yıl | Pro/yıl | Toplam gelir | Maliyet (reklam dahil) | Net |
|---|---|---|---|---|---|---|---|---|
| Kötü | 20.000 | 2.000 | 20 | 899 € | 170 € | **1.069 €** | 28.924 € | **−27.855 €** |
| Orta | 60.000 | 9.000 | 135 | 9.088 € | 2.295 € | **11.383 €** | 67.324 € | **−55.941 €** |
| İyi | 150.000 | 30.000 | 600 | 50.328 € | 15.300 € | **65.628 €** | 130.924 € | **−65.296 €** |

Varsayımlar: kurulum başı reklam maliyeti 0,8–1,2 €, sabit gider 400–900 €/ay (sunucu, veri API, içerik), mağaza payı %15.

**Kritik çıkarım:**
- Kurulum başına yıllık gelir **0,19 € (orta) – 0,44 € (iyi)**. Kurulum başına reklam maliyeti ~1 €. **Ücretli kullanıcı edinimiyle geri dönüş 2–5 yıl sürer; bu da fiilen zarar demek.**
- Aynı rakamlar **organik büyümeyle** (reklam yok; Telegram, Instagram ve kulaktan kulağa) şöyle: orta senaryoda **+4.059 €/yıl**, iyi senaryoda **+54.704 €/yıl**.
- **Sonuç [Varsayım, %75 güven]:** Bu iş ancak bir topluluk işi olarak kârlı olur. Önce HolidayPirates/JFC gibi takipçi kazanılır, uygulama sonra gelir. Tersi para yakar.

---

## 6. Sermaye ihtiyacı

| Kalem | Tutar | Etiket |
|---|---|---|
| Apple Developer + Google Play | 99 $/yıl + 25 $ bir kez | [Gerçek] |
| Uygulama geliştirme (Flutter/React Native, dışarıdan) | 8–25 bin € | [Varsayım] |
| Aynı uygulama Erdem + Claude ile | Nakit ~0, zaman 150–300 saat | [Varsayım] |
| Uçuş veri API'si | Travelpayouts verisi partnerlere ücretsiz; Amadeus/Duffel kullanım başı ücretli | [Varsayım] |
| Vize/giriş şartı veri tabanı | Elle derleme veya ücretli API (IATA Timatic vb.) | [Varsayım] |
| Kullanıcı edinimi | Organikse ~0; ücretliyse kurulum başı ~1 € | [Varsayım] |
| Aylık işletme | 400–900 € | [Varsayım] |

**Nakit riski:** Affiliate ödemeleri genellikle rezervasyondan sonra, seyahat tamamlanınca ve birkaç hafta gecikmeyle gelir [Varsayım]. İlk 6–12 ay gelir neredeyse sıfır.

---

## 7. Rekabet avantajı (moat)

Gerçekçi bakınca zayıf, ama sıfır değil:
- **Veri avantajı [Varsayım]:** Vize + giriş şartı + çıkış harcı + bayram takvimi birleşimi kopyalanabilir, ama Enuygun gibi satış odaklı bir oyuncunun önceliği değil.
- **Topluluk ve güven:** JFC ve HolidayPirates'in tek gerçek kalesi bu. Elde edilmesi yıllar sürer.
- **Marka:** "ucuzgez" adı Türkçede kendini anlatıyor. Bu küçük ama gerçek bir avantaj [Varsayım].
- **Zayıflık:** Enuygun isterse vize filtresini 2–3 ayda ekler [Spekülasyon].

---

## 8. Uygulama zorluğu

- **Ekip:** 1 içerik/fırsat avcısı (günde 1–2 saat), 1 geliştirici (Claude destekli Erdem), sosyal medya yönetimi.
- **Lisans:** Sadece yönlendirme yapıldığı sürece TÜRSAB acente lisansı gerekmez [Varsayım; satış yapılırsa gerekir, hukukçuya teyit ettirilmeli].
- **KVKK:** Vize ve pasaport bilgisi kişisel veri. Uygulama bunları sadece cihazda tutmalı, sunucuya göndermemeli [Varsayım: en güvenli tasarım].
- **Süre:** PWA + Telegram botu 2–4 hafta. Mağaza uygulaması 2–4 ay [Varsayım].

---

## 9. Neden işe yarayabilir / Neden başarısız olabilir

**Neden işe yarayabilir**
- Sorun gerçek ve büyüyor: 11,8 milyon yurt dışı çıkış ve süren Schengen krizi [Gerçek].
- Model kanıtlanmış: JFC 30 £ ile başladı, milyonlarca üyeye ulaştı [Gerçek].
- Türkiye'ye özel açı (pasaport, harç, bayram) global oyunculardan korunaklı [Varsayım].
- Erdem'in Bulgaristan/Balkan bilgisi, Sofya çıkışlı rotalar için doğal içerik avantajı sağlıyor [Varsayım].

**Neden başarısız olabilir**
- **Seyahat uygulamalarında kullanıcı tutma çok düşük:** 1. gün %18, 30. gün %2,8 [Gerçek]. İnsanlar seyahat uygulamasını sadece planlarken açar.
- **Türk kullanıcı aboneliğe az para öder:** Türkiye merkezli geliştiricilerin abonelik gelirinin %89'u yurt dışından geliyor [Gerçek]. Bu, yurt içi ödeme isteğinin zayıf olduğuna dair dolaylı bir sinyal [Varsayım].
- **Affiliate komisyonu çok düşük:** Bilet başına ~%1,1 [Gerçek]. Ciddi gelir için on binlerce aktif kullanıcı gerekir.
- **Ücretsiz rakip:** Google Flights fiyat takibi ve bazı uçuşlarda fiyat garantisini bedava veriyor [Gerçek].
- **Fırsat sıklığı:** Kullanıcının kendi tarihine uygun fırsat çıkmayabilir. Going'in yorumlarında bile bu şikâyet var [Gerçek]. Kürasyon modelinin doğal zayıflığı bu.
- **Zaman:** Bu iş günlük içerik ister. Erdem'in "hızlı başla, sonuç gelmezse bırak" eğilimiyle en çok çatışan iş tipi bu.

---

## 10. Riskler ve en büyük bilinmeyenler

1. **Türk kullanıcı vize filtreli fırsat için para öder mi?** En büyük bilinmeyen. Test edilmeden uygulama yazılmamalı.
2. Vize/giriş şartı verisinin doğruluğu: Yanlış bilgi verilirse kullanıcı havalimanında kalır; itibar ve sorumluluk riski doğar.
3. Affiliate programlarına kabul: Skyscanner ve benzerleri trafiği olmayan yayıncıyı reddediyor veya oranı düşürüyor [Gerçek].
4. TL dalgalanması: Gelir euro, kullanıcı fiyatı TL. Pro fiyatı sık güncellenmeli.

---

## 11. Alternatifler (aynı emekle daha iyi ne yapılır?)

- **A — Uygulama yok, Telegram + site (önerilen):** Aynı farklılaşma (vize etiketi, toplam maliyet, bayram planı) içerik olarak verilir. Maliyet ~0, öğrenme hızı maksimum.
- **B — Telegram botu:** Kullanıcı vizesini ve kalkış ilini bota yazar, kişisel fırsat alır. Uygulama mağazası, onay süreci ve %15 mağaza payı yok. Uygulamanın %70'i, emeğin %10'u [Varsayım].
- **C — PWA:** Sitenin "ana ekrana ekle" versiyonu. Push bildirimleri iOS'ta da destekleniyor [Varsayım: iOS 16.4+ web push; teyit edilmeli].
- **D — Bu zamanı HPP/Vitrexia satışına vermek:** 1. kademe öncelik. 150–300 saatlik uygulama emeği, oralarda doğrudan gelir üretir.

---

## 12. En hızlı doğrulama deneyi (≤ 4 hafta, ≤ 50 €)

1. Telegram kanalında her fırsata 3 etiket ekle: **🟢 Vizesiz / 🟡 e-Vize-kapıda / 🔵 Schengen gerekli** ve **"kapıdan kapıya TL"** satırı (harç dahil).
2. Bir hafta "Sofya çıkışlı" özel paylaşım ve bir "bayram/köprü" paylaşımı yap.
3. Kanala sabitlenmiş Tally/Google Form koy: *"Elindeki vizeye göre kişisel fırsat bildirimi — Pro, yılda 499 TL. Ön kayıt ol, açılınca ilk ay bedava."*
4. Bütün linkleri Travelpayouts affiliate linkine çevir ve tıklamaları ölç.

**Ölçülecekler:** abone artışı, etiketli ve etiketsiz paylaşımların tıklama farkı, Pro ön kayıt sayısı.

---

## 13. Öldürme kriterleri

| 6 hafta sonunda | Karar |
|---|---|
| Telegram abonesi < 300 **ve** Pro ön kaydı < 20 | Uygulama fikri tamamen kapanır. Ucuzgez statik sayfa + kanal olarak pasif kalır. |
| Etiketli paylaşımların tıklaması, etiketsizlerden belirgin şekilde yüksek değil | "Pasaporta göre fırsat" farkı tutmuyor demektir. Fikir kapanır. |
| Abone ≥ 1.000, Pro ön kaydı ≥ 50, affiliate'ten ilk gelir | Telegram botu (Alternatif B) yapılır. Uygulama hâlâ yapılmaz. |
| Bot 6 ayda 5.000+ aktif kullanıcı ve ödeme yapan Pro üye getirir | Ancak o zaman mağaza uygulaması konuşulur. |

---

## 14. Başlarsa ilk 30 gün

- **1. hafta:** Travelpayouts hesabı (Aviasales + Airalo), site ve kanal linklerinin affiliate'e çevrilmesi, vize etiketi şablonu.
- **2. hafta:** Türk pasaportu giriş şartları tablosu (ilk 40 popüler rota), çıkış harcı dahil toplam maliyet hesaplama şablonu.
- **3. hafta:** İlk "Sofya çıkışlı" ve "2027 bayram/köprü" içerikleri, Pro ön kayıt formu.
- **4. hafta:** Ölçüm, öldürme kriterlerine göre karar.
- **Haftalık zaman sınırı:** 2–3 saat. Bunu aşarsa HPP/Vitrexia'dan zaman çalıyor demektir.

---

## 15. Mevcut önceliklere etkisi

- Uygulama geliştirme (150–300 saat) **HPP ve Vitrexia'dan doğrudan zaman çalar. Bu yüzden şu an kabul edilemez.**
- Önerilen test (haftada 2–3 saat, mevcut haftalık tarama düzenine eklenerek) 2. kademe sınırları içinde kalır.

---

## 16. Güven tahmini

- "Uygulamayı şimdi yazmak para ve zaman kaybettirir": **%85**
- "Vize/pasaport odaklı farklılaşma, TR'de gerçek bir boşluk": **%60** (rakip taraması sınırlı; Enuygun'un ve küçük kanalların vize filtresi olup olmadığı tek tek doğrulanmadı)
- "Organik toplulukla iyi senaryoya (30 bin aktif) ulaşmak": **%10–15**
- Birim ekonomi rakamları: kaba tahmin, **±%50 hata payı**

---

## Kaynaklar
- Going: https://get.going.com/flight-alerts-and-tools/ · https://www.going.com/?id=322 · https://www.trustpilot.com/review/going.com?page=2 · https://dk.trustpilot.com/review/going.com · https://www.groupon.com/coupons/going
- Hopper: https://techcrunch.com/?p=2330381 · https://future.a16z.com/hoppers-big-bet-all-travelers-worry-but-not-about-the-same-thing/ · https://techcrunch.com/?p=3138693 (FTC 35 M $) · https://www.businessofapps.com/?p=83179
- Jack's Flight Club: https://en.wikipedia.com/wiki/Jack%27s_Flight_Club · https://ui.awin.com/merchant-profile/12296?setLocale=pl_PL · https://dev.jacksflightclub.com/partnerships
- HolidayPirates: https://www.urlaubspiraten.de/partner · https://www.reutersevents.com/travel/node/59943
- Enuygun: https://www.enuygun.com/hakkinda/ · https://www.turkiyesigorta.com.tr/turkiye-sigorta-musteri-platformu/musteri-platformu-is-ortakliklarimiz/seyahat-ulasim/enuygun/en-uygun-ucak-bileti-indirimi · https://www.enuygun.com/kullanim-kurallari/
- Google Flights fiyat garantisi: https://support.google.com/travel/answer/9430556
- Affiliate: https://travelpayouts.com/en/offers/aviasales-affiliate-program · https://www.travelpayouts.com/blog/skyscanner-flight-affiliate-program/amp/ · https://www.travelpayouts.com/blog/?p=15465 · https://www.airalo.com/m/resources/airalo-affiliate-program
- DHMİ 2025: https://www.dha.com.tr/politika/bakan-uraloglu-hava-yolu-ile-seyahat-eden-yolcu-sayisinda-rekor-kirdik-2793107
- Vize: https://www.24saatgazetesi.com/vize-krizi-turizmi-vurdu-turkler-avrupa-yerine-uzakdoguya-yoneliyor · https://www.haberturk.com/turkiye-schengen-vize-basvurusunda-ikinci-sirada-3888002-ekonomi · https://gazeteoksijen.com/turkiye/tursabdan-schengen-vizesi-uyarisi-randevular-1000-euroya-satiliyor-bu-duruma-dur-denilmeli-277178 · https://www.posta.com.tr/galeri/turk-vatandaslarinin-2026da-vizesiz-gidebilecegi-rotalar-liste-guncellendi-tam-78-ulke-var-2951581 · https://www.karar.com/guncel-haberler/vize-derdi-bitti-sadece-kimlikle-veya-pasaportla-gidilebilen-103-ulke-2082431
- Çıkış harcı: https://www.enuygun.com/bilgi/yurt-disi-cikis-harci-nedir · https://www.yeniasir.com.tr/ekonomi/2026/11/03/yurt-disi-cikis-harci-ne-kadar-olacak
- Uygulama tutma: https://www.businessofapps.com/?p=97743 · https://uxcam.com/blog/mobile-app-retention-benchmarks/
- TR abonelik geliri: https://www.foreks.com/haber/detay/6ae1ac87422c786f3f7ab76d/FRKS/tr/revenuecat-in-eylul-2025-agustos-2026-raporuna-gore-turk-mobil-uygulamalarinin-abonelik-gelirlerinin-yuzde-89-u-yurt-disindan-geliyor-28-10-26/
