#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Beyanname Takip Çizelgesi - Python Kurulum Betiği
Windows, Linux ve macOS için otomatik kurulum
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

class BeyannameTakipKurulum:
    """Beyanname Takip Çizelgesi kurulum sınıfı"""
    
    def __init__(self):
        self.sistem = platform.system()
        self.python_versiyon = sys.version_info
        self.proje_dizini = Path(__file__).parent
        self.venv_dizini = self.proje_dizini / 'venv'
        
        print("=" * 50)
        print("Beyanname Takip Çizelgesi Kurulum Aracı")
        print("=" * 50)
        print(f"\nSistem: {self.sistem}")
        print(f"Python Versiyonu: {self.python_versiyon.major}.{self.python_versiyon.minor}.{self.python_versiyon.micro}")
        print(f"Proje Dizini: {self.proje_dizini}\n")
    
    def python_versiyonunu_kontrol_et(self):
        """Python versiyonunu kontrol et"""
        print("[1/6] Python versiyonu kontrol ediliyor...")
        
        if self.python_versiyon.major < 3 or (self.python_versiyon.major == 3 and self.python_versiyon.minor < 8):
            print(f"❌ Hata: Python 3.8+ gereklidir. Mevcut versiyon: {self.python_versiyon.major}.{self.python_versiyon.minor}")
            sys.exit(1)
        
        print(f"✓ Python {self.python_versiyon.major}.{self.python_versiyon.minor}.{self.python_versiyon.micro} uygun\n")
        return True
    
    def gerekli_dosyalari_kontrol_et(self):
        """Gerekli dosyaların varlığını kontrol et"""
        print("[2/6] Gerekli dosyalar kontrol ediliyor...")
        
        gerekli_dosyalar = [
            'requirements.txt',
            'setup.py',
            'app.py'
        ]
        
        eksik_dosyalar = []
        for dosya in gerekli_dosyalar:
            dosya_yolu = self.proje_dizini / dosya
            if not dosya_yolu.exists():
                eksik_dosyalar.append(dosya)
                print(f"❌ {dosya} bulunamadı")
            else:
                print(f"✓ {dosya} bulundu")
        
        if eksik_dosyalar:
            print(f"\n❌ Hata: {len(eksik_dosyalar)} dosya eksik!")
            sys.exit(1)
        
        print("✓ Tüm gerekli dosyalar bulundu\n")
        return True
    
    def virtual_environment_olustur(self):
        """Virtual Environment oluştur"""
        print("[3/6] Virtual Environment oluşturuluyor...")
        
        if self.venv_dizini.exists():
            print(f"⚠ Virtual Environment zaten var: {self.venv_dizini}")
        else:
            try:
                subprocess.check_call([sys.executable, '-m', 'venv', str(self.venv_dizini)])
                print(f"✓ Virtual Environment oluşturuldu: {self.venv_dizini}\n")
            except subprocess.CalledProcessError as e:
                print(f"❌ Hata: Virtual Environment oluşturulamadı: {e}")
                sys.exit(1)
        
        return True
    
    def paketleri_yukle(self):
        """Gerekli paketleri yükle"""
        print("[4/6] Gerekli paketler yükleniyor...")
        
        # Virtual Environment'ın Python executable'ı
        if self.sistem == "Windows":
            python_exe = str(self.venv_dizini / 'Scripts' / 'python.exe')
            pip_exe = str(self.venv_dizini / 'Scripts' / 'pip.exe')
        else:
            python_exe = str(self.venv_dizini / 'bin' / 'python')
            pip_exe = str(self.venv_dizini / 'bin' / 'pip')
        
        # pip'i güncelle
        print("  • pip güncelleniyor...")
        try:
            subprocess.check_call([pip_exe, 'install', '--upgrade', 'pip'])
            print("    ✓ pip güncellendi")
        except subprocess.CalledProcessError as e:
            print(f"    ⚠ pip güncellemede uyarı: {e}")
        
        # Paketleri yükle
        print("  • Paketler yükleniyor...")
        requirements_dosyasi = self.proje_dizini / 'requirements.txt'
        
        try:
            subprocess.check_call([pip_exe, 'install', '-r', str(requirements_dosyasi)])
            print("    ✓ Tüm paketler yüklendi\n")
        except subprocess.CalledProcessError as e:
            print(f"❌ Hata: Paketler yüklenemedi: {e}")
            sys.exit(1)
        
        return True
    
    def klasorleri_olustur(self):
        """Gerekli klasörleri oluştur"""
        print("[5/6] Uygulama klasörleri oluşturuluyor...")
        
        klasorler = [
            'veri/beyannameler',
            'veri/tahakkuklar',
            'cikti',
            'templates',
            'static'
        ]
        
        for klasor in klasorler:
            klasor_yolu = self.proje_dizini / klasor
            klasor_yolu.mkdir(parents=True, exist_ok=True)
            print(f"✓ {klasor} oluşturuldu")
        
        print()
        return True
    
    def orneks_dosyalari_olustur(self):
        """Örnek dosyaları oluştur"""
        print("[6/6] Örnek dosyalar oluşturuluyor...")
        
        # VKN listesi örneği
        vkn_dosyasi = self.proje_dizini / 'veri' / 'vkn_listesi_ornek.csv'
        if not vkn_dosyasi.exists():
            with open(vkn_dosyasi, 'w', encoding='utf-8') as f:
                f.write('VKN\n')
                f.write('1234567890\n')
                f.write('0987654321\n')
            print(f"✓ {vkn_dosyasi.name} oluşturuldu")
        
        # .env örneği
        env_dosyasi = self.proje_dizini / '.env'
        if not env_dosyasi.exists():
            with open(env_dosyasi, 'w', encoding='utf-8') as f:
                f.write('FLASK_ENV=development\n')
                f.write('FLASK_DEBUG=True\n')
                f.write('FLASK_APP=app.py\n')
                f.write('MAX_UPLOAD_SIZE=52428800\n')
            print(f"✓ {env_dosyasi.name} oluşturuldu")
        
        print()
        return True
    
    def kurulumlari_tamamla(self):
        """Kurulumu tamamla ve bilgi göster"""
        print("=" * 50)
        print("✓ Kurulum Başarıyla Tamamlandı!")
        print("=" * 50)
        print()
        
        if self.sistem == "Windows":
            aktiflestime_komutu = f"{self.venv_dizini}\\Scripts\\activate.bat"
        else:
            aktiflestime_komutu = f"source {self.venv_dizini}/bin/activate"
        
        print("SONRAKI ADIMLAR:")
        print("-" * 50)
        print("\n1. Virtual Environment'ı Aktifleştir:")
        print(f"   {aktiflestime_komutu}")
        print("\n2. Uygulamayı Başlat:")
        print("   python app.py")
        print("\n3. Tarayıcıda Aç:")
        print("   http://localhost:5000")
        print("\n" + "=" * 50)
        print("\nEK BİLGİLER:")
        print("-" * 50)
        print("• Veri klasörü: veri/")
        print("• Beyanname dosyaları: veri/beyannameler/")
        print("• Tahakkuk dosyaları: veri/tahakkuklar/")
        print("• VKN listesi: veri/vkn_listesi_ornek.csv")
        print("• Rapor ve çıktılar: cikti/")
        print("\n" + "=" * 50)
    
    def kurulumu_basla(self):
        """Kurulumun tüm adımlarını başlat"""
        try:
            self.python_versiyonunu_kontrol_et()
            self.gerekli_dosyalari_kontrol_et()
            self.virtual_environment_olustur()
            self.paketleri_yukle()
            self.klasorleri_olustur()
            self.orneks_dosyalari_olustur()
            self.kurulumlari_tamamla()
            
            return True
        
        except KeyboardInterrupt:
            print("\n\n❌ Kurulum iptal edildi!")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Beklenmeyen hata: {e}")
            sys.exit(1)


def main():
    """Ana fonksiyon"""
    kurulum = BeyannameTakipKurulum()
    
    # Kuruluma başla
    if kurulum.kurulumu_basla():
        print("\n💡 İpucu: Daha fazla bilgi için README.md dosyasını okuyun.")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
