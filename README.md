# Coding-Challenges
This repository contains a group of exercises I have done in a week while learning Python.
Exercises were taken from LeetCode. These were chosen by Keith Galli in his video "Solving Coding Interview Questions in Python on LeetCode (easy & medium problems)".

* Keith Galli's YouTube Channel: https://www.youtube.com/c/KGMIT

## Why all of this?
I have been learning Python since right before 2022 began. So to test my knowledge on the matter I deciced to take on some coding interview exercises.

## List of exercises
* **Goal parser**: You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order. Given the string command, return the Goal Parser's interpretation of command.
* **Destination City**: You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city. It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
* **How Many Numbers Are Smaller Than the Current Number**: Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]. Return the answer in an array.
* **Binary Search**: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.
* **Longest Palindrome**: Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
* **Maximum Number of Coins You Can Get**: 
  There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
  * In each step, you will choose any 3 piles of coins (not necessarily consecutive).
  * Of your choice, Alice will pick the pile with the maximum number of coins.
  * You will pick the next pile with the maximum number of coins.
  * Your friend Bob will pick the last pile.
  * Repeat until there are no more piles of coins.
  Given an array of integers piles where piles[i] is the number of coins in the ith pile. Return the maximum number of coins that you can have.
* **Design browser history**: 
  You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.
  Implement the BrowserHistory class:
  * BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
  * void visit(string url) Visits url from the current page. It clears up all the forward history.
  * string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
  * string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
* **Delete Nodes And Return Forest**: Given the root of a binary tree, each node in the tree has a distinct value. After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees). Return the roots of the trees in the remaining forest. You may return the result in any order.
