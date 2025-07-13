import qrcode
from PIL import Image, ImageDraw

# Website URL to encode
url = "https:/YourURL.com"

# Create QR code with high error correction
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Generate QR code image
qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

# Load logo image
logo = Image.open('Logo.png')

# Resize logo
qr_width, qr_height = qr_img.size
logo_size = min(qr_width, qr_height) // 6
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Create circular white background
logo_bg_size = logo_size + 20
logo_bg = Image.new('RGB', (logo_bg_size, logo_bg_size), 'white')

# Create circular mask
mask = Image.new('L', (logo_bg_size, logo_bg_size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, logo_bg_size, logo_bg_size), fill=255)

# Paste logo onto circular background
logo_position = ((logo_bg_size - logo_size) // 2, (logo_bg_size - logo_size) // 2)
logo_bg.paste(logo, logo_position, mask=logo.convert('RGBA'))

# Paste logo with background at center of QR
logo_position_qr = ((qr_width - logo_bg_size) // 2, (qr_height - logo_bg_size) // 2)
qr_img.paste(logo_bg, logo_position_qr, mask)

# Save final image
qr_img.save('QR-Image.png')

print("QR code generated and saved as 'QR-Image.png'.")
