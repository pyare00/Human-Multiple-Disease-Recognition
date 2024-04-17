import tkinter as tk
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import main
import get1

result=None
def heart_pred():
    
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
    button1.grid(row=0, column=0,pady=12,padx=10,sticky=NW)

    from PIL import ImageDraw, ImageFont
    image = Image.new("RGB", (825, 100), "#242424")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("georgia", 66)
    draw.text((20, 20), "Heart Disease Recognition", font=font, fill="#27b290")

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

    sex= ctk.CTkEntry(master=frame,text_color="turquoise",placeholder_text="Gender : (Male , Female)"
                                              ,font=("georgia",18))
    sex.pack(pady=10,padx=10,fill=X,expand=True)

    chol= ctk.CTkEntry(master=frame,placeholder_text="Cholestrol (mg/dl)",text_color="turquoise",font=("georgia",18))
    chol.pack(pady=10,padx=10,fill=X,expand=True)

    ca= ctk.CTkEntry(master=frame,placeholder_text="Enter number of Major Vessels (0–3)",text_color="turquoise"
                                             ,font=("georgia",18))
    ca.pack(pady=10,padx=10,fill=X,expand=True)

    thalach= ctk.CTkEntry(master=frame,placeholder_text="Maximum Heart Rate Achieved",text_color="turquoise"
                                             ,font=("georgia",18))
    thalach.pack(pady=10,padx=10,fill=X,expand=True)

    cplabel = ctk.CTkLabel(master=frame,text='Choose Chest Pain Type',
                          font=("georgia",16),text_color="#2fa572")
    cplabel.pack(padx=10,anchor='w')
    cp= ctk.CTkOptionMenu(master=frame,values=["0: Asymptomatic","1: Atypical angina",
                          "2: Non-anginal","3: Typical angina"],anchor="center",font=("georgia",18))
    cp.pack(padx=10, pady=10, fill=X,expand=True)
    cp.set("0: Asymptomatic")

    

    def pred():
        global result
        if result is not None:
            result.destroy()

        name_val = name.get()
        age_val = age.get()
        sex_val = sex.get()
        chol_val = chol.get()
        ca_val = ca.get()
        cp_val = cp.get()[0]
        thal_val=thalach.get()
       
        
        prediction=get1.predict(age_val,sex_val,cp_val,chol_val,thal_val,ca_val)
        print(prediction)
       
        
        
        if prediction==[0]:
            result = ctk.CTkLabel(master=frame,text='Congrats '+name_val+'!! You Don\'t Have Heart Disease',
                          font=("georgia",32),text_color="lightpink")
            result.pack(pady=12,padx=10,fill=X,expand=True)

        else:
            result = ctk.CTkLabel(master=frame,text='Sorry '+name_val+' !! You Have Heart Disease',
                          font=("georgia",32),text_color="red")
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
