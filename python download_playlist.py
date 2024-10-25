import os
import yt_dlp

# URL de la playlist YouTube
playlist_url = ''

# Répertoire de téléchargement
download_folder = r''

# Créer un dossier pour stocker les vidéos téléchargées
try:
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        print(f"Dossier de téléchargement créé avec succès : {download_folder}")
    else:
        print(f"Dossier de téléchargement existe déjà : {download_folder}")
except Exception as e:
    print(f"Erreur lors de la création du dossier de téléchargement : {e}")

# Options pour yt-dlp
ydl_opts = {
    'format': 'bestaudio/best',  # Télécharger le meilleur format audio disponible
    'extractaudio': True,  # Extraire l'audio
    'audioformat': 'mp3',  # Format audio désiré
    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Modèle de nom de fichier
    'noplaylist': False,  # Télécharger toute la playlist
    'quiet': False,  # Afficher les messages de téléchargement
    'progress_hooks': [lambda d: print(f"Progress: {d['filename']} ({d.get('downloaded_bytes', 0)} bytes downloaded)")],  # Afficher la progression
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Utiliser FFmpeg pour extraire l'audio
        'preferredcodec': 'mp3',  # Convertir en MP3
        'preferredquality': '192',  # Qualité audio
    }],
    'ignoreerrors': True,  # Ignorer les erreurs pour les vidéos non disponibles
}

# Télécharger la playlist
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
    print('Tous les téléchargements sont terminés.')
except Exception as e:
    print(f"Erreur lors du téléchargement de la playlist : {e}")
