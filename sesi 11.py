import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="BERHASIL DI TANAM")
    label2.pack()


label = tkinter.Label(main_window, text="lanjutkan menanam ?")
tombol = tkinter.Button(main_window, text="MENANAM !", command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()
