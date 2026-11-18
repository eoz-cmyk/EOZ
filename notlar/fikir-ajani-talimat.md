# Günlük fikir ajanı — talimat

Bu dosya her sabah 08:00'de (Europe/Istanbul) çalışan ajanın talimatıdır. Değişiklik gerekirse burayı düzenle; zamanlanmış görev bu dosyayı okur.

## Kimin için, ne arıyoruz
Erdem için, **aklına gelmemiş** yatırım veya iş fikirleri. Aradığı:
- Duyunca "bu neden daha önce aklıma gelmedi" dedirten işler
- Hızlı ve kolay geri dönüş; kâr potansiyeli yüksek; hızlı aksiyon alınabilir; kârlı exit ihtimali olan
- Online iş **veya** Türkiye / Bulgaristan'da yerleşik iş
- İstisna: araştırmada "geleceğin işi" olacak bir fikir çıkarsa kriterlere tam uymasa da bildir (kategori: `gelecek`)

Varsayılan sınırlar (Varsayım, Erdem düzeltebilir): ≤50 bin € sermaye, ≤6 ayda ilk gelir, haftada birkaç saat zaman (HPP ve Vitrexia 1. kademe). Sınırı aşan fikir **atılmaz**: `sınır dışı` etiketlenir, hangi sınırı aştığı ve nasıl yapılabilir hale gelebileceği (ortak, pilot, teşvik/kredi, sadece bir parçası) yazılır.

## Her çalıştırmada adımlar
1. `git pull` (main). `notlar/fikir-havuzu.md`, `takip/` ve `arastirma/` başlıklarını oku.
2. **Bekleyen kararlar:** havuzda durumu `yeni` olan fikirleri listele (Telegram mesajının sonuna bir satırlık hatırlatma olarak eklenecek).
3. **Yeni fikir bul:** havuzda, takip dosyalarında, HPP ve Vitrexia kapsamında olmayan **tek** bir fikir. Önce geniş tara (yeni düzenlemeler, teşvikler, TR/BG'de arz açığı olan hizmetler, yurt dışında tutup TR/BG'de henüz olmayan modeller, yeni teknolojinin açtığı küçük nişler), 3–5 aday çıkar, skorla, en iyisini seç. Bariz/klişe fikirleri ele (dropshipping, genel kafe, genel YouTube vb.).
4. **Kısa araştırma** (derin değil): pazar sinyali, benzer örnekler, tahmini sermaye ve getiri, ilk 30 günde ne yapılır, en büyük risk, exit yolu. Her bilgi **Gerçek / Varsayım / Spekülasyon** etiketli; kaynaklar sonda.
5. Raporu `arastirma/YYYY-MM-DD-fikir-<kisa-konu>.md` olarak yaz (1–2 sayfa). Başta: tek cümle fikir, kategori, sınır, skor tablosu, öneri (DEVAM ET / PARK / YAPMA).
6. Havuza satır ekle (durum `yeni`), "Son güncelleme" tarihini güncelle.
7. Commit + `git push origin main` (Erdem'in onayıyla günlük kayıtlar doğrudan main'e gider).
8. Telegram özeti gönder: `bash araclar/telegram_gonder.sh "<mesaj>"`. Biçim (6–8 satır, düz metin):
   ```
   💡 Günün fikri (GG.AA): <fikir adı>
   Ne: <tek cümle>
   Neden şimdi: <tek cümle>
   Sermaye / getiri: <tahmin> [Varsayım]
   En büyük risk: <tek cümle>
   Kategori · Sınır · Skor: <online|TR|BG|gelecek> · <içinde|sınır dışı: ...> · <x>/25
   Rapor: https://github.com/eoz-cmyk/EOZ/blob/main/<yol>
   Cevap: "devam" / "park" / "red"
   ⏳ Bekleyen: <varsa önceki yeni fikirler, yoksa satırı yazma>
   ```

## Erdem'in cevabı geldiğinde (herhangi bir oturum)
"devam / park / red" (gerekirse fikir adıyla) gelince havuzdaki durumu güncelle, Karar notlarına bir satır ekle, commit + push. `devam` ise `takip/<proje-adi>.md` dosyası aç (son durum, sıradaki adım, son güncelleme).
