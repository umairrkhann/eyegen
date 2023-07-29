"""from gtts import gTTS
import os
  
def funct(stri = "" , attribute = ""):
# Language in which you want to convert
    from gtts import gTTS
    import os
  
    language = 'en'

    myobj = gTTS(text=stri, lang=language, slow=False)
   
    myobj.save(attribute+".mp3")
  
    os.system("mpg321 "+attribute+".mp3")

funct("You are in an open space","free_space")


"""

"""from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("mpg321 welcome.mp3")"""

from gtts import gTTS
import os

mytext = "Hi, this is an example of converting text to audio. This is a bot speaking here, not a real human!"
audio = gTTS(text=mytext, lang="en", slow=False)

audio.save("example.mp3")
os.system("start example.mp3")