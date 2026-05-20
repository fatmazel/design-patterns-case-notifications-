# Faz 3: Behavioral Patterns - AI Log

## 1. AI'ya Sorulan Soru (Prompt)
Bildirim sistemime olay tabanlı bir izleme mekanizması eklemek
istiyorum. Ayrıca farklı gönderim stratejilerini (anlık, toplu)
esnek bir şekilde yönetmek istiyorum. Hangi Behavioral örüntüleri
kullanmalıyım?

## 2. AI Yanıtının Özeti
AI üç örüntü önerdi:

**Observer:** Bildirim olaylarını izlemek için yayıncı-abone modeli.
NotificationEventManager yayıncı görevi görüyor, EmailObserver ve
SMSObserver ise abone olarak olayları dinliyor.

**Strategy:** Farklı gönderim davranışlarını kapsüllemek için.
ImmediateSendStrategy anlık gönderim, BatchSendStrategy ise mesajları
kuyruğa alıp toplu gönderim yapıyor. NotificationContext runtime'da
strateji değiştirebiliyor.

**Chain of Responsibility:* Bir isteği, işleyici (handler) nesnelerinden oluşan bir zincir boyunca sırayla iletmek için. Her bir işleyici gelen isteği değerlendirir; ya kendi işleyip süreci sonlandırır ya da zincirdeki bir sonraki halkaya devreder. Böylece isteği gönderen ile işleyen arasındaki bağımlılık ortadan kalkar.

## 3. AI'ın Yanlış veya Eksik Önerdiği Şeyler
Sunulan önerilerde teknik bir hata veya eksiklik tespit edilmemiştir. Ancak, Chain of Responsibility tasarım örüntüsünün projenin mevcut kapsamı doğrultusunda bu aşamada gerekli olmadığı değerlendirilmiştir

## 4. Uygulama ve Kararlar
Kod yapısına uygunlukları ve temel gereksinimleri karşılamaları sebebiyle Observer ve Strategy örüntülerinin projeye entegre edilmesine karar verilmiştir. Öte yandan, Chain of Responsibility örüntüsünün mevcut aşamada sisteme gereksiz bir karmaşıklık katacağı sonucuna varılarak uygulanmasından vazgeçilmiştir.