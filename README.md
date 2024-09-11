```markdown
# Discord Voice Channel Switcher Bot

Bu proje, belirli bir kategorideki dolu ses kanalları arasında rastgele geçiş yapan bir Discord botudur. Bot, sesli kanallar arasında dolaşarak kullanıcıları trollemeye ve eğlenceli anlar yaşatmaya yarar.

## Kurulum

1. Bu projeyi klonlayın veya indirin:
   ```bash
   git clone https://github.com/kullanici-adiniz/discord-vc-switcher-bot.git
   cd discord-vc-switcher-bot
   ```

2. Gerekli Python kütüphanelerini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. `config.json` dosyasını düzenleyin ve kendi bot tokeninizi ve kategori ID'nizi ekleyin:
   ```json
   {
       "token": "BOT_TOKENINIZ",
       "category_id": "KATEGORI_IDNIZ"
   }
   ```

## Kullanım

1. Botu çalıştırmak için aşağıdaki komutu kullanın:
   ```bash
   python vc-troll.py
   ```

2. Bot başlatıldıktan sonra belirttiğiniz kategori içindeki dolu ses kanalları arasında rastgele geçiş yapacaktır.

## Gereksinimler

- Python 3.8+
- `discord.py`, `colorama`, `termcolor` kütüphaneleri

## Katkı

Katkıda bulunmak için lütfen bir pull request gönderin veya bir issue açın. Katkılarınızı bekliyoruz!

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atın.
```

### 3. Örnek `config.json` Dosyası

**config.json:**
```json
{
    "token": "BOT_TOKENINIZ",
    "category_id": "KATEGORI_IDNIZ"
}
```
