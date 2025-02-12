import qrcode

# Get user input
data = input("Enter text or URL: ")

# Generate QR code
qr = qrcode.make(data)

# Save the QR code as an image file
qr.save("qrcode.png")

# Confirmation message
print("QR Code generated and saved as 'qrcode.png'!")
