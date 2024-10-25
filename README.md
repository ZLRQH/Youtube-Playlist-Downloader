# Youtube Playlist Downloader 🎶

Ce script Python télécharge les fichiers audio d'une playlist YouTube publique et les convertit en MP3.

## Fonctionnalités

- Télécharge chaque vidéo d'une playlist en fichier MP3.
- Sauvegarde les fichiers dans un dossier spécifique.
- Affiche la progression et gère les erreurs pour chaque vidéo.

## Prérequis

- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) pour télécharger et convertir les vidéos YouTube en audio
- [FFmpeg](https://ffmpeg.org/download.html) pour l'extraction et la conversion des fichiers audio

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/youtube-playlist-downloader.git
   cd youtube-playlist-downloader```

## Utilisation

- Pour utiliser le script l'utilisateur doit changer la variable :
playlist_url = 'Ajoutez l'url de votre playlist Youtube vérifier qu'elle soit publique pour que tout fonctionne correctment'
download_folder ='Ajoutez votre chemin pour le repertoire de téléchargement'
