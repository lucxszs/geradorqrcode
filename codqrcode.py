import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data('https://wa.me/5511978445654')
qr.make(fit=True)

imagem = qr.make_image(fill_color='orange', back_color='black')

imagem.save('qrcode-site.png')
