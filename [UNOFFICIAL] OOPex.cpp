#include <iostream>
#include <list>
using namespace std;

enum Piece
{
    white_pawn,
    white_rook,
    white_horse,
    white_bishop,
    white_king,
    white_queen,
    black_pawn,
    black_rook,
    black_horse,
    black_bishop,
    black_king,
    black_queen
};

enum Code
{
    WP,
    WR,
    WH,
    WB,
    WK,
    WQ,
    BP,
    BR,
    BH,
    BB,
    BK,
    BQ
};

enum State
{
    alive,
    dead,
    safe,
    checked
};

class Pieces
{
public:
    char posX;
    int posY;
    Piece piece;
    Code code;
    State state;
    Pieces(char x, int y, Piece p, Code c, State s) : posX(x), posY(y), piece(p), code(c), state(s) {}
    
    void details()
    {
        cout << piece << ": " << posY << posX;
    }

};

int main()
{
    list<Pieces> white_pieces;
    white_pieces.push_back(Pieces('a', 2, white_pawn, WP, alive));

    return 0;
}
