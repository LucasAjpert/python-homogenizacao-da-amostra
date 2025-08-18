# --- main.py ---

import tkinter as tk
from view import MainView
# Importação atualizada para o novo caminho
from controllers.app_controller import AppController

if __name__ == "__main__":
    root = tk.Tk()
    controller = AppController()
    view = MainView(root, controller)
    controller.set_view(view)
    root.mainloop()