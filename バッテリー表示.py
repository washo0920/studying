import psutil


btr = psutil.sensors_battery()
print(btr.percent)

m, s = divmod(btr.secsleft, 60)
h, m = divmod(m, 60)
print('{}:{}:{}'.format(h, m, s,))

