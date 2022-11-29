import tkinter as tk

infinite_cycle = True


def stop_programm():
    # Передает в controller infinite_cycle = False
    global infinite_cycle
    return infinite_cycle

def quit_window():
    # инициализация основного окна
    window = tk.Tk()
    window.title('Остановка программы')

    h = 80
    w = 228
    sw = window.winfo_screenwidth()
    x = int((sw - w) / 2)
    sh = window.winfo_screenheight()
    y = int((sh - h) / 2)
    window.geometry(f"{w}x{h}+{x}+{y}")
    window.resizable(False, False)

    def stop_programm():
        global infinite_cycle
        nonlocal window
        infinite_cycle = False
        window.destroy()

    btn_destroy = tk.Button(window, text='Остановить программу, остановить бота и закрыть окно', 
                            command=stop_programm, wraplength=220, 
                            font=('times new roman', 14, 'bold'))
    btn_destroy.pack()

    window.mainloop()