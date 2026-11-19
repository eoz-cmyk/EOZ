# Schengen 90/180 gün takibi

**Kademe:** 3 (kişisel takip) · **Son güncelleme:** 2026-11-19

## Son durum (19.11.2026 itibarıyla)
- Pasaport: TC yeşil (hususi) pasaport, Schengen'e vizesiz. Kural: herhangi bir günde son 180 günde en fazla 90 gün. (Gerçek)
- Oturum izni yok, yani Bulgaristan dahil her Schengen günü sayılır. (Gerçek, Erdem'in beyanı)
- Son 180 günde kullanılan: **23 gün** · Kalan: **67 gün** (hesap: `araclar/schengen_90_180.py`)
- Bugün girersen en geç çıkış: **01.02.2027** (Temmuz seyahati Ocak ortasında pencereden düşüyor)
- Google Sheets (formüllerle kendisi hesaplar): https://docs.google.com/spreadsheets/d/1J6pIOsDL1OsUVu9Yqp9tD5-A8ms31zZ3TLgCPF8ZYsQ/edit
- Not: Sheets düzenleme bağlayıcısı açık değil, Claude tabloya satır ekleyemiyor. Erdem satır ekler ya da bağlayıcı açılır. Bu dosya ile tablo elle senkron tutulur.

## Sıradaki adım
- Her giriş/çıkışta bu tabloya bir satır (veya Erdem mesajı → Claude işler).
- Uçuşlar: bilet e-postaları bağlı Gmail'e alınacak ya da iletilecek, haftalık taranacak.

## Seyahatler
Giriş/çıkış günleri tam gün sayılır. İçerideysen çıkış boş kalır.

| Giriş | Çıkış | Ülke | Nasıl | Not |
|---|---|---|---|---|
| 2026-07-11 | 2026-07-18 | BG |  |  |
| 2026-10-04 | 2026-10-10 | BG |  |  |
| 2026-10-16 | 2026-10-23 | BG |  | Mesajda "bf" yazıyordu, BG varsayıldı (Varsayım) |

## Kurallar ve notlar
- Schengen'e dahil: Bulgaristan ve Romanya (Ocak 2025'ten beri tam üye). (Gerçek)
- Sayılmaz: Türkiye, Kıbrıs (AB üyesi ama Schengen dışı), İrlanda, İngiltere, Gürcistan. (Gerçek)
- EES ile pasaporta damga basılmıyor, giriş/çıkış biyometrik kaydediliyor. Fazla kalış otomatik tespit edilir. (Gerçek)
- Bu kayıtlar EES'teki resmi kaydın yerine geçmez. Sınırda tartışma olursa resmi kayıt esas alınır. (Varsayım)

## Kaynaklar
- AB Komisyonu, kısa süreli kalış hesaplayıcı: https://home-affairs.ec.europa.eu/policies/schengen-borders-and-visa/border-crossing_en
- EES resmi sayfası: https://travel-europe.europa.eu/ees_en
- Konsey kararı, Bulgaristan ve Romanya'nın tam Schengen üyeliği (1 Ocak 2025)
