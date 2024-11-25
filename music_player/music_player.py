from pygame import mixer
import sys

# Initialize mixer
mixer.init()

# Songs dictionary
songs = {
    '1': 'Shiv_tandv.mp3',
    '2': 'Barsaat_Ho.mp3',
    '3': 'Barsaat_Ki.mp3',
    '4': 'Bewafa_TeraC.mp3',
    '5': 'O_Aasman_Wale.mp3',
    '6': 'Dil-Mera-Chahe.mp3',
    '7': 'Teri_Galliyon.mp3'
}

# Display song options
print("Select a song to play:")
for key, song in songs.items():
    print(f"{key} for {song.split('.')[0]}")
print("Enter 'x' to exit.")

# Main loop
while True:
    user_input = input('Command: ')
    if user_input == 'x':
        print("Exiting the program. Goodbye!")
        mixer.music.stop()
        sys.exit()
    elif user_input in songs:
        mixer.music.stop()  # Stop any currently playing music
        mixer.music.load(songs[user_input])
        mixer.music.play()
        print(f"Playing: {songs[user_input].split('.')[0]}")
    else:
        print("Invalid input. Please try again.")
