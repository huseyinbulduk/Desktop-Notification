from plyer import notification

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Masaüstü Bildirim Uygulaması",
        timeout=10  # Bildirimin görüntüleneceği süre (saniye cinsinden)
    )

if __name__ == "__main__":
    title = input("Bildirim başlığını girin: ")
    message = input("Bildirim mesajını girin: ")
    show_notification(title, message)
