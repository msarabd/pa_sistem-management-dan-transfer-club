# menampilkan saldo club
# selalu bertmabah
#  duit barca, 120000000

import time
import threading
from data import data_barcelona


def saldo_barca():
    global saldo

    threading.Thread(target=saldo_barca, args=data["saldo"])


print("a")
