def song_decoder(song):
    song = song.replace("WUB"," ")
    song = " ".join(song.split())
    return song


song = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"

print(song_decoder(song))
