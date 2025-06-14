import qrcode
imagem = qrcode.make('https://www.example.com')
imagem.save("meuqrcode.jpg")