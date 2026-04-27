import yt_dlp
import os

def descargar_musica_desde_archivo(archivo, carpeta="Mi_musica"):
    try:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        with open(archivo, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
            
        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': f'{carpeta}/%(title)s.%(ext)s'
        }

        print("Descargando audios...")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download(urls)

        print("Descarga completada!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    descargar_musica_desde_archivo("urls.txt")