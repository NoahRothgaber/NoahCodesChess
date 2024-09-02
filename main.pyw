# Example file showing a basic pygame "game loop"
import pygame


white_piece_names = [
    'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn',
    'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn',
    'white_rook', 'white_knight', 'white_bishop', 'white_queen',
    'white_king', 'white_bishop', 'white_knight', 'white_rook'
]

black_piece_names = [
    'black_rook', 'black_knight', 'black_bishop', 'black_queen',
    'black_king', 'black_bishop', 'black_knight', 'black_rook',
    'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn',
    'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn',
]
positions_pose = {}
positions = [
    'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
    'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
    'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
    'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
    'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
    'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
    'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
    'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'
]
# pygame setup

class ChessGame:
    def __init__(self):
        self.piece_list = []
        pygame.init()
        self.screen = pygame.display.set_mode((451, 451))
        pygame.display.set_caption("Noah Codes Chess!")
        icon = pygame.image.load('assets/knightW3.png')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.running = True
        self.background = pygame.image.load("assets/board1.png").convert_alpha()
        self.black_rook_v1 = pygame.image.load("assets/rookB2.png").convert_alpha()
        self.black_knight_v1 = pygame.image.load("assets/knightB2.png").convert_alpha()
        self.black_bishop_v1 = pygame.image.load("assets/bishopB2.png").convert_alpha()
        self.black_queen_v1 = pygame.image.load("assets/queenB2.png").convert_alpha()
        self.black_king_v1 = pygame.image.load("assets/kingB2.png").convert_alpha()
        self.black_pawn_v1 = pygame.image.load("assets/pawnB2.png").convert_alpha()
        self.white_rook_v1 = pygame.image.load("assets/rookW2.png").convert_alpha()
        self.white_knight_v1 = pygame.image.load("assets/knightW2.png").convert_alpha()
        self.white_bishop_v1 = pygame.image.load("assets/bishopW2.png").convert_alpha()
        self.white_queen_v1 = pygame.image.load("assets/queenW2.png").convert_alpha()
        self.white_king_v1 = pygame.image.load("assets/kingW2.png").convert_alpha()
        self.white_pawn_v1 = pygame.image.load("assets/pawnW2.png").convert_alpha()

        self.white_piece_image_list = [
            self.white_pawn_v1, self.white_pawn_v1, self.white_pawn_v1, self.white_pawn_v1,
            self.white_pawn_v1, self.white_pawn_v1, self.white_pawn_v1, self.white_pawn_v1,
            self.white_rook_v1, self.white_knight_v1, self.white_bishop_v1, self.white_queen_v1,
            self.white_king_v1, self.white_bishop_v1, self.white_knight_v1, self.white_rook_v1
        ]

        self.black_piece_image_list = [
            self.black_rook_v1, self.black_knight_v1, self.black_bishop_v1, self.black_queen_v1,
            self.black_king_v1, self.black_bishop_v1, self.black_knight_v1, self.black_rook_v1,
            self.black_pawn_v1, self.black_pawn_v1, self.black_pawn_v1, self.black_pawn_v1,
            self.black_pawn_v1, self.black_pawn_v1, self.black_pawn_v1, self.black_pawn_v1
        ]

        self.currrent_turn = "White"

        self.white_pieces = []
        self.black_pieces = []

    def current_player_pieces(self):
        if self.currrent_turn == "White":
            return self.white_pieces
        else:
            return self.black_pieces

    def run_game(self):
        self.setup_board()
        piece_selected = None
        piece_selected_original_pose = ()      
        while self.running:
            self.screen.blit(self.background, (0,0))
            self.render_pieces()       
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type ==pygame.MOUSEBUTTONDOWN and not piece_selected:
                    for piece in self.current_player_pieces():
                        if piece.piece_image is not None:
                            if piece.hitbox.collidepoint(event.pos):
                                print(f'Collision! Piece Name {piece.name} on {piece.coord}')
                                piece_selected = piece
                                piece_selected_original_pose = piece.hitbox.copy()
                elif event.type == pygame.MOUSEBUTTONDOWN and piece_selected:
                    # main valid move check
                    print("Clicked with piece on mouse")
                    print(piece_selected.hitbox)
                    self.check_valid_move(square_selected=destination_square)
                    print(piece_selected.hitbox)
                elif piece_selected and event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    piece_selected.hitbox.center = mouse_x, mouse_y
                    piece_selected.image_top_left = mouse_x, mouse_y
                    print(piece_selected.hitbox)  

                # fill the screen with a color to wipe away anything from last frame
                #black_knight_1_v1 =
                self.screen.blit(self.background, (0,0))
                self.render_pieces()
            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()


    def check_valid_move(self, square_selected):
        existing_piece = None
        if self.piece_selected.name == "white_pawn" or "black_pawn":    
            
                for piece in self.piece_list:
                    if square_selected == piece.hitbox:
                        existing_piece = piece
                if not existing_piece:
                    self.piece_selected.hitbox = square_selected
                
        elif existing_piece:
            pass
        elif self.piece_selected.name == "white_knight" or "black_knight":
            pass
        elif self.piece_selected.name == "white_bishop" or "black_bishop":
            pass
        elif self.piece_selected.name == "white_queen" or "black_queen":
            pass
        elif self.piece_selected.name == "white_king" or "black_king":
            pass

    def setup_board(self):
        x = 14
        y = 14
        count = 1
        starter_pieces = 0
        for position in positions:
            piece = None
            piece_name =''
            piece_image = None
            if starter_pieces < 16:
                piece_image = self.black_piece_image_list[starter_pieces]
                piece_name = black_piece_names[starter_pieces]
                piece_hitbox = piece_image.get_rect(topleft=(x, y))
                piece = Piece(position, (x,y), piece_image, piece_name, piece_hitbox)
                self.black_pieces.append(piece)
                print(piece.name)
            elif starter_pieces > 47:
                piece_image = self.white_piece_image_list[starter_pieces % 48]
                piece_name = white_piece_names[starter_pieces % 48 ]
                piece_hitbox = piece_image.get_rect(topleft=(x, y))
                piece = Piece(position, (x,y), piece_image, piece_name, piece_hitbox)
                self.white_pieces.append(piece)
                print(piece.name)    
            if count % 8 == 0:
                x = 14
                y += 53
            else:
                x += 53
            count += 1
            starter_pieces += 1
    
    def render_pieces(self):
        for piece in self.white_pieces:
            if piece.piece_image is not None:
                self.screen.blit(piece.piece_image, piece.hitbox.topleft)
        
        for piece in self.black_pieces:
            if piece.piece_image is not None:
                self.screen.blit(piece.piece_image, piece.hitbox.topleft)

class Piece:
    def __init__(self, square, top_left_coord, image, piece_name, piece_hitbox):
        self.coord = square
        self.image_top_left = top_left_coord
        self.piece_image = image
        self.name = piece_name
        self.hitbox = piece_hitbox 
    coord = ''
    image_top_left = ()
    name = ''
    hitbox = None
    moved = False

def main():
    game = ChessGame()
    game.run_game()

if __name__ == "__main__":
    main()