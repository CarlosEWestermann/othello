import tkinter as tk
from enum import Enum

class BoardColors(Enum):
    TILE_COLOR = "green"
    BACKGROUND_COLOR = "black"
    PLAYER_1_COLOR = "white"
    PLAYER_2_COLOR = "black"

class PlayerCellState(Enum):
    NO_PLAYER = 0
    PLAYER_1 = 1
    PLAYER_2 = 2

class WindowDimensions(Enum):
    WIDTH = 1800
    HEIGHT = 1800

class GameRenderer:
    def __init__(self, master: tk.Tk, board_state: list[list[int]], player_1_name: str, player_2_name: str) -> None:
        self.master = master
        self.board_state = board_state
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.render_game()

    def __draw_player_piece(self, position: tuple, player: PlayerCellState) -> None:
        row, col = position
        cell_width = WindowDimensions.WIDTH.value // len(self.board_state)
        cell_height = WindowDimensions.HEIGHT.value // len(self.board_state)
        center_x = (col * cell_width) + (cell_width // 2)
        center_y = (row * cell_height) + (cell_height // 2)

        if player == PlayerCellState.PLAYER_1:
            piece_color = BoardColors.PLAYER_1_COLOR.value
        else:
            piece_color = BoardColors.PLAYER_2_COLOR.value

        piece_radius = min(cell_width, cell_height) // 4
        piece = tk.Canvas(self.master, width=piece_radius * 2, height=piece_radius * 2, bg=piece_color, highlightthickness=0)
        piece.create_oval(0, 0, piece_radius * 2, piece_radius * 2, fill=piece_color)
        piece.place(x=center_x - piece_radius, y=center_y - piece_radius)

    def __get_game_name(self) -> str:
        return self.player_1_name + " vs " + self.player_2_name

    def render_game(self):
        self.master.geometry(f"{WindowDimensions.WIDTH.value}x{WindowDimensions.HEIGHT.value}")
        self.master.title(self.__get_game_name())

        board_frame = tk.Frame(self.master, bg=BoardColors.BACKGROUND_COLOR.value)
        board_frame.pack(fill=tk.BOTH, expand=True)
        board_frame.pack_propagate(False)

        board_size = len(self.board_state)
        cell_width = WindowDimensions.WIDTH.value // board_size
        cell_height = WindowDimensions.HEIGHT.value // board_size

        for row in range(len(self.board_state)):
            for col in range(len(self.board_state[row])):
                tile_color = BoardColors.TILE_COLOR.value
                cell_frame = tk.Frame(
                    board_frame,
                    bg=tile_color,
                    highlightbackground="black",
                    highlightthickness=1,
                    width=cell_width,
                    height=cell_height
                )
                cell_frame.grid(row=row, column=col, sticky="nsew")
                
                player_state = self.board_state[row][col]
                if player_state == PlayerCellState.PLAYER_1.value:
                    self.__draw_player_piece((row, col), PlayerCellState.PLAYER_1)
                elif player_state == PlayerCellState.PLAYER_2.value:
                    self.__draw_player_piece((row, col), PlayerCellState.PLAYER_2)

board_state = [
            [0, 1, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
renderer = GameRenderer(player_1_name="Player 1", player_2_name="Player 2", board_state=board_state, master=tk.Tk())
renderer.master.mainloop()
