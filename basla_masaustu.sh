#!/bin/bash

# Beyanname Takip Çizelgesi - Masaüstü Uygulaması Başlat

echo ""
echo "======================================"
echo "Masaüstü Uygulaması Başlatılıyor..."
echo "======================================"
echo ""

# Virtual Environment oluştur veya kontrol et
if [ ! -d "venv" ]; then
    echo "Kurulum yapılıyor..."
    python3 setup_kurulum.py
fi

# Virtual Environment'ı aktifleştir
source venv/bin/activate

# Masaüstü uygulamasını başlat
python3 masaustu_app.py
