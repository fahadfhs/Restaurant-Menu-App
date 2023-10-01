import qrcode

image = qrcode.make("https://127.0.0.1:8000")  # takes us to our url
image.save("qr.png")  # generates a qr code which takes us to our url
