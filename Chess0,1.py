positions_white_x = [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
positions_white_y = ["a", "b", "c", "d", "e", "f", "g", "h", "a", "b", "c", "d", "e", "f", "g", "h"]

positions_black_x = [7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]
positions_black_y = ["a", "b", "c", "d", "e", "f", "g", "h", "a", "b", "c", "d", "e", "f", "g", "h"]

symbols_white = ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP", "WR", "WH", "WB", "WQ", "WK", "WB", "WH", "WR"]
symbols_black = ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP", "BR", "BH", "BB", "BK", "BQ", "BB", "BH", "BR"]

def render():
    print ("_________________________")
    for i in range(8):
        row = "|"
        for idx in range(8):
            skip = 0
            for ind in range(16):
                if positions_white_x[ind] == i + 1 and positions_white_y[ind] == idx + 1:
                    row = row + symbols_white[ind]
                    row = row + "|"
                    skip = 1
            
            if skip == 0:
                for ind in range(16):
                    if positions_black_x[ind] == i + 1 and positions_black_y[ind] == idx + 1:
                        row = row + symbols_black[ind]
                        row = row + "|"
                        skip = 1
                        
            if skip == 0:
                row = row + "  |"
                
        print (row)
        print ("_________________________")
        
render()
