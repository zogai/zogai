import os
import urllib.request
import xbmcgui
import xbmcvfs

BUILD_URL = "https://github.com/zogai/zogai/releases/download/v1.0/zogai.zip"
BUILD_NAME = "zogai.zip"

download_path = xbmcvfs.translatePath("special://home/My_Builds/")
zip_path = os.path.join(download_path, BUILD_NAME)

if not xbmcvfs.exists(download_path):
    xbmcvfs.mkdirs(download_path)

dialog = xbmcgui.Dialog()

yes = dialog.yesno(
    "Zogai Wizard",
    "Download Zogai Kodi Build?"
)

if yes:
    dialog.notification("Zogai Wizard", "Downloading build...", xbmcgui.NOTIFICATION_INFO, 5000)

    try:
        urllib.request.urlretrieve(BUILD_URL, zip_path)
        dialog.ok(
            "Zogai Wizard",
            "Build downloaded successfully.\n\nOpen OpenWizard → Restore Local Build → My_Builds → zogai.zip"
        )
    except Exception as e:
        dialog.ok("Zogai Wizard Error", str(e))
