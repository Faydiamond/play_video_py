

# importing pyglet module
import pyglet
 
# width of window
width = 0
   
# height of window
height = 0
   

video = int(input(' digite un numero de 1 al 3, cada numero represnta el ejercio de las pruebas:  '))
#remplace la ruta del video con un archivo en formato mp4 que tenga en su maquina
if (video == 1):
    vidPath = r"C:\Users\FabiDiamanti\Documents\Fabian\entrevista_python\Hotel\ecomar.mp4"
    height = 720
    width = 1270
if (video == 2):
    vidPath = r"C:\Users\FabiDiamanti\Documents\Fabian\entrevista_python\Hotel\acme.mp4"
    height = 460
    width = 700
if (video == 3):
    vidPath = r"C:\Users\FabiDiamanti\Documents\Fabian\entrevista_python\Hotel\inversor.mp4"
    height = 460
    width = 810

 


# caption i.e title of the window
title = "ecomar"
   
# creating a window
window = pyglet.window.Window(width, height, title)

# video path

 
# creating a media player object
player = pyglet.media.Player()
 
# creating a source object
source = pyglet.media.StreamingSource()
 
# load the media from the source
MediaLoad = pyglet.media.load(vidPath)
 
# add this media in the queue
player.queue(MediaLoad)
 
# play the video
player.play()
 
# on draw event
@window.event
def on_draw():
     
    # clea the window
    window.clear()
     
    # if player source exist
    # and video format exist
    try:
        
        
        if player.source and player.source.video_format:
             
            # get the texture of video and
            # make surface to display on the screen
            player.get_texture().blit(0, 0)
            

            
    except:
        print('error')
    
         
# key press event    
@window.event
def on_key_press(symbol, modifier):
   
    # key "p" get press
    if symbol == pyglet.window.key.P:
         
        # printing the message
        print("Key : P is pressed")
         
        # pause the video
        player.pause()
         
        # printing message
        print("Video is paused")
         
         
    # key "r" get press
    if symbol == pyglet.window.key.R:
         
        # printing the message
        print("Key : R is pressed")
         
        # resume the video
        player.play()
         
        # printing message
        print("Video is resumed")
        
        # key "r" get press
    if symbol == pyglet.window.key.E:
         
        # printing the message
        print("Key : E is pressed")
         
        # resume the video
        window.close()
         
        # printing message
        print("crre ventana")
 
 
# run the pyglet application
pyglet.app.run()


