import playsound
import random
from os import remove, system
from gtts import gTTS
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
BhayanakT, BhayanakI = "Bhayanak Atma feat. Gagan Mudgal-", "z6H7QX0fQrE"
SceneT, SceneI = "Scene Kya Hai - Nucleya x DIVINE-", "4zYOO4F1ecw"
JindT, JindI = "Jind Mahi (feat. Avneet Khurmi)-", "JB6ZEpkWFJo"
AajaT, AajaI = "Nucleya - BASS Rani - Aaja feat Avneet Khurmi & Guri Gangsta-", "slNebO7Yips"
LiggiT, LiggiI = "Ritviz - Liggi [Official Music Video]-", "6BYIKEH0RCQ"
MumbaiT, MumbaiI = "Mumbai Dance (Feat. Julius Sylvest)-", "xqqnmZTyAnA"
KhatamT, KhatamI = "EMIWAY - KHATAM HUE WAANDE (Prod.YOKI) (OFFICIAL MUSIC VIDEO)-", "nu2MOmczxwQ"
BombayT, BombayI = "Chal Bombay-", "_jpuXTbAQh8"
MagentaT, MagentaI = "DJ Snake - Magenta Riddim-", "op4B9sNGi0k"
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NCS$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
MortalsT, MortalsI = "Warriyo - Mortals (feat. Laura Brehm) [NCS Release]-", "yJg-Y5byMMw"
LandscapeT, LandscapeI = "Jarico - Landscape [NCS BEST OF]-", "Srqs4CitU2U"
AnimalsT, AnimalsI = "Martin Garrix - Animals [NCS Fanmade _ Video Old]-", "4Y4CQrisma4"
YalgaarT, YalgaarI = "YALGAAR - CARRYMINATI X Wily Frenzy-", "zzwRbKI2pn4"
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def Speak(ToSpeak):
    tts = gTTS(text=ToSpeak, lang='hi', slow=False)
    Filename = random.randint(1,100000)
    audio_file = 'audio-' +str(Filename) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    remove(audio_file)
def YouTubeMusic(Title, ID):
    system("youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v="+ID)
    Speak("Now Playing, "+Title)
    playsound.playsound(Title+ID+".mp3")
    system("Exit")

YouTubeMusic(LiggiT,LiggiI)
