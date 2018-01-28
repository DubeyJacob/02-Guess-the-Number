The goal of this program is to have a user try to guess a number between 1 and 20 within 5 guesses. The
player also has the opportunity to input their own name to make the game seem more intimate.
The import sys,random command imports those specific libraries to this program. The random library is the
most important to this program. Before getting into any coding, there were variables that needed to be 
initially defined.In the lines 8 and 9, variables 'guesses' and 'guess_range' were defined. 'guesses' was
defined as 0 so that when providing feedback to the player during the game, the guess counter would
increase accordingly. Next I wanted to make the game more intimate by asking the player for their name.
Whatever their input, it would also be defined as Name which would be included in future strings. The
next block defined the number as a random integer between 1 and the 'guess_range' which in this case was
20. The next block is a short description of the rules in a very fun manner putting the situation in terms
apples instead of just numbers. In it it will also display the name the player gave at the beginning of
the game. Then it will print an instruction of 'Guess how many apples are in my bag. You have 5 guesses.'
Next comes the loop. It is a while loop for as long as the guesses < 5. As long as guesses are less 5,
the user will be able to input an answer with the guess = input() command. 'Guess' is then converted
into an integer. There is then a command that makes the guess counter increase by one for every time
through the loop. There are then several conditions organized by the 'if' function. The first of which
is if the guess is < the number. If this is the case then the 'guesses' is converted into a string
so that it can be inserted in the string that tells the player that they guessed too low and to try again.
The guesses is converted into a string here so that it shows up. Afterword it is then converted back into
an integer and the loop starts again from the top. The next condition is if the guess is > the number. The
same set of commands are in place in terms of converting the 'guesses' into a string. The print then tells
the player that their guess was too high and the 'guesses' will be inserted as well to tell the player
how many guesses they have made. The 'guesses' is then converted back into an integer and the loop starts
again. The last condition is if the guess is equal to the number in which case the loop breaks and moves on
to the next part of code. The other way the loop would break is if the guesses exceed or meet the total of
5. The expression would no longer be True and would then move on in the code. At this point if the number
is correct then the 'guesses' will be converted to string and the program will print a string that
congratulates the player (using the inputed name) and tells them how many guesses it took them. At this point
if the number was still not correct after the 5 guesses then the number will be converted to string and then
a string will print telling the player what the correct answer was. In the program there is an except command
where if the player inputs an answer that is not a whole number the game will tell the player to enter a 
whole number. This function is currently not working as once something that is not a whole number is entered
the program then ends. This is something I am still looking into on how to fix it.