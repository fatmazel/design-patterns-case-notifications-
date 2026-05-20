### Bildirim Sisteminde Factory Method Deseni Kullanımı ve Mimari İyileştirmeler
Bu çalışmada, notification_system.py dosyası içerisinde yer alan bildirim mekanizmasının nesne üretim süreçleri, Factory Method tasarım deseni kullanılarak iyileştirilmiştir.

### Mevcut Yapıdaki Problemler
Eski sistemde (NotificationManager.send_notification metodu), tüm bildirim türlerinin üretimi tek bir merkezde toplanmıştı. Her yeni bildirim kanalı (email, sms, push vb.) eklendiğinde if-else bloklarının uzaması gerekiyordu. Bu yaklaşım iki temel soruna yol açıyordu:

Kodun Kırılganlığı: Yeni bir özellik eklemek, halihazırda çalışan ve test edilmiş ana koda müdahale etmeyi gerektiriyordu. Bu da beklenmeyen hatalara zemin hazırlıyordu.

Sorumlulukların Karışması: SMS için 160 karakter sınırı gibi yalnızca belirli bir kanala özgü kurallar, genel yönetici sınıfının içinde birikerek kodun karmaşıklaşmasına ve şişmesine neden oluyordu.

### Factory Method ile Yapılan İyileştirmeler
Sistemdeki nesne üretim sorumluluğu NotificationFactory sınıfına devredilerek süreç ana akıştan ayrıştırıldı. Dinamik bir yapı kurmak adına sistem iki temel işlev üzerinden kurgulandı:

register_notification: Sisteme dahil edilen yeni bildirim kanallarının fabrikaya tanıtılmasını sağlar.

create_notification: İstemcinin (client), "email" veya "sms" gibi anahtar kelimeler göndererek ilgili nesnenin üretilmesini talep ettiği fonksiyondur.

Bu sayede istemci tarafı; EmailNotification veya SMSNotification gibi somut (concrete) sınıflarla doğrudan iletişim kurmak yerine, işlemini sadece parametre geçirerek soyut bir katman üzerinden halledebilir hale gelmiştir.

### Mimari Kazanımlar
Uygulanan kayıt (registry) mantığı sayesinde sistem esnek ve genişletilebilir bir yapıya kavuşmuştur. Örneğin, ileride sisteme WhatsApp bildirimleri entegre edilmek istendiğinde mevcut kodlarda hiçbir değişiklik yapılmasına gerek kalmayacaktır. Yalnızca yeni sınıfı oluşturup fabrikaya kaydetmek yeterli olacaktır.

Bu refactoring işleminin yazılım prensipleri (SOLID) açısından temel kazanımları şunlardır:

Açık/Kapalı Prensibi (OCP): Sistem, yeni bildirim kanalları eklemeye (gelişime) açık; mevcut kodları değiştirmeye (değişime) kapalı hale getirilmiştir.

Tek Sorumluluk Prensibi (SRP): Nesne üretim işi fabrikaya, bildirim gönderim kuralları ise ilgili sınıfların kendisine bırakılarak sınıf sorumlulukları ayrıştırılmıştır.

Bağımlılıkların Tersine Çevrilmesi Prensibi (DIP): Ana sistem somut sınıflara değil, genel bir "Notification" soyutlamasına bağımlı hale getirilmiştir.