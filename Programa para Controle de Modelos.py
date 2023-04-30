import tkinter
import tkinter.messagebox
import customtkinter
import time

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



        
            
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Contador de Modelos")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Rodizio dos Modelos da Fábrica", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event_CC, text="CC")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event_RC, text="RC")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event_SUV, text="SUV")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event_Liberar_Peça, text="Liberar Peça")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
       
        
       

    
        self.label1 = customtkinter.CTkLabel(master=self,
                               text="", 
                               text_color="black",
                               width=35,
                               height=10,
                               font= ("Montserrat", 35),
                               fg_color=("black", "white"),
                               corner_radius=8,anchor=tkinter.CENTER)
        self.label1.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
       

       
        self.label2 = customtkinter.CTkLabel(master=self,
                               text="",                
                               text_color="black",
                               width=35,
                               height=10,
                               font= ("Montserrat", 35),
                               fg_color=("black", "yellow"),
                               corner_radius=8,anchor=tkinter.CENTER)
        self.label2.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        

        self.label3 = customtkinter.CTkLabel(master=self,
                               text="",            
                               text_color="black",
                               width=35,
                               height=10,
                               font= ("Montserrat", 35),
                               fg_color=("black", "blue"),
                               corner_radius=8,anchor=tkinter.CENTER)
        self.label3.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.liberar_peça = False
        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event_RC(self):
        dialog = customtkinter.CTkInputDialog(text="Digite um valor:", title="Modelo da RC")
        self.num = dialog.get_input()
        self.label1.configure(text="")
        self.label3.configure(text="")
        self.veri_SUV = False
        self.veri_RC = True
        self.contagem = 1
    

    def sidebar_button_event_SUV(self):
        dialog2 = customtkinter.CTkInputDialog(text="Digite um valor: ", title="Modelo da SUV")
        self.num = dialog2.get_input()
        self.label2.configure(text="")        
        self.label1.configure(text="")
        self.veri_SUV = True
        self.veri_RC = False
        self.contagem = 1  

    def sidebar_button_event_CC(self):
      self.label2.configure(text="")
      self.label3.configure(text="")  
      self.label1.configure(text="Somente CC!")
      

      print("Agora é só CC\n")

    def sidebar_button_event_Liberar_Peça(self):
        
        if self.contagem <= int(self.num):
                if self.veri_RC == True:
                    print(self.contagem, "°CC")
                    self.label2.configure(text = self.contagem)
                    self.contagem+=1
                    if self.contagem >= int(self.num)+1:
                        print("Agora é uma RC\n")
                        self.contagem = 1   
                   
                if self.veri_SUV == True:
                    print(self.contagem, "°CC")
                    self.label3.configure(text = self.contagem)
                    self.contagem+=1
                    if self.contagem >= int(self.num)+1:
                        self.contagem = 1    
                        print("Agora é uma SUV\n")
        else:
                print("Levante a Peça")

        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()