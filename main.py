import qrcode

qrContent = input("Ingrese el contenido del qr: ")

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 50,
    border = 2
)

qr.add_data(qrContent)
qr.make(fit=True)

img = qr.make_image(fill_color = "black", black_color = "white")
img.save("qr.png")

print("Qr guardado")