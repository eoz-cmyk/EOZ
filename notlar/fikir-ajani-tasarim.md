# Günlük fikir ajanı — tasarım

**Son güncelleme:** 2026-11-18 · **Durum:** çalışıyor (ilk düzenli çalıştırma 2026-11-19)

## Amaç
Erdem'in aklına gelmemiş, hızlı geri dönüşlü, kârlı ve exit ihtimali olan iş/yatırım fikirlerini her gün bir tane bulup Telegram'dan bildirmek; Erdem "devam / park / red" der.

## Hedefler / hedef olmayanlar
- Hedef: günde 1 fikir, kısa ve etiketli rapor, tekrar etmeyen öneriler (fikir havuzu).
- Hedef değil: derin araştırma (seçilen fikir `devam` alırsa ayrıca yapılır), HPP / Vitrexia içeriği.
- Başarısızlık sayılır: klişe veya tekrar eden fikirler, kaynaksız iddialar.

## Yaklaşımlar
1. Her sabah yeni oturum (ilk seçim): denendi; görevin açtığı yeni oturumlara depo eklenemediği için push 403 verdi. Bırakıldı.
2. **Depolu, kalıcı tek oturum (şu an):** görev her sabah aynı oturuma ("Günlük fikir ajanı (kalıcı)") mesaj atar; depo erişimi var. Hafıza yine havuz dosyasında; oturum bağlamı zamanla özetlenir. Erdem'in cevabı açık bir oturuma düşmezse ertesi sabahki mesaj bekleyen kararları hatırlatır.

## Kurulum
- Zamanlama: her gün 07:45 Europe/Istanbul (mesaj ~08:00'de gelir), kalıcı oturuma.
- Talimat: `notlar/fikir-ajani-talimat.md` · Havuz: `notlar/fikir-havuzu.md` · Gönderim: `araclar/telegram_gonder.sh`
- Sınır dışı fikirler atılmaz; etiketlenir ve nasıl yapılabilir hale geleceği yazılır.
