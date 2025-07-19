# 🗃️ Gelişmiş SQL INSERT Üretici

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green?style=for-the-badge&logo=pandas)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

Excel ve CSV dosyalarınızı, gelişmiş seçeneklerle, farklı veritabanı lehçelerine uygun, hatasız SQL `INSERT` sorgularına dönüştüren interaktif bir web uygulaması.

---

### ✨ Uygulama Arayüzü

Bu alana uygulamanızın ekran görüntüsünü veya kısa bir GIF'ini ekleyerek projenizi çok daha çekici hale getirebilirsiniz!

![SQL Insert Üretici Arayüzü](https://i.imgur.com/E5J0nua.png)
*(**İpucu:** Bu görseli, kendi uygulamanızın ekran görüntüsüyle değiştirin. Örneğin, Windows'ta `Ekran Alıntısı Aracı`'nı kullanabilir, resmi [imgur.com](https://imgur.com/upload) gibi bir siteye yükleyip linkini buraya yapıştırabilirsiniz.)*

---

## 🚀 Temel Özellikler

* **Anında Veri Önizleme:** Dosyayı yüklediğiniz anda içeriğin ilk birkaç satırını görerek doğru veriyi işlediğinizden emin olun.
* **Gelişmiş SQL Seçenekleri:**
    * **Hedef Veritabanı:** MS SQL Server, PostgreSQL ve MySQL lehçeleri arasında seçim yapın.
    * **Tablo Adı:** İsteğe bağlı olarak tablo adını kendiniz belirleyin veya dosya adının kullanılmasını sağlayın.
    * **INSERT Tipi:** Her satır için ayrı `INSERT` sorguları veya tüm veriler için tek, birleştirilmiş (multi-row) bir `INSERT` sorgusu oluşturun.
    * **Boş Hücre Yönetimi:** Dosyadaki boş hücrelerin SQL'de `NULL` olarak mı yoksa boş metin (`''`) olarak mı temsil edileceğini seçin.
* **Çoklu Sayfa Desteği:** Birden fazla sayfaya sahip Excel dosyalarında, hangi sayfayı işlemek istediğinizi seçmenize olanak tanır.
* **Kullanıcı Dostu Arayüz:** Tüm kontroller, ayarlar ve sonuçlar tek bir ekranda, anlaşılır bir şekilde sunulur.
* **Yardım Menüsü:** Entegre `❓` yardım menüsü ile uygulamanın kullanımı hakkında hızlıca bilgi alın.
* **SQL İndirme:** Oluşturulan SQL kodunu tek tıkla `.sql` dosyası olarak indirin.

---

## 🛠️ Kullanılan Teknolojiler

* **Python:** Uygulamanın temelini oluşturan programlama dili.
* **Streamlit:** İnteraktif web arayüzünü oluşturmak için kullanılan ana kütüphane.
* **Pandas:** Excel ve CSV dosyalarını okuma, işleme ve analiz etme için kullanılan güçlü veri kütüphanesi.

---

## ⚙️ Kurulum ve Yerel Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git](https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git)
    cd PROJE_ADINIZ
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    *(Bir sanal ortam (virtual environment) oluşturmanız tavsiye edilir.)*
    ```bash
    pip install -r requirements.txt
    ```
    *(Not: Proje klasörünüzde `streamlit`, `pandas`, `openpyxl` içeren bir `requirements.txt` dosyası oluşturun.)*

3.  **Uygulamayı Başlatın:**
    ```bash
    streamlit run app.py
    ```
    Bu komut, uygulamayı yerel bir sunucuda başlatacak ve otomatik olarak tarayıcınızda açacaktır.

---

## ☁️ İnternette Yayınlama (Streamlit Community Cloud)

Bu uygulamayı Python bilmeyen arkadaşlarınızla paylaşmanın en kolay yolu, onu ücretsiz olarak internette yayınlamaktır.

1.  Projenizi bir GitHub deposuna yükleyin.
2.  `share.streamlit.io` adresine gidin ve GitHub hesabınızla giriş yapın.
3.  **"New app"** butonuna tıklayarak deponuzu seçin ve **"Deploy!"** butonuna basın.
4.  Birkaç dakika içinde `proje-isminiz.streamlit.app` şeklinde bir linke sahip olacaksınız!

---

## 🤝 Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir "issue" açın veya bir "pull request" gönderin. Tüm katkılar memnuniyetle karşılanır!

---

## 📄 Lisans

Bu proje, MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.