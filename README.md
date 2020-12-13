# Simple Tic-Tac-Toe game using Minimax Alpha-Beta Pruning written in Python

This is a Tic-Tac-Toe game using Minimax Algorithm with Alpha-Beta Pruning in Python. It will choose the move with maximum score when it is the AI's turn and choose the move with the minimum score when it is the human player's turn. Using this strategy in this game, AI player avoids losing to the human player, mostly will win if it play first and will tie if it play second.

### Minimax Algorithm
Minimax is used in decision making and game theory for minimizing the possible loss for a worst case (maximum loss) scenario and to find the optimal move for a player assuming that the other player is also playing optimally. It's widely used in two player turn-based games such as Tic-Tac-Toe, Chess, Mancala, Go,... - [wiki](https://en.wikipedia.org/wiki/Minimax)

### Alpha-Beta Pruning
Alpha–Beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It is an adversarial search algorithm used commonly for machine playing of two-player games - [wiki](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

### How to run the program
- First, clone the repo
```
git clone https://github.com/lannguyen0910/minimax_tictactoe
```

- Second, go to repo folder 
```
cd */minimax_tictactoe
```

- Third, run the game using the command line
```
python play.py
```

### Result
![Result1](result/1.png) ![Result2](result/2.png)

### Preference
Youtube: The Coding Train - [link](https://www.youtube.com/watch?v=trKjYdBASyQ&feature=emb_logo)
