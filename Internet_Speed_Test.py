import speedtest
s = speedtest.Speedtest(secure=True)
bytes = 1000000
downs = round(s.download()/bytes,2)
ups = round(s.upload()/bytes,2)

print(f'Donwload Speed: {downs} Mbps')
print(f'Upload Speed: {ups} Mbps')