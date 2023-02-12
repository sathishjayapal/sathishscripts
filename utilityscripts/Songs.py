import random, os
music_dir = '/Volumes/MacProHD/iTunes/Music'
songs = os.listdir(music_dir)
#Prints all the directory for songs
print(songs)
song = random.randint(0,len(songs))
# Prints The Song Name
print(songs[song])
#Bummer for Macs.
# os.startfile(os.path.join(music_dir, songs[0]))
