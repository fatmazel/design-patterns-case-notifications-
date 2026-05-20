# Faz 2: Structural Patterns - AI Log

## 1. AI'ya Sorulan Soru (Prompt)
Mevcut bildirim sistemindeki temel sınıfları değiştirmeden,
bildirimlere Şifreleme ve Loglama gibi ek özellikler kazandırmak
istiyorum. Ayrıca farklı metod isimlerine sahip üçüncü taraf bir
SMS servisini sisteme nasıl entegre edebilirim?
Hangi yapısal örüntüleri kullanmalıyım?

## 2. AI Yanıtının Özeti
AI üç örüntü önerdi:
- Adapter: Üçüncü taraf LegacySmsLibrary entegrasyonu için
- Decorator: Şifreleme ve loglama özelliklerini dinamik eklemek için
- Facade: Tüm sistemi tek noktadan yönetmek için

## 3. AI'ın Yanlış veya Eksik Önerdiği Şeyler

Örnek: "AI başlangıçta Decorator zincirinde loglama sırasını yanlış
kurdu. Gönderimden önce log atıyordu, oysa henüz gönderilmemişti.
Bunu fark edip düzelttim."

## 4.Uygulama ve Kararlar
Alternatif seçenekleri inceledikten sonra bu 3 örüntünün gerekli 
ve yeterli olduğuna karar verdim.

**Adapter:** Üçüncü taraf LegacySmsLibrary kütüphanesinin metod 
isimleri ve parametre sırası sistemimizle uyumsuzdu. Kütüphaneyi 
değiştirmeden entegre etmek için Adapter biçilmiş kaftandı.

**Decorator:** Şifreleme ve loglama özelliklerini mevcut sınıflara 
dokunmadan dinamik olarak eklemek gerekiyordu. Kalıtım kullansaydım 
her kombinasyon için yeni sınıf açmam gerekirdi — Decorator bunu 
çok daha esnek çözdü.

**Facade:** Factory, Decorator zinciri ve gönderim adımları bir 
arada karmaşık bir pipeline oluşturuyordu. Facade ile tüm bu 
karmaşıklığı tek bir metod arkasına gömdük, istemci kodu 
sadeleşti.