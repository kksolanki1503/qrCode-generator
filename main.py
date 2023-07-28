import qrcode as qr

img = qr.make("https://www.youtube.com/channel/UCnaWFYy6LRjPAgJRkQRwbOA")
img.save("vandana qrcode.png")