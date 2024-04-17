import tkinter as tk
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import main
import get4

result=None
def diabetes_pred():
    root=ctk.CTk()
    title = root.title("Heart Disease Recognition")
    root.geometry("800x750")
    root.iconbitmap('icon.ico')

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    def back():
        root.destroy()
        main.main()

    image1 = Image.open("back-button.png")
    img_resized=image1.resize((50,50))
    image1 =ImageTk.PhotoImage(img_resized)

    button1=Button(root,image=image1,bg="#242424",border=0, command=back)
    button1.grid(row=0, column=0,pady=5,padx=10,sticky=NW)

    from PIL import ImageDraw, ImageFont
    image = Image.new("RGB", (850, 100), "#242424")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("georgia", 62)
    draw.text((20, 20), "Diabetes Disease Recognition", font=font, fill="#27b290")

    # Save the image to a file and display it in Tkinter
    image.save("wordart.png")
    photo = tk.PhotoImage(file="wordart.png")
    label = Label(root,image=photo,bg="#242424")
    label.grid(row=1, column=0,columnspan=5,padx=10,sticky=N+S+E+W)
    label.place(relx=0.5, rely=0.04, anchor=N)

    # Create a frame
    frame = ctk.CTkFrame(master=root)
    frame.grid(row=2, column=0,pady=10,padx=80,sticky=N+S+E+W)
    frame.place(relx=0.5, rely=0.2, anchor='n')
    # Set the label inside the frame
    label1 = ctk.CTkLabel(master=frame,text='PLEASE  ENTER  FOLLOWING  DETAILS',
                          font=("georgia",22),text_color="#2fa572")
    label1.pack(pady=12,padx=10,fill=X,expand=True)
      
    # Create the input from user
    name= ctk.CTkEntry(master=frame,placeholder_text="Name",text_color="turquoise",font=("georgia",18))
    name.pack(pady=10,padx=10,fill=X,expand=True)

    age= ctk.CTkEntry(master=frame,placeholder_text="Age",text_color="turquoise",font=("georgia",18))
    age.pack(pady=10,padx=10,fill=X,expand=True)

    glucose= ctk.CTkEntry(master=frame,text_color="turquoise",placeholder_text="Glucose Level"
                                              ,font=("georgia",18))
    glucose.pack(pady=10,padx=10,fill=X,expand=True)

    bp= ctk.CTkEntry(master=frame,placeholder_text="BloodPressure",text_color="turquoise",font=("georgia",18))
    bp.pack(pady=10,padx=10,fill=X,expand=True)

    skinTh= ctk.CTkEntry(master=frame,placeholder_text="Skin Thickness",text_color="turquoise"
                                             ,font=("georgia",18))
    skinTh.pack(pady=10,padx=10,fill=X,expand=True)

    insulin= ctk.CTkEntry(master=frame,placeholder_text="Insulin Level",text_color="turquoise"
                                             ,font=("georgia",18))
    insulin.pack(pady=10,padx=10,fill=X,expand=True)

    bmi = ctk.CTkEntry(master=frame,placeholder_text='BMI',
                          font=("georgia",16),text_color="#2fa572")
    bmi.pack(pady=10,padx=10,fill=X,expand=True)


    def pred():
        global result
        if result is not None:
            result.destroy()

        name_val = name.get()
        age_val = age.get()
        glucose_val = glucose.get()
        bp_val = bp.get()
        skinTh_val = skinTh.get()
        insulin_val = insulin.get()
        bmi_val=bmi.get()
       
        
        prediction=get4.predict(age_val,glucose_val,bp_val,skinTh_val,insulin_val,bmi_val)
        print(prediction)
       
        
        
        if prediction==[0]:
            result = ctk.CTkLabel(master=frame,text='Congrats '+name_val+' You Don\'t Have  D i a b e t e s',
                          font=("georgia",30),text_color="green")
            result.pack(pady=12,padx=10,fill=X,expand=True)

        else:
            result = ctk.CTkLabel(master=frame,text='Sorry '+name_val+' ! You Have  D i a b e t e s',
                          font=("georgia",30),text_color="red")
            result.pack(pady=12,padx=10,fill=X,expand=True)
      
    # Create a button to login
    button = ctk.CTkButton(master=frame,
                           text='Predict',font=("georgia",18),command=pred)
    button.pack(pady=12,padx=10,fill=X,expand=True)

    def exit():
          root.destroy()
          
    button = ctk.CTkButton(master=frame,
                           text='Exit',font=("georgia",18),command=exit)
    button.pack(pady=12,padx=10,fill=X,expand=True)


    root.mainloop()

