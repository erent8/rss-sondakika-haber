import tkinter as tk
import feedparser

# CNN Türk Ekonomi RSS feed URL'si
rss_url = 'https://www.cnnturk.com/feed/rss/ekonomi/news'

# Tkinter arayüzü oluştur
root = tk.Tk()
root.title("RSS Haberleri - CNN Türk Ekonomi")
root.geometry("500x400")

# Metin alanı ekle
text_area = tk.Text(root, wrap='word', height=20, width=60)
text_area.pack(pady=10)

# Güncelle butonu
def rss_veri_cek():
    # RSS verisini çek
    feed = feedparser.parse(rss_url)
    
    # Metin alanını temizle
    text_area.delete(1.0, tk.END)
    
    # RSS başlıkları, açıklamalar ve yayın tarihlerini yazdır
    for entry in feed.entries:
        baslik = f"Başlık: {entry.title}\n"
        aciklama = f"Açıklama: {entry.description}\n"
        yayin_tarihi = f"Yayınlanma Tarihi: {entry.published}\n"
        text_area.insert(tk.END, baslik)
        text_area.insert(tk.END, aciklama)
        text_area.insert(tk.END, yayin_tarihi)
        text_area.insert(tk.END, "-" * 50 + "\n")

# RSS verisini güncelleyen buton
btn_guncelle = tk.Button(root, text="RSS Güncelle", command=rss_veri_cek)
btn_guncelle.pack(pady=10)

# Açıklama etiketi
label = tk.Label(root, text="Başlık, açıklama ve tarih burada görünecek.")
label.pack(pady=5)

# Tkinter döngüsü
root.mainloop()
