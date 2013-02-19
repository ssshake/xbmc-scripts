# Import the XBMC/XBMCGUI modules.
import xbmc, xbmcgui, time, urllib

#inherit from WindowDialog instead of Window so that it's shown on top of
#what's onscreen instead of replacing it entirely
class CamView(xbmcgui.WindowDialog):

    def __init__(self):
        #Define image location and size
        self.image = xbmcgui.ControlImage(870, 438, 380, 253, "")
        self.addControl(self.image)

viewer = CamView()
viewer.show()
start_time = time.time()
while(time.time() - start_time <= 14):
    #set url to ip cam image, password auth not supported 
    urllib.urlretrieve("http://asdf.com/camera/", '/tmp/bell.jpg')
    viewer.image.setImage("")
    viewer.image.setImage("/tmp/bell.jpg")
    #Define image transparency 
    viewer.image.setAnimations([('conditional', 'effect=fade start=90 end=90 time=0 condition=true',)])
    xbmc.sleep(500)
viewer.close()
del viewer
