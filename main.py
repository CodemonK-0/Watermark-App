from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import messagebox, font

class Watermark_App:
    def __init__(self, window):
        self.window = window
        self.window.title("MY APP")
        self.window.configure(background="gray")

        self.file_path = ""  # file path of the file
        self.file_types = [
            ("JPEG files", "*.jpg;*.jpeg"),
            ("PNG files", "*.png"),
            ("GIF files", "*.gif"),
            ("ALL FILES", "*.*"),
        ]
        self.font_size = 50
        self.font = ImageFont.truetype("arial.ttf",self.font_size)
        self.selected_image = False

        self.posi_x = 0
        self.posi_y = 0
        self.angle = 0
        self.rgba_values = [255, 255, 255, 255]
        self.marked_img = None
        self.default_img = ImageTk.PhotoImage(Image.open(r"V:\Assignments\image Watermarking Desktop App\images\default.png"))

        # Widgets
        self.welcome_label = Label(window, text="Watermark App", bg="gray", fg="black", font=("Arial", 20, "bold"))
        self.image_label = Label(window, image=self.default_img, bg="gray")
        self.file_button = Button(window, text="Add file", bg="black", fg="white", command=self.open_image)
        self.apply_button = Button(window, text="Apply", width=5, bg="black", fg="white", command=self.apply_watermark)
        self.save_button = Button(window, text="Save", width=5, bg="black", fg="white", command=self.save)
        self.text_label = Label(window, text="Type watermark text below!", bg="gray")
        self.status_label = Label(window, text="Status", bg="gray")
        self.watermark_entry = Entry(window)
        self.up_button = Button(window, width=3, text="▲", command=self.move_up)
        self.down_button = Button(window, width=3, text="▼", command=self.move_down)
        self.right_button = Button(window, width=3, text="▶", command=self.move_right)
        self.left_button = Button(window, width=3, text="◀", command=self.move_left)
        self.font_scale = Scale(window, from_=50, to=200, orient=HORIZONTAL, width=6, font=font.Font(family="Helvetica", size=7), command=self.increase_font)
        self.opacity_scale = Scale(window, from_=255, to=10, orient=HORIZONTAL, width=6, font=font.Font(family="Helvetica", size=7), command=self.font_opacity) 
        self.opacity_scale.set(255)
        self.rotate_right_button = Button(window, width=3, text="↺", command=self.right_rotate)
        self.rotate_left_button = Button(window, width=3, text="↻", command=self.left_rotate)
        self.close_button = Button(window, text="Close", bg="black", fg="white", command=window.destroy)

        # Grid
        window.columnconfigure((0, 1), weight=2)
        window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=2)

        self.welcome_label.grid(row=0, padx=10, sticky="nsew")
        self.image_label.grid(row=0, column=1, padx=10, sticky="nsew", columnspan=1, rowspan=7)
        self.file_button.grid(row=2, padx=10)
        self.text_label.grid(row=3, padx=10)
        self.watermark_entry.grid(row=4)
        self.apply_button.grid(row=5, pady=(0, 15), sticky="w")
        self.save_button.grid(row=5, pady=(0, 15), sticky="e")
        self.status_label.grid(row=5, column=0)
        self.up_button.grid(row=6, padx=10, pady=(0, 30), sticky="n")
        self.down_button.grid(row=6, padx=10, pady=(30, 0), sticky="s")
        self.right_button.grid(row=6, padx=(0, 30), sticky="e")
        self.left_button.grid(row=6, padx=(30, 0), sticky="w")
        self.rotate_right_button.grid(row=7, padx=(30, 0), sticky="w")
        self.rotate_left_button.grid(row=7, padx=(0, 30), sticky="e")
        self.font_scale.grid(row=7, column=1, padx=(50), sticky="e")
        self.opacity_scale.grid(row=7, column=1, padx=(50), sticky="w")
        self.close_button.grid(row=7)

    # Command funcitons
    def open_image(self):
        try:
            self.file_path = fd.askopenfilename(filetypes=self.file_types)
            if self.file_path:
                self.selected_image = TRUE
                self.status_label.configure(text="File selected")
                base_image = Image.open(self.file_path).convert("RGBA")
                base_image.thumbnail((400, 400))
                display_img = ImageTk.PhotoImage(base_image)
                self.image_label.configure(image=display_img)
                self.image_label.image = display_img
        except PermissionError:
            return None
        

    def apply_watermark(self):
        try:
            text = self.watermark_entry.get()
            if text == "":
                raise ValueError("No watermark to apply.")
            if not self.selected_image:
                raise NameError("File is not selected.")
        except (ValueError, NameError) as e:
            messagebox.showerror(message=f"{e}")
        else:
            base_image = Image.open(self.file_path).convert("RGBA")
            text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(text_image)
            draw.text((self.posi_x,self.posi_y), text=self.watermark_entry.get(), font=self.font, fill=tuple(self.rgba_values))
            text_image = text_image.rotate(self.angle)
            marked_img = Image.alpha_composite(base_image, text_image)
            self.selected_image = marked_img
            marked_img.thumbnail((400, 400))
            display_img = ImageTk.PhotoImage(marked_img)
            self.image_label.configure(image=display_img)
            self.image_label.image = display_img

    def move_up(self):
        self.posi_y -= 50
        self.apply_watermark()

    def move_down(self):
        self.posi_y += 50
        self.apply_watermark()

    def move_right(self):
        self.posi_x += 50
        self.apply_watermark()

    def move_left(self):
        self.posi_x -= 50
        self.apply_watermark()

    def increase_font(self,value):
        self.font_size = int(value)
        self.apply_watermark()

    def font_opacity(self,value):
        self.rgba_values[3] = int(value)
        if self.watermark_entry.get():
            self.apply_watermark()

    def right_rotate(self):
        self.angle += 10
        self.apply_watermark()

    def left_rotate(self):
        self.angle -= 10
        self.apply_watermark()

    def save(self):
        if self.file_path.endswith("default.png"):
            messagebox.showerror(message=f"No image to save.")
        else:
            save_path = fd.asksaveasfile(
                title="Save file as", defaultextension=".jpg", filetypes=self.file_types
            )
            width, height = Image.open(self.file_path).size
            if save_path:
                final_img = self.selected_image.resize((width, height)).convert("RGB")
                final_img.save(save_path)
                messagebox.showinfo(message=f"Image saved!")
            else:
                messagebox.showerror(message=f"Error, restart the application.")

if __name__ == "__main__":
    window = Tk()
    app = Watermark_App(window)
    window.mainloop()