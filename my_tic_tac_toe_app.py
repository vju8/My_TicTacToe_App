import tkinter as tk
import random 
from PIL import Image, ImageTk
from tkinter import messagebox


class MyTicTacToe():

    
    def __init__(self): 
        """ Constructor function."""
        
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe Game")
        self.root.configure(background='#F7E7CE')    
        self.root.iconphoto(False, tk.PhotoImage(file="tic-tac-toe.png"))
        self.root.resizable(False,False)
        self.open_main_window()
        self.root.mainloop()
        
        
    def open_main_window(self): 
        """
        Function responsible for opening the main menu game window with 
        the game choices.
        """
        
        def resize_image(image):
            """
            Function responsible for resizing images.
            """

            new_width = 130
            new_height = 130
            resized_image = image.resize((new_width, new_height), Image.LANCZOS)
            return ImageTk.PhotoImage(resized_image)
    
       
        # clear any existing widgets
        self.clear_widgets()
        # set up the perfect geometry for the window
        self.root.geometry("+550+200")
        
        self.menu_frame = tk.Frame(self.root, bg = "#DCAE96")
        self.menu_frame.pack(padx = 20, pady = 20)
        
        self.main_label = tk.Label(self.menu_frame, text = "Tic-Tac-Toe Game", bg = "#DCAE96", font = ("Arial", 28, "bold"))
        self.main_label.pack(padx = 10, pady = 5)
        
        main_picture = Image.open("tic-tac-toe.png")
        self.main_picture_resized = resize_image(main_picture)         
        self.main_picture_label = tk.Label(self.menu_frame, image = self.main_picture_resized)
        self.main_picture_label.pack(pady = 10)
        # reference the images (need to keep the reference of your image to avoid garbage collection)
        self.main_picture_label.image = self.main_picture_resized
        
        self.play_solo_button = tk.Button(self.menu_frame, text = "Solo Play against PC", bg = "#4B3832", fg = "white", font = ("Arial", 18), command = lambda: self.open_new_game_window(game_mode = "solo"))
        self.play_solo_button.pack(fill = "x", pady = 5)
        
        self.play_multi_button = tk.Button(self.menu_frame, text = "Play with a Friend", bg = "#4B3832", fg = "white", font = ("Arial", 18), command = lambda: self.open_new_game_window(game_mode = "multi"))
        self.play_multi_button.pack(fill = "x", pady = 5)
        
        self.exit_button = tk.Button(self.menu_frame, text = "Exit", bg = "#4B3832", fg = "white", font = ("Arial", 18), command = self.on_closing)
        self.exit_button.pack(fill = "x", pady = 5)
        
           
    def open_new_game_window(self, game_mode):
        """
        Function responsible for creating a new game window with all it's
        i^nitial widgets.
        """
        
        # clear any existing widgets
        self.clear_widgets()
        # set up the perfect geometry for the window
        self.root.geometry("+550+50")
        
        # first player to play is always "X"
        self.current_player = "X"
        # flag game_over needed to stop the game when a result (win or draw) is reached
        self.game_over = False
        
        # input the game mode
        self.game_mode = game_mode
        print("\nNEW GAME STARTED")
        print(f"You selecte mode: {self.game_mode}\n")
        
        self.game_title = tk.Label(self.root, text = "Tic-Tac-Toe Game", bg = "#F7E7CE", font = ("Arial", 28, "bold"))
        self.game_title.pack(padx = 20, pady = 20)
        
        self.mode_label = tk.Label(self.root, text = f"Game Mode: {self.game_mode.capitalize()}", bg = "#F7E7CE", font = ("Arial", 18))
        self.mode_label.pack(padx = 20, pady = (0, 5))
        
        if self.game_mode == "multi": 
            self.turn_label = tk.Label(self.root, text = f"{self.current_player} Turn", bg = "#F7E7CE", font = ("Arial", 18))
            self.turn_label.pack(padx = 20, pady = (0, 5))
        
        self.winner_label = tk.Label(self.root, text = "", bg = "#F7E7CE", fg = "green", font = ("Arial", 18))
        self.winner_label.pack(padx = 20, pady = (0, 5))
        
        self.game_frame = tk.Frame(self.root, bg = "#DCAE96")
        self.game_frame.pack(padx = 20, pady = 20)
        
        # create a nested list to store the future tkinter button objects
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # create the buttons, add them to buttons nested list and position them using grid layout manager
        for row in range(3): 
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.game_frame, text = "", width = 8, height = 4, font = ("Arial", 18), command = lambda r = row, c = col: self.next_move(r, c))
                self.buttons[row][col].grid(row = row, column = col, padx = 2, pady = 2)
        
        # adding the back button
        self.back_button = tk.Button(self.root, text = "Back", width = 20, bg = "#DCAE96", fg = "black", font = ("Arial", 18), command = self.open_main_window)
        self.back_button.pack(pady = (0, 20))
        # print(f"The sign now is {self.current_player}")
        
        
    def on_closing(self):
        """
        Function responsible for creating a yesno messagebox for the user 
        and based on the input either keep or destroy the tkinter window.
        """
        
        # when closing the app, ask user if he is sure (yes/no)
        if messagebox.askyesno(title = "Quit?",
                               message = "Do you really want to quit?"):
            self.root.destroy()    
     
        
    def clear_widgets(self):
        """
        Function responsible for clearing the widgets from the root frame 
        when switching between windows and game modes.
        """
        
        # Clear all widgets from the window
        for widget in self.root.winfo_children():
            widget.destroy()    
    
    
    def check_empty_cells(self):
        """
        Function responsible for finding the empty cells on the boards in 
        order for the computer to chose a random cell for the next move.
        """

        empty_cells = [[row, col] for row in range(3) for col in range(3) if self.buttons[row][col]["text"] == ""]
        return random.choice(empty_cells) 
    
    
    def computer_move(self): 
        """
        Function reponsible to perform the computer move based on the random 
        principle of finding an empty spot in the two dimensional matrix 
        representing the board of the game.
        """
        
        row, col = self.check_empty_cells()
        # print(row, col)
        button = self.buttons[row][col]
        # print(f"Button clicked: Row {row}, Column {col}")
        button.config(text = f"{self.current_player}")
    
   
    def next_move(self, row, col):
        """
        Function responsible to perform the next move when clicking on a 
        button. This may happen by real click of a player or automatically 
        by the computer.
        """
        
        
        if self.game_mode == "solo":
            button = self.buttons[row][col] 
            cell_content = button.cget("text")
            
            if cell_content == "":
                
                if self.current_player == "X" and self.game_over == False:
                    # print(f"Button clicked: Row {row}, Column {col}")
                    button.config(text = f"{self.current_player}")
                    self.check_result()
                
                self.current_player = "O"

                if self.current_player == "O" and self.game_over == False:
                    self.computer_move()
                    self.check_result()
                    self.current_player = "X"
            else: 
                print("Cell is already taken.")
        
        else: 
            button = self.buttons[row][col] 
            cell_content = button.cget("text")
            
            if cell_content == "":
                # print(f"Button clicked: Row {row}, Column {col}")
                button.config(text = f"{self.current_player}")
                self.check_result()
                self.current_player = "O" if self.current_player == "X" else "X"
            else: 
                print("Cell is already taken.")
                
            if self.game_over is not True:
                self.turn_label.config(text = f"{self.current_player} Turn")
    
    
    def check_result(self):
        """
        Function responsible to check the result after each move and clarify 
        which player won or if it's a draw.
        """
        
        # WIN CASE 1 (horizontals):
        for row in range(3): 
            if (self.buttons[row][0].cget("text") == self.buttons[row][1].cget("text") == self.buttons[row][2].cget("text")) and (self.buttons[row][0].cget("text") != "") and (self.game_over == False):
                print(f"\n{self.current_player} IS THE WINNER")
                self.winner_label.config(text = f"{self.current_player} IS THE WINNER")
                self.game_over = True
                self.disable_board()

        # WIN CASE 2 (verticals):
        for col in range(3): 
            if (self.buttons[0][col].cget("text") == self.buttons[1][col].cget("text") == self.buttons[2][col].cget("text")) and (self.buttons[0][col].cget("text") != "") and (self.game_over == False):
                print(f"\n{self.current_player} IS THE WINNER")        
                self.winner_label.config(text = f"{self.current_player} IS THE WINNER")
                self.game_over = True
                self.disable_board()

        # WIN CASE 3 (diagonal 1):
        if (self.buttons[0][0].cget("text") == self.buttons[1][1].cget("text") == self.buttons[2][2].cget("text")) and (self.buttons[1][1].cget("text") != "") and (self.game_over == False):
            print(f"\n{self.current_player} IS THE WINNER")    
            self.winner_label.config(text = f"{self.current_player} IS THE WINNER")
            self.game_over = True
            self.disable_board()

        # WIN CASE 4 (diagonal 2):
        if (self.buttons[2][0].cget("text") == self.buttons[1][1].cget("text") == self.buttons[0][2].cget("text")) and (self.buttons[1][1].cget("text") != "") and (self.game_over == False):
            print(f"\n{self.current_player} IS THE WINNER")    
            self.winner_label.config(text = f"{self.current_player} IS THE WINNER")    
            self.game_over = True
            self.disable_board()

        # DRAW CASE
        if all(button_text["text"] != "" for button_text in self.game_frame.winfo_children()) and self.game_over == False:
            print("\nIT'S A DRAW")    
            self.winner_label.config(text = "IT'S A DRAW")
            self.game_over = True
            self.disable_board()


    
    def disable_board(self): 
        """
        Function responsible to set the state of the buttons in the game_frame
        to disabled, as soon as the win or draw situation is met. Also when 
        multiplayer mode is played, the turn label changes to 'GAME OVER'.
        """
        
        if self.game_mode == "multi":
            self.turn_label.config(text = "GAME OVER")
        
        for button in self.game_frame.winfo_children():
            button["state"] = "disabled"
                        
        
        
if __name__ == "__main__":
    
    tictactoe_app = MyTicTacToe()
