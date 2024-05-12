# Setting Student model to use for setting up the database
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File


class Student(models.Model):
    GENDER_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE", "Female")
    )
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    student_id = models.CharField(max_length=20, unique=True)
    student_class = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=9,
                              choices=GENDER_CHOICES,
                              default="FEMALE")
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def save(self, *args, **kwargs):
        if not self.qr_code:
            try:
                # Generate QR code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(self.student_id)
                qr.make(fit=True)

                # Create QR code image
                img = qr.make_image(fill_color="black", back_color="white")

                # Save QR code to field
                buffer = BytesIO()
                img.save(buffer)
                filename = f'{self.student_id}.png'
                filebuffer = File(buffer, name=filename)
                self.qr_code.save(filename, filebuffer)

                # Call parent's save method
                super().save(*args, **kwargs)

            except Exception as e:
                # Handle any exceptions (e.g., validation error, file saving error)
                print(f"Error saving QR code for student {self.student_id}: {e}")
