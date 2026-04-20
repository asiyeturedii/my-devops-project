# 1. Hafif bir Python temel imajı alıyoruz
FROM python:3.9-slim

# 2. Konteyner içinde çalışacağımız klasörü belirliyoruz
WORKDIR /app

# 3. Kütüphane listesini kopyalayıp yüklüyoruz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Bilgisayarımızdaki tüm kodları konteynerin içine kopyalıyoruz
COPY . .

# 5. Uygulamanın 5000 portundan çalışacağını söylüyoruz
EXPOSE 5000

# 6. Uygulamayı çalıştırıyoruz
CMD ["python", "app.py"]