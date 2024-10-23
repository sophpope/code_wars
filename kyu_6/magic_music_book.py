"""
You are on a party with your friends and one of them suggest to play a game called "Magic Music Box". 
The game consists of a magic music box that is playing one by one all the music notes in order from DO to SI over and over. 
The goal of the game is to store in the magic music box words that contain the musical note that is being played at each moment.


In this kata you have to create a function that given an array of words returns another array with all the words that have been stored in the magic music box in the correct order.

A word can be stored in the magic music box when it contains the musical note that the box is playing at each moment. When a word is stored, the music box starts to play the next note, and so on.

The function must try to store every word from the input if possible, even if it means to retry some words that didn't fitted previuosly.

If there are no more words in the input that can be stored in the box, the function should stop and return the array with the stored words in the order they have been stored.
"""