import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk,ImageDraw, ImageFont
from matplotlib import font_manager
import form1
import form2
import form3
import form4
def main():
    
      root = Tk()
      
      root.geometry("800x700")
      root.iconbitmap('icon.ico')
      root.title('CHECK YOUR HEALTH')
      root.configure(bg='#458B74')

      
      font = font_manager.FontProperties(family='georgia', weight='bold')
      file = font_manager.findfont(font)


      image = Image.new("RGB", (800, 100), "#448078")
      draw = ImageDraw.Draw(image)
      font = ImageFont.truetype(file, 39)
      draw.text((20, 20), "Human Multiple Disease Recognition", font=font, fill="#BBFFFF")

      # Save the image to a file and display it in Tkinter
      image.save("wordart1.png")
      photo = tk.PhotoImage(file="wordart1.png")
      label = Label(image=photo,bg="#448078")
      label.pack(fill=X,pady=30)

      image1 = PhotoImage(file="button_heart-disease-prediction.png")
      image2 = PhotoImage(file="button_malaria-disease-prediction.png")
      image3 = PhotoImage(file="button_pneumonia-disease-prediction.png")
      image4 = PhotoImage(file="button_diabetes-disease-prediction.png")
      img_exit = PhotoImage(file="button_exit.png")

      def exit():
            root.destroy()
            
      def exit1():
            root.destroy()
            form1.heart_pred()
            

      def exit2():
            root.destroy()
            form2.malaria_pred()

      def exit3():
            root.destroy()
            form3.pneumonia_pred()

      def exit4():
            root.destroy()
            form4.diabetes_pred()
            

      button1 = Button(root, image=image1, borderwidth=0,pady=20,bg="#458B74",command=exit1)
      button2 = Button(root, image=image2, borderwidth=0,pady=20,bg="#458B74",command=exit2)
      button3 = Button(root, image=image3, borderwidth=0,pady=20,bg="#458B74",command=exit3)
      button4 = Button(root, image=image4, borderwidth=0,pady=20,bg="#458B74",command=exit4)
      exit_button = Button(root, image=img_exit, borderwidth=0,pady=20,bg="#458B74",command=exit)

      button1.pack(fill=None,outline=None, expand=True)
      button2.pack(fill=None,outline=None, expand=True)
      button3.pack(fill=None,outline=None, expand=True)
      button4.pack(fill=None,outline=None, expand=True)
      exit_button.pack(fill=None,outline=None, expand=True)

      root.mainloop()

if __name__ == "__main__":
    main()
