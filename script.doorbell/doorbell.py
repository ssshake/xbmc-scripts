# Import the XBMC/XBMCGUI modules.
import xbmc, xbmcgui, time, urllib, xbmcvfs, xbmcaddon, os
__addon__   = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')

url='https://asdf.com/camera/'

path = xbmc.translatePath('special://profile/addon_data/%s' % __addonid__)
if not xbmcvfs.exists(path):
    xbmcvfs.mkdir(path)
imagefile = os.path.join(path, 'bell.jpg')


class CamView(xbmcgui.WindowDialog):

    def __init__(self):
        #set the initial image before the window is shown
        urllib.urlretrieve(url, imagefile)
        self.image = xbmcgui.ControlImage(870, 383, 380, 253, "")
        self.addControl(self.image)

viewer = CamView()
viewer.show()
start_time = time.time()
firstimage = True
while(time.time() - start_time <= 14):
    urllib.urlretrieve(url, imagefile)
    viewer.image.setImage("")
    viewer.image.setImage(imagefile)
    curr_time = round(time.time() - start_time, 0)
    if firstimage:
        nowtime=time.strftime("%I:%M %p")
        xoptions="Notification(\"Doorbell\",%s, 13800, special://masterprofile/media/bell1.png)" % (nowtime)
        xbmc.executebuiltin(xoptions)
        viewer.image.setAnimations([('conditional', 'effect=fade start=0 end=90 time=250 delay=125 condition=true',), ('conditional', 'effect=slide start=0,400 end=0,0 time=250 condition=true',)])
        firstimage = False
    elif curr_time == 14:
        viewer.image.setAnimations([('conditional', 'effect=fade start=90 end=90 time=0 condition=true',), ('conditional', 'effect=slide start=0,0 end=0,400 time=250 condition=true',)])
        print "catch"
    else:
        viewer.image.setAnimations([('conditional', 'effect=fade start=90 end=90 time=0 condition=true',)])
        print curr_time
    xbmc.sleep(500)


viewer.close()
del viewer
