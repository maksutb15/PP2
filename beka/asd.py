'''import datetime
bugin=datetime.datetime.now()
bugin2=bugin+datetime.timedelta(minutes=86400)
print(bugin2)'''
import datetime
bugin= datetime.datetime.now()
bugin2= bugin.replace(microsecond=1)
print(bugin)