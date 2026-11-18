# Günlük fikir ajanı — tasarım

**Son güncelleme:** 2026-11-18 · **Durum:** kuruluyor

## Amaç
Erdem'in aklına gelmemiş, hızlı geri dönüşlü, kârlı ve exit ihtimali olan iş/yatırım fikirlerini her gün bir tane bulup Telegram'dan bildirmek; Erdem "devam / park / red" der.

## Hedefler / hedef olmayanlar
- Hedef: günde 1 fikir, kısa ve etiketli rapor, tekrar etmeyen öneriler (fikir havuzu).
- Hedef değil: derin araştırma (seçilen fikir `devam` alırsa ayrıca yapılır), HPP / Vitrexia içeriği.
- Başarısızlık sayılır: klişe veya tekrar eden fikirler, kaynaksız iddialar.

## Yaklaşımlar
1. **Her sabah yeni oturum (seçildi):** temiz bağlam, havuz dosyası hafıza işlevi görür. Erdem'in cevabı o an açık oturuma düşmezse ertesi sabahki mesaj bekleyen kararları hatırlatır.
2. Hep aynı oturumda çalışmak: cevaplar doğrudan gelir ama oturum şişer, uzun vadede kırılgan.

## Kurulum
- Zamanlama: her gün 08:00 Europe/Istanbul, her çalıştırmada yeni oturum.
- Talimat: `notlar/fikir-ajani-talimat.md` · Havuz: `notlar/fikir-havuzu.md` · Gönderim: `araclar/telegram_gonder.sh`
- Sınır dışı fikirler atılmaz; etiketlenir ve nasıl yapılabilir hale geleceği yazılır.
