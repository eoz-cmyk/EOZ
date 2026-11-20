# Günün fikri — "Balkan İhale Radarı": Türk firmalarına Bulgaristan / Romanya / Yunanistan kamu ihalelerini Türkçe özetleyen ücretli Telegram kanalı

**Tarih:** 2026-11-20 · **Hazırlayan:** Günlük fikir ajanı · **Mod:** kısa araştırma (derin değil)
**Not:** Bu çalıştırma, Erdem'in tek seferlik yönlendirmesiyle "ücretli Telegram bildirim grubu" alanından seçildi.

**Tek cümle:** AB'nin resmi ihale bülteni TED'in ücretsiz API'sinden ve Bulgaristan ile Romanya'nın ulusal ihale portallarından her gün ilanları çeken bir sistem. İnşaat, yapı malzemesi, ahşap/MDF, makine ve temizlik gibi Türk firmalarının rekabet edebildiği alanlara göre filtreler, yapay zekâyla Türkçe özetler ve aylık abonelikle sektör bazlı Telegram kanallarına gönderir.

| Kategori | Sınır | Öneri |
|---|---|---|
| online (TR müşteri, BG/RO/GR veri) | içinde | **DEVAM ET**, önce 4 haftalık ücretsiz pilot kanalla talep testi |

## Skor

| Hız | Sermaye | Kâr | Exit | "Neden aklıma gelmedi" | Toplam |
|---|---|---|---|---|---|
| 4 | 5 | 3 | 2 | 4 | **18/25** |

- **Hız 4:** Veri kaynağı hazır ve ücretsiz. İlk kanal 2–3 haftada kurulabilir [Varsayım].
- **Sermaye 5:** Sunucu, yapay zekâ çeviri maliyeti ve ödeme altyapısı aylık birkaç yüz €'yu geçmez [Varsayım].
- **Kâr 3:** Marj yüksek, ama abone sayısı sınırlı bir B2B kitleye bağlı [Varsayım].
- **Exit 2:** Küçük bir abone tabanı ancak bir ihale bilgi platformuna ya da danışmanlık firmasına satılabilir [Spekülasyon].

## Elenen adaylar (aynı alanda)

| Aday | Skor | Neden elendi |
|---|---|---|
| EKAP yurt içi ihale filtre kanalı | 13/25 | EKAP'ın kendi bildirimleri ve mevcut ücretli ihale takip uygulamaları var. Fark yaratmak zor. |
| İcra ve Milli Emlak gayrimenkul satış bildirimi (Eskişehir) | 14/25 | ilan.gov.tr ve mevcut uygulamalar bu işi yapıyor. Kişisel veri (borçlu bilgisi) riski var. |
| Kalkınma ajansı ve KOSGEB hibe çağrıları özeti | 14/25 | Kitlenin ödeme isteği düşük. Danışmanlar bu bilgiyi zaten ücretsiz dağıtıyor. |
| İhracat alım talepleri (ataşelik, B2B siteleri) | 15/25 | Kaynakların çoğu üyelik istiyor ve yeniden dağıtım hakkı belirsiz. |

## Pazar sinyali
- **[Gerçek]** TED verisi, Komisyonun açık veri politikası (2011/833/AB) kapsamında kaynak gösterilerek ticari amaçla da ücretsiz kullanılabilir. Resmi Search API v3 anonim erişime açık.
- **[Gerçek]** TED, yalnızca AB eşiklerinin üzerindeki ihaleleri kapsar. Daha küçük ihaleler için ulusal portallar gerekir: Bulgaristan'da CAIS EOP, Romanya'da SEAP.
- **[Gerçek]** Ticaret Bakanlığı'nın 2026 Bulgaristan raporuna göre 2025'te Bulgaristan'da inşaat alanında 6.384 kamu sözleşmesi imzalandı, toplam değeri 4,79 milyar €. Bulgaristan inşaat siciline kayıtlı Türk firma sayısı 18.
- **[Gerçek, şirket açıklaması]** Makyol'un Romanya CEO'suna göre Türk müteahhitlerin Romanya'daki proje sayısı 231, toplam değeri 15,2 milyar $'ı aşıyor. IC İçtaş, Romanya'da 420 milyon €'luk bir demiryolu sözleşmesi imzaladı.
- **[Gerçek, haber]** AB'nin Çinli firmaları kamu ihalelerinden uzak tutması Romanya'da Türk firmalarına alan açtı.
- **[Varsayım]** Büyük müteahhitlerin kendi ihale ekipleri var. Asıl hedef, Balkan ihalelerini takip edecek personeli olmayan KOBİ'ler: yapı malzemesi ve MDF tedarikçileri, taşeronlar, makine kiralama ve temizlik firmaları. Bu kitle EOZ'daki MDF TR→BG takibiyle de örtüşüyor.

## Benzer örnekler
- **[Gerçek]** Apify gibi platformlarda TED verisini CPV koduna ve ülkeye göre süzen çok sayıda hazır araç var. Teknik engel düşük.
- **[Varsayım]** TendersOnTime ve Tender Impulse gibi uluslararası ihale bilgi servisleri İngilizce, pahalı ve Türk KOBİ'sine göre filtrelenmemiş. Türkçe ve sektöre göre süzülmüş bir Telegram kanalına rastlanmadı. Bu doğrulanmadı, ilk haftanın işi.

## Gelir modeli [Varsayım]
- **Fiyat:** Sektör kanalı başına aylık 40–60 € (yaklaşık 2.000–3.000 TL). Bütün sektörler için 100 €.
- **Hedef:** Ayda 3.000 € net için yaklaşık 60–75 abone gerekir. 10.000 € için yaklaşık 200 abone. Türkiye'deki ihracatçı KOBİ sayısı düşünülünce 60–75 abone ulaşılabilir görünüyor, 200 için güçlü bir satış kanalı gerekir.
- **Ek gelir:** Abonelere "bu ihaleye nasıl girilir" danışmanlığı ya da Bulgaristan'daki yerel ortaklarla eşleştirme için komisyon [Spekülasyon].

## Otomasyon nasıl kurulur
1. Her sabah zamanlanmış görev TED Search API v3'ü sorgular: ülke BG, RO ve GR; CPV kodları 45 (inşaat), 44 (yapı malzemesi), 03.41 / 44.19 (ahşap), 90 (temizlik).
2. Bulgaristan ve Romanya ulusal portalları API ya da RSS ile, yoksa sayfa okuma ile eklenir. Bu adım ikinci aşamaya kalabilir.
3. Yapay zekâ her ilanı 4–5 satırlık Türkçe özete çevirir: ne, nerede, tahmini bedel, son teklif tarihi, şartnamede Türk firması için kritik şart. Altına orijinal link konur.
4. Özetler sektöre göre ayrı Telegram kanallarına gönderilir. Bot, şu an kullandığımız `araclar/telegram_gonder.sh` mantığıyla aynı.
5. Ödeme: Türkiye'de iyzico veya PayTR ile abonelik ve e-fatura. Ödeyen kişi Telegram botuyla kanala eklenir, ödeme bitince çıkarılır. Alternatif olarak Telegram Stars kullanılabilir.

## Hukuki riskler
- **[Gerçek]** TED verisinin ticari yeniden kullanımı serbest, kaynak gösterilmesi şart.
- **[Varsayım]** Bulgaristan ve Romanya ulusal portallarının kullanım şartları ayrı ayrı okunmalı. Sayfa okuma yasaklıysa yalnızca resmi API veya açık veri kullanılır.
- **[Gerçek]** Ücretli abonelik satmak ticari faaliyettir. Şahıs şirketi ya da mevcut bir şirket üzerinden faturalandırılmalı.
- **[Varsayım]** Kişisel veri riski düşük. İhale ilanlarında kurum bilgisi var, gerçek kişi bilgisi neredeyse yok. Abone listesi için KVKK aydınlatma metni yeterli.
- **[Varsayım]** "Bu ihaleyi kazanırsınız" gibi vaatler verilmemeli. Hizmet bilgi derlemesi olarak konumlanmalı.

## İlk 30 günde ne yapılır
1. **1. hafta:** TED API'den BG, RO ve GR için son 30 günün inşaat ve yapı malzemesi ilanlarını çek. Hacmi ölç: günde kaç ilan geliyor? Türkçe özet formatını belirle.
2. **2. hafta:** Ücretsiz pilot Telegram kanalı aç. MDF takip dosyasındaki bağlantılar ve sektör dernekleri üzerinden 30–50 kişi davet et.
3. **3–4. hafta:** Pilot kullanıcılardan 10'una "ayda 50 € öder misiniz?" diye sor. Karar eşiği: en az 5 kişi "evet" derse ödeme altyapısını kur ve fiyatı aç.

## En büyük risk
Talep. Türk KOBİ'leri Balkan ihalelerine girmekte isteksiz olabilir: dil, teminat mektubu, yerel ortak ihtiyacı ve AB belgeleri. Bilgiyi alsalar da teklif vermiyorlarsa aboneliği iptal ederler [Spekülasyon]. Pilotun ölçmesi gereken asıl şey bu.

## Exit yolu
Abone tabanı ve kurulu otomasyon, bir ihale bilgi platformuna, Balkanlara açılmak isteyen bir danışmanlık firmasına ya da bir ihracatçı birliğine satılabilir. Daha gerçekçi yol, yan gelir olarak tutup danışmanlık ve ortak eşleştirme işine kanal olarak kullanmak [Spekülasyon].

## Kaynaklar
- Avrupa Komisyonu, Tenders Electronic Daily: https://single-market-economy.ec.europa.eu/single-market/public-procurement/digital-procurement/tenders-electronic-daily_en
- TED RSS: https://ted.europa.eu/en/simap/rss-feed/-/rss/search/mior
- Apify, TED Tenders (resmi API, yeniden kullanım şartları): https://apify.com/clearsource/ted-tenders
- Open Contracting, Bulgaristan OpenTender: https://data.open-contracting.org/en/publication/44
- Open Contracting, Romanya OpenTender: https://data.open-contracting.org/en/publication/75
- T.C. Ticaret Bakanlığı, 2026 Bulgaristan Müteahhitlik ve Teknik Müşavirlik Sektörü Raporu: https://ticaret.gov.tr/data/656094bf13b8762630b82fa0/2026 Bulgaristan Muteahhitlik ve Teknik Musavirlik Sektoru Raporu.pdf
- Bloomberg HT, Makyol Romanya: https://www.bloomberght.com/makyol-insaat-tan-romanyada-3-milyar-euroluk-altyapi-3761179
- Ekonomi Gazetesi, Çin karşıtı politika ve Makyol: https://www.ekonomigazetesi.com/sirket-haberleri/cin-karsiti-politika-makyolu-romanyada-lider-yapti-64176
- Habertürk, IC İçtaş Romanya: https://www.haberturk.com/ic-ictas-romanya-da-420-milyon-euro-luk-ihale-kazandi-3846487-ekonomi
- Kamu İhale Kurumu (e-Devlet): https://www.turkiye.gov.tr/kamu-ihale-kurumu
- İhale Bulucu (App Store, yurt içi rakip örneği): https://apps.apple.com/app/id6502546343
