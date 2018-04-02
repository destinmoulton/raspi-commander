from datetime import datetime
import remi.gui as gui

from Styles import LastRefreshedStyles


class LastRefreshed:
    def get_last_refreshed(self):

        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        text = "Last refreshed: {}".format(time)

        lb = gui.Label(text, style=LastRefreshedStyles["text"])

        cont = gui.Widget()
        cont.append(lb)
        return cont
