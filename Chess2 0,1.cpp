#include <iostream>
#include <list>
using namespace std;

void render(list<char>* letters, list<int>* positions_white_y, list<char>* positions_white_x, list<int>* positions_black_y, list<char>* positions_black_x, list<string>* symbols_white, list<string>* symbols_black);

int main()
{
    list<char> letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'};

    list<int> positions_white_y = {2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1};
    list<char> positions_white_x = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'};

    list<int> positions_black_y = {7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8};
    list<char> positions_black_x = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'};

    list<string> symbols_white = {"WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP", "WR", "WH", "WB", "WK", "WQ", "WB", "WH", "WR"};
    list<string> symbols_black = {"BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP", "BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR"};

    render(&letters, &positions_white_y, &positions_white_x, &positions_black_y, &positions_black_x, &symbols_white, &symbols_black);
    return 0;
}

void render(list<char>* letters, list<int>* positions_white_y, list<char>* positions_white_x, list<int>* positions_black_y, list<char>* positions_black_x, list<string>* symbols_white, list<string>* symbols_black)
{
    cout << "_________________________" << endl;
    int skip;
    for (int i = 0; i < 8; i++)
    {
        cout << "|";
        for (int idx = 0; idx < 8; idx++)
        {
            skip = 0;
            auto it_white_y = positions_white_y->begin();
            auto it_white_x = positions_white_x->begin();
            auto it_white_sym = symbols_white->begin();
            for (int ind = 0; ind < 16; ind++, ++it_white_y, ++it_white_x, ++it_white_sym)
            {
                if (*it_white_y == i + 1 && *it_white_x == *next(letters->begin(), idx))
                {
                    cout << *it_white_sym << "|";
                    skip = 1;
                    break;
                }
            }

            if (skip == 0)
            {
                auto it_black_y = positions_black_y->begin();
                auto it_black_x = positions_black_x->begin();
                auto it_black_sym = symbols_black->begin();
                for (int ind = 0; ind < 16; ind++, ++it_black_y, ++it_black_x, ++it_black_sym)
                {
                    if (*it_black_y == i + 1 && *it_black_x == *next(letters->begin(), idx))
                    {
                        cout << *it_black_sym << "|";
                        skip = 1;
                        break;
                    }
                }
            }

            if (skip == 0)
            {
                cout << "  |";
            }
        }
        cout << endl;
        cout << "_________________________" << endl;
    }
}
