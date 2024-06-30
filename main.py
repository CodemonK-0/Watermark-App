from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import messagebox, font

# file path of the file
file_path = r"V:\Assignments\image Watermarking Desktop App\images\default.png"


# watermark font
fnt_size = ImageFont.truetype(
    r"V:\Assignments\image Watermarking Desktop App\Roboto_Mono\RobotoMono-VariableFont_wght.ttf",
    size=50,
)

rgba_values = [255, 255, 255, 255]
marked_img = None


file_types = [
    ("JPEG files", "*.jpg;*.jpeg"),
    ("PNG files", "*.png"),
    ("GIF files", "*.gif"),
    ("ALL FILES", "*.*"),
]

image_selected = False

posi_x = 0
posi_y = 0
angle = 0


def open_image():
    global image_selected, base_image, file_path
    try:
        file_path = fd.askopenfilename(filetypes=file_types)
        if file_path:
            image_selected = True
            status_label.configure(text="File selected")
            base_image = Image.open(file_path).convert("RGBA")
            base_image.thumbnail((400, 400))
            display_img = ImageTk.PhotoImage(base_image)
            image_label.configure(image=display_img)
            image_label.image = display_img
    except PermissionError:
        return None


def apply_watermark():
    global marked_img
    try:
        text = watermark.get()
        if text == "":
            raise ValueError("No watermark to apply.")
        if not image_selected:
            raise NameError("File is not selected.")
    except (ValueError, NameError) as e:
        messagebox.showerror(message=f"{e}")
    else:
        base_image = Image.open(file_path).convert("RGBA")
        text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(base_image)
        draw.text((0, 0), text=watermark.get(), font=fnt_size, fill=tuple(rgba_values))
        marked_img = Image.alpha_composite(base_image, text_image)
        marked_img.thumbnail((400, 400))
        display_img = ImageTk.PhotoImage(marked_img)
        image_label.configure(image=display_img)
        image_label.image = display_img


def move_up():
    global posi_y, marked_img, angle
    posi_y -= 50
    try:
        text = watermark.get()
        if text == "":
            raise ValueError("No watermark to apply.")
        if not image_selected:
            raise NameError("File is not selected.")
    except (ValueError, NameError) as e:
        messagebox.showerror(message=f"{e}")
    else:
        base_image = Image.open(file_path).convert("RGBA")
        text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)
        draw.text(
            (posi_x, posi_y),
            text=watermark.get(),
            font=fnt_size,
            fill=tuple(rgba_values),
        )
        text_image = text_image.rotate(angle)
        marked_img = Image.alpha_composite(base_image, text_image)
        marked_img.thumbnail((400, 400))
        display_img = ImageTk.PhotoImage(marked_img)
        image_label.configure(image=display_img)
        image_label.image = display_img


def move_down():
    global posi_y, marked_img, angle
    posi_y += 50
    try:
        text = watermark.get()
        if text == "":
            raise ValueError("No watermark to apply.")
        if not image_selected:
            raise NameError("File is not selected.")
    except (ValueError, NameError) as e:
        messagebox.showerror(message=f"{e}")
    else:
        base_image = Image.open(file_path).convert("RGBA")
        text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)
        draw.text(
            (posi_x, posi_y),
            text=watermark.get(),
            font=fnt_size,
            fill=tuple(rgba_values),
        )
        text_image = text_image.rotate(angle)
        marked_img = Image.alpha_composite(base_image, text_image)
        marked_img.thumbnail((400, 400))
        display_img = ImageTk.PhotoImage(marked_img)
        image_label.configure(image=display_img)
        image_label.image = display_img


def move_left():
    global posi_x, marked_img, angle
    posi_x -= 50
    try:
        text = watermark.get()
        if text == "":
            raise ValueError("No watermark to apply.")
        if not image_selected:
            raise NameError("File is not selected.")
    except (ValueError, NameError) as e:
        messagebox.showerror(message=f"{e}")
    else:
        base_image = Image.open(file_path).convert("RGBA")
        text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)
        draw.text(
            (posi_x, posi_y),
            text=watermark.get(),
            font=fnt_size,
            fill=tuple(rgba_values),
        )
        text_image = text_image.rotate(angle)
        marked_img = Image.alpha_composite(base_image, text_image)
        marked_img.thumbnail((400, 400))
        display_img = ImageTk.PhotoImage(marked_img)
        image_label.configure(image=display_img)
        image_label.image = display_img


def move_right():
    global posi_x, marked_img, angle
    posi_x += 50
    try:
        text = watermark.get()
        if text == "":
            raise ValueError("No watermark to apply.")
        if not image_selected:
            raise NameError("File is not selected.")
    except (ValueError, NameError) as e:
        messagebox.showerror(message=f"{e}")
    else:
        base_image = Image.open(file_path).convert("RGBA")
        text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)
        draw.text(
            (posi_x, posi_y),
            text=watermark.get(),
            font=fnt_size,
            fill=tuple(rgba_values),
        )
        text_image = text_image.rotate(angle)
        marked_img = Image.alpha_composite(base_image, text_image)
        marked_img.thumbnail((400, 400))
        display_img = ImageTk.PhotoImage(marked_img)
        image_label.configure(image=display_img)
        image_label.image = display_img


def increase_font(value):
    global fnt_size, marked_img, angle
    num = int(value)
    fnt_size = ImageFont.truetype(
        r"V:\Assignments\image Watermarking Desktop App\Roboto_Mono\RobotoMono-VariableFont_wght.ttf",
        size=num,
    )
    try:
        text = watermark.get()
        if text == "":
            raise ValueError("No watermark to apply.")
        if not image_selected:
            raise NameError("File is not selected.")
    except (ValueError, NameError) as e:
        messagebox.showerror(message=f"{e}")
    else:
        base_image = Image.open(file_path).convert("RGBA")
        text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)
        draw.text(
            (posi_x, posi_y),
            text=watermark.get(),
            font=fnt_size,
            fill=tuple(rgba_values),
        )
        text_image = text_image.rotate(angle)
        marked_img = Image.alpha_composite(base_image, text_image)
        marked_img.thumbnail((400, 400))
        display_img = ImageTk.PhotoImage(marked_img)
        image_label.configure(image=display_img)
        image_label.image = display_img


def font_opacity(value):
    global rgba_values, marked_img, angle
    alpha = int(value)
    rgba_values[3] = alpha
    if watermark.get():
        base_image = Image.open(file_path).convert("RGBA")
        text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        text_image = text_image.rotate(angle)
        draw = ImageDraw.Draw(text_image)
        draw.text(
            (posi_x, posi_y),
            text=watermark.get(),
            font=fnt_size,
            fill=tuple(rgba_values),
        )
        text_image = text_image.rotate(angle)
        marked_img = Image.alpha_composite(base_image, text_image)
        marked_img.thumbnail((400, 400))
        display_img = ImageTk.PhotoImage(marked_img)
        image_label.configure(image=display_img)
        image_label.image = display_img
    else:
        return None


def save():
    if file_path.endswith("default.png"):
        messagebox.showerror(message=f"No image to save.")
    else:
        save_path = fd.asksaveasfile(
            title="Save file as", defaultextension=".jpg", filetypes=file_types
        )
        width, height = Image.open(file_path).size
        if save_path:
            final_img = marked_img.resize((width, height)).convert("RGB")
            final_img.save(save_path)
            messagebox.showinfo(message=f"Image saved!")
        else:
            messagebox.showerror(message=f"Error, restart the application.")


def right_rotate():
    global marked_img, angle
    if watermark.get():
        base_image = Image.open(file_path).convert("RGBA")
        text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        angle += 10
        draw = ImageDraw.Draw(text_image)
        draw.text(
            (posi_x, posi_y),
            text=watermark.get(),
            font=fnt_size,
            fill=tuple(rgba_values),
        )
        text_image = text_image.rotate(angle)
        marked_img = Image.alpha_composite(base_image, text_image)
        marked_img.thumbnail((400, 400))
        display_img = ImageTk.PhotoImage(marked_img)
        image_label.configure(image=display_img)
        image_label.image = display_img


def left_rotate():
    global marked_img, angle
    if watermark.get():
        base_image = Image.open(file_path).convert("RGBA")
        text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        angle -= 10
        draw = ImageDraw.Draw(text_image)
        draw.text(
            (posi_x, posi_y),
            text=watermark.get(),
            font=fnt_size,
            fill=tuple(rgba_values),
        )
        text_image = text_image.rotate(angle)
        marked_img = Image.alpha_composite(base_image, text_image)
        marked_img.thumbnail((400, 400))
        display_img = ImageTk.PhotoImage(marked_img)
        image_label.configure(image=display_img)
        image_label.image = display_img


window = Tk()
window.title("MY APP")
window.configure(background="gray")
default_img = ImageTk.PhotoImage(
    Image.open(r"V:\Assignments\image Watermarking Desktop App\images\default.png")
)
# WELCOME TEXT
welcome_label = Label(
    window, text="Watermark App", bg="gray", fg="black", font=("Arial", 20, "bold")
)
# Image label
image_label = Label(window, image=default_img, bg="gray")

# ADD FILE
file_button = Button(
    window, text="Add file", bg="black", fg="white", command=open_image
)
apply_button = Button(
    window, text="Apply", width=5, bg="black", fg="white", command=apply_watermark
)
save_button = Button(window, text="Save", width=5, bg="black", fg="white", command=save)
# Text
text_label = Label(window, text="Type watermark text below!", bg="gray")
status_label = Label(window, text="Status", bg="gray")


# Entry
watermark = Entry(window)
# Position buttons
up_button = Button(window, width=3, text="▲", command=move_up)
down_button = Button(window, width=3, text="▼", command=move_down)
right_button = Button(window, width=3, text="▶", command=move_right)
left_button = Button(window, width=3, text="◀", command=move_left)
font_scale = Scale(
    window,
    from_=50,
    to=200,
    orient=HORIZONTAL,
    width=6,
    font=font.Font(family="Helvetica", size=7),
    command=increase_font,
)
opacity_scale = Scale(
    window,
    from_=256,
    to=10,
    orient=HORIZONTAL,
    width=6,
    font=font.Font(family="Helvetica", size=7),
    command=font_opacity,
)
opacity_scale.set(255)

# Rotate Watermark Buttons
rotat_r = Button(window, width=3, text="↺", command=right_rotate)
rotat_l = Button(window, width=3, text="↻", command=left_rotate)

# Close button
close_button = Button(
    window, text="Close", bg="black", fg="white", command=window.destroy
)

# Grid
window.columnconfigure((0, 1), weight=2)
window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=2)


# place widgets
welcome_label.grid(row=0, padx=10, sticky="nsew")
image_label.grid(row=0, column=1, padx=10, sticky="nsew", columnspan=1, rowspan=7)
file_button.grid(row=2, padx=10)
text_label.grid(row=3, padx=10)
watermark.grid(row=4)

# Apply and save buttons
apply_button.grid(row=5, pady=(0, 15), sticky="w")
save_button.grid(row=5, pady=(0, 15), sticky="e")
status_label.grid(row=5, column=0)


# Move buttons
up_button.grid(row=6, padx=10, pady=(0, 30), sticky="n")
down_button.grid(row=6, padx=10, pady=(30, 0), sticky="s")
right_button.grid(row=6, padx=(0, 30), sticky="e")
left_button.grid(row=6, padx=(30, 0), sticky="w")
rotat_r.grid(row=7, padx=(30, 0), sticky="w")
rotat_l.grid(row=7, padx=(0, 30), sticky="e")

# close
close_button.grid(row=7)


# Scales
font_scale.grid(row=7, column=1, padx=(50), sticky="e")
opacity_scale.grid(row=7, column=1, padx=(50), sticky="w")

window.mainloop()
