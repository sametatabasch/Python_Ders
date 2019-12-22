import os
f = os.popen('pwd')
now = f.read()
print("Çalıştığım konum=", now)