import tkinter as tk
import customtkinter as ctk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import main
import get2

result=None
label1=None
def malaria_pred():
    
    root = Tk()
    root.geometry("800x750")
    root.iconbitmap('icon.ico')
    root.title('MALARIA DISEASE PREDICTION')
    root.configure(bg='#458B74')

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    def back():
        root.destroy()
        main.main()

    image1 = Image.open("back-button.png")
    img_resized=image1.resize((50,50))
    image1_tk =ImageTk.PhotoImage(img_resized) # Convert to Tkinter-compatible image
    button1=Button(root,image=image1_tk,border=0,bg='#458B74', command=back) # Use the Tkinter-compatible image
    button1.grid(row=0, column=0,pady=10,padx=10,sticky=NW)

    from PIL import ImageDraw, ImageFont
    from matplotlib import font_manager
    font = font_manager.FontProperties(family='georgia', weight='bold')
    file = font_manager.findfont(font)


    image = Image.new("RGB", (1550, 100), "#448078")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(file, 40)
    draw.text((470, 20), "Malaria Disease Recognition", font=font, fill="#BBFFFF")

    # Save the image to a file and display it in Tkinter
    image.save("wordart2.png")
    photo = tk.PhotoImage(file="wordart2.png")
    label = Label(image=photo,bg="#448078")
    label.grid(row=1, column=0, pady=12,sticky=N+S+E+W)
    label.place(relx=0.5, rely=0.1, anchor=N)

    
    def open_image():
        global file_path
        file_path = filedialog.askopenfilename()
        if file_path:
            global label1
            if label1 is not None:
                label1.destroy()
            cell_image = Image.open(file_path)
            img_resized=cell_image.resize((200,200)) # new width & height
            photo1 = ImageTk.PhotoImage(img_resized)
            label1 = Label(image=photo1,bg='#458B74')
            label1.image = photo1
            label1.grid(row=2, column=0,pady=12,padx=10,sticky=N+S+E+W)

    
    def pred():
        global result
        prediction =5
        if result is not None:
            result.destroy()
        

        prediction = get2.predict(file_path)
        print(prediction)
        

        if prediction==0:
            result = ctk.CTkLabel(root,text='W o w !   U n i n f e c t e d',
                          font=("georgia",22),text_color="#2714fa")
            result.grid(row=6, column=0,pady=12,padx=10,sticky=N+S+E+W)

        elif prediction==1:
            result = ctk.CTkLabel(root,text='M a l a r i a   I n f e c t e d',
                          font=("georgia",22),text_color="Red")
            result.grid(row=6, column=0,pady=12,padx=10,sticky=N+S+E+W)

        
    def exit():
          root.destroy()
           
    image1 = PhotoImage(file="button_upload-cell-image.png")
    pred_btn = ImageTk.PhotoImage(file='button_predict.png')
    img_exit = PhotoImage(file="button_exit.png")

    button = Button(root, image=image1, borderwidth=0, pady=20, bg="#458B74", command=open_image)
    button.grid(row=3, column=0,pady=12,padx=10,sticky=N+S+E+W)

    button2 = Button(root, image=pred_btn, borderwidth=0, pady=20, bg="#458B74",command=pred)
    button2.grid(row=4, column=0,pady=12,padx=10,sticky=N+S+E+W)

    exit_button = Button(root, image=img_exit, borderwidth=0,pady=20,bg="#458B74",command=exit)
    exit_button.grid(row=5, column=0,pady=12,padx=10,sticky=N+S+E+W)
    root.mainloop()
