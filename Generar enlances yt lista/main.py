import yt_dlp
import pyperclip

def buscar_enlace(cancion):
    opciones = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,   # 🔥 clave: no entra al video
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            resultado = ydl.extract_info(f"ytsearch1:{cancion}", download=False)

            if 'entries' in resultado and resultado['entries']:
                video = resultado['entries'][0]
                return f"https://www.youtube.com/watch?v={video['id']}"
            else:
                return None

    except Exception:
        return None


if __name__ == "__main__":
    entrada = input("Ingrese canciones separadas por coma: ")
    canciones = [c.strip() for c in entrada.split(",")]

    enlaces = []

    for cancion in canciones:
        print(f"Buscando: {cancion}...")
        link = buscar_enlace(cancion)

        if link:
            print(f"Encontrado: {link}")
            enlaces.append(link)
        else:
            print("No se pudo obtener enlace.")

    if enlaces:
        texto_final = "\n".join(enlaces)
        pyperclip.copy(texto_final)
        print("\nTodos los enlaces fueron copiados al portapapeles.")