# **Design Document: Blackjack**

# **1.1: Getting Started**
 
Welcome to the game of Blackjack! In order to play the game, you have to download the file **blackjack1.py** from my GitHub repository and put it into a folder on your desktop. Next, type **cd ~/Desktop/(insert folder name)** in the terminal. To run the program, type **python3 blackjack1.py**. Now, get ready to have some fun with the game!

# **1.2: Classes**

## **Card**
- This class represents all the cards in the Deck from which the Dealer draws from. Each card has a rank, a suit, and a point value ranging from 1 to 11.
## **Deck**
- This class represents a standard 52-card deck, which contains 13 different cards from each of the four suits (Spades, Hearts, Diamonds, Clubs). 
## **Hand**
- This class represents both the Player's hand as well as the Dealer’s hand. It keeps track of what cards the Player and the Dealer have.
## **Chips**
- This class represents the chips of the Player. It keeps track of the current amount of money that the Player has, the decisions as well as the bets that the Player makes.
## **Game**
- This class runs the entire game and updates the state of the game with each new turn. In addition to dealing the cards from the Deck to the Player and the Dealer, it responds to the actions of the Player. The Game also takes in and pays out bets made by the Player.

# **1.3: How to Play**

In this section, I will go over how to play the game as well as any special features that I have implemented in the game.

## **Placing Bets**
- At the start of each round, the Game will ask you to place a bet. Put any amount you are willing to risk.

## **Dealing Hands**
- Once you have placed your bet, the Game will then deal two cards from the deck to both you and the Dealer. 

## **Looking at your Cards**
- In my version of Blackjack, I assign the card values as such: {2 → 2, 3 → 3, 4 → 4, 5 → 5, 6 → 6, 7 → 7, 8 → 8, 9 → 9, 10 → 10, Jack → 10, Queen → 10, King → 10, Ace → 1 or 11}. Based on the two cards you have, you can perform different actions:

- ### **Hit**
  - This means you draw another card. The rule of thumb is that if your hand has a value of 17 or greater, you do not hit. If you end up going over 21, you bust and lose the game.
- ### **Tip**
  - This gives you the chance to ask the Dealer for advice on what to do next depending on what cards the Dealer and you already have.
- ### **Stand**
  - This means you stop drawing any more cards. Your current hand value  will be compared against the Dealer’s hand.
- ### **Double Down**
  - If you are feeling adventurous, you can double your bet and get an additional card. The risk involved is that you can only draw one more card!

## **Payout**
- Depending on the outcome of the round, you will either gain two or four times (double down) the amount of money you bet if you win, or you will get nothing at all if you lose. In the case of a tie, your bet will be returned.

# **1.4: Test Cases**

To ensure that the tip function of Blackjack runs as intended, I created the following test cases to check if the players will receive effective advice from my program to increase their win rate.

- If the Dealer’s card shown is between 2 - 6 and the Player’s hand value is less than or equal to 11, the program should recommend the Player to hit.
- If the Dealer’s card shown is between 2 - 6 and the Player’s hand value is more than 11, the program should recommend the Player to stand.
- If the Dealer’s card shown is between 2 - 6 and the Player’s hand value is either 10 or 11, the program should recommend the Player to double down.
- If the Player’s hand value is 17 or more, disregarding what the Dealer’s card is, the program should recommend the Player to stand.

In addition, since an ace can be worth one or eleven, I created the following test cases to check the expected hand value when the Player’s hand contains one or more aces.

- Drawing one ace should return a value of either one or eleven, depending on the value of the other card of the Player.
- Drawing two aces should return a value of either two or twelve.
- Drawing three aces should return a value of either three or thirteen.
- Drawing four aces should return a value of either four or fourteen.

# **1.5: Final Thoughts**

When I first looked at the Engineering Challenge, I knew I had to use a language and pick a game that I am familiar with in order to finish it within three hours. After careful consideration, I decided to build a Blackjack game in Python. One of the main reasons why I chose Python for the challenge is that Python is portable, expandable, and embeddable, allowing for my game to be run on any computer regardless of the architecture or operating system. In addition, Python is the language of choice because of its clean syntax, making it easily readable which helps reduce the amount of time I need to spend on debugging the code. Furthermore, Python is an interpreted language, which means I can test my game quickly without having to compile the code each time I make any changes. The availability of Python’s random library also makes it possible for me to employ the shuffle function to emulate the shuffling of the deck of cards in the game. With all these benefits, I was able to complete the challenge within the suggested time limit. As for the classes I implemented, each of them was chosen to represent the different parts of a Blackjack game. In particular, the Deck and Card classes were designed in such a way that they could be extended for other card games such as Texas Hold’em as well as Bridge. Overall, I had a lot of fun implementing the game of Blackjack for the Engineering Challenge. I hope you have fun playing the game too!

