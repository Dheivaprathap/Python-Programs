from tkinter import *
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image as PILImage
import os

# Main Window
root = Tk()
root.title("Resume Builder")
root.geometry("600x700")
root.configure(bg="#dff6ff")

photo_path = ""

# Functions

def upload_photo():
    global photo_path
    photo_path = filedialog.askopenfilename(
        title="Select Photo",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )

    if photo_path:
        photo_label.config(text=os.path.basename(photo_path), fg="green")


def generate_resume():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_text.get("1.0", END).strip()
    skills = skills_text.get("1.0", END).strip()
    education = education_text.get("1.0", END).strip()
    experience = experience_text.get("1.0", END).strip()

    if not name:
        messagebox.showerror("Error", "Please enter your name")
        return

    pdf_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Save Resume"
    )

    if not pdf_file:
        return

    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Add Photo
    if photo_path:
        try:
            img = PILImage.open(photo_path)
            img.thumbnail((120, 120))
            temp_img = "temp_photo.jpg"
            img.save(temp_img)

            elements.append(Image(temp_img, width=100, height=100))
            elements.append(Spacer(1, 12))
        except:
            messagebox.showwarning("Warning", "Photo could not be added")

    # Resume Content
    elements.append(Paragraph(f"<b><font size=18>{name}</font></b>", styles['Title']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"<b>Email:</b> {email}", styles['BodyText']))
    elements.append(Paragraph(f"<b>Phone:</b> {phone}", styles['BodyText']))
    elements.append(Paragraph(f"<b>Address:</b> {address}", styles['BodyText']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Skills</b>", styles['Heading2']))
    elements.append(Paragraph(skills, styles['BodyText']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Education</b>", styles['Heading2']))
    elements.append(Paragraph(education, styles['BodyText']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Experience</b>", styles['Heading2']))
    elements.append(Paragraph(experience, styles['BodyText']))

    doc.build(elements)

    messagebox.showinfo("Success", "Resume downloaded successfully!")


# Title
Label(root, text="Resume Builder", font=("Arial", 22, "bold"), bg="#dff6ff", fg="#005792").pack(pady=10)

# Name
Label(root, text="Full Name", bg="#dff6ff", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
name_entry = Entry(root, width=50, font=("Arial", 12))
name_entry.pack(padx=20, pady=5)

# Email
Label(root, text="Email", bg="#dff6ff", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
email_entry = Entry(root, width=50, font=("Arial", 12))
email_entry.pack(padx=20, pady=5)

# Phone
Label(root, text="Phone", bg="#dff6ff", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
phone_entry = Entry(root, width=50, font=("Arial", 12))
phone_entry.pack(padx=20, pady=5)

# Address
Label(root, text="Address", bg="#dff6ff", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
address_text = Text(root, width=50, height=3, font=("Arial", 11))
address_text.pack(padx=20, pady=5)

# Skills
Label(root, text="Skills", bg="#dff6ff", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
skills_text = Text(root, width=50, height=3, font=("Arial", 11))
skills_text.pack(padx=20, pady=5)

# Education
Label(root, text="Education", bg="#dff6ff", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
education_text = Text(root, width=50, height=3, font=("Arial", 11))
education_text.pack(padx=20, pady=5)

# Experience
Label(root, text="Experience", bg="#dff6ff", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
experience_text = Text(root, width=50, height=3, font=("Arial", 11))
experience_text.pack(padx=20, pady=5)

# Upload Photo Button
Button(root, text="Upload Photo", command=upload_photo, bg="#0077b6", fg="white", font=("Arial", 11, "bold")).pack(pady=10)

photo_label = Label(root, text="No photo selected", bg="#dff6ff", fg="red")
photo_label.pack()

# Generate Resume Button
Button(root, text="Download Resume PDF", command=generate_resume,
       bg="#00b894", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).pack(pady=20)

root.mainloop()

"""
Install Required Libraries:

pip install reportlab pillow

Run Program:

python resume_builder.py
"""
