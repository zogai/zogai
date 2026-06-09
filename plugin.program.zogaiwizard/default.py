import xbmcgui
import xbmc
import urllib.request
import os

BUILD_URL = "https://github.com/zogai/zogai/releases/download/v1.0/zogai.zip"
BUILD_NAME = "zogai.zip"

download_path = xbmc.translatePath("special://home/My_Builds/")
zip_path = os.path.join(download_path, BUILD_NAME)

if not os.path.exists(download_path):
    os.makedirs(download_path)

yes = xbmcgui.Dialog().yesno(
    "Zogai Wizard",
    "Download Zogai Kodi Build?"
)

if yes:
    xbmcgui.Dialog().notification("Zogai Wizard", "Downloading build...", xbmcgui.NOTIFICATION_INFO, 5000)
    urllib.request.urlretrieve(BUILD_URL, zip_path)
    xbmcgui.Dialog().ok(
        "Zogai Wizard",
        "Build downloaded successfully.\n\nNow open OpenWizard → Restore Local Build → My_Builds → zogai.zip"
    )
