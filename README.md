```markdown
# Discord 7/24 Voice Bot

Bu proje, Discord sunucularında ses kanalları arasında geçiş yapmanızı sağlayan bir bot içerir. Bot, belirli bir sunucuda ses kanalına bağlanır ve bağlı olduğu süreyi güncelleyerek kullanıcıya bilgi verir.

## Özellikler

- Sunucuları ve ses kanallarını listeleme
- Seçilen ses kanalına bağlanma ve kanalda kalma süresini güncelleme
- Belirli bir zaman aralığında bağlantıyı kontrol etme ve yeniden bağlanma

## Kurulum

### Gereksinimler

- Python 3.8 veya daha yeni bir sürüm
- Bir Discord bot token'ı (Bot oluşturmak ve token almak için [Discord Developer Portal](https://discord.com/developers/applications) kullanabilirsiniz)

### Adımlar

1. Bu projeyi klonlayın veya zip dosyasını indirin.
   
   ```bash
   git clone https://github.com/kullanici-adi/discord-7-24.git
   cd discord-voice-channel-switcher
   ```

2. Gerekli Python paketlerini yükleyin.

   ```bash
   pip install -r requirements.txt
   ```

3. `config.json` dosyasını açarak Discord bot token'ınızı girin.

   ```json
   {
       "token": "ACC-TOKEN"
   }
   ```

4. Botu çalıştırın.

   ```bash
   python main.py
   ```

## Kullanım

Bot çalıştırıldığında, komut satırında sunucu ve ses kanalı seçme seçenekleri sunulacaktır. Gerekli seçimleri yaptıktan sonra bot, seçilen ses kanalına bağlanacak ve bağlı kalma süresini belirli aralıklarla güncelleyerek kullanıcıya bilgi verecektir.

## Katkıda Bulunma

Katkıda bulunmak için, lütfen bir `pull request` gönderin. Her türlü geri bildiriminiz ve öneriniz için teşekkür ederiz.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.
```
