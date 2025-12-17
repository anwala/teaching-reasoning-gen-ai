# Web Crawler

## Introduction

Recall in Module 4 we were [introduced](https://docs.google.com/presentation/d/1L0mk2dnBPvD_wZlaj3fCbPwaIxmboC2sV9Z0hQqkc4M/edit?slide=id.g3a44747e5f3_0_0#slide=id.g3a44747e5f3_0_0) to the [Web Crawler](https://en.wikipedia.org/wiki/Web_crawler) (or robot): a program that systematically searches the web and indexes the content. We also built a [simple Web Crawler](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anwala/teaching-reasoning-gen-ai/blob/main/spring-2026/modules/module-04/data_102_02_s26_mod_04_python_crawler.ipynb).

Here, we will revisit the problem of building a crawler, but this time with the aid of Generative AI and assess and reflect on the pros/cons of the development process with and without the use of GenAI.

## (In-class individual activity): Building a web crawler with GenAI

Design separate prompts for each of the following tasks using PSP to:
1. Learn about the Web Crawling and challenges of Web Crawling
2. Learn about the Web Crawler program and identify its main components
3. Implement the components of the Web Crawler identified in 2.
4. Merge the subcomponent of the Web Crawler in 3. to form a complete Web Crawler
5. Learn about testing the Web Crawler 
6. Identify seed URLs to test the Web Crawler
7. Test the Web Crawler

Let's reflect. Lets vote for a Wild Card Program for next time.

# 3D Tic-Tac-Toe

## Introduction/rules

Here, we will apply our PSP to implement a 2 player 3D Tic-Tac-Toe game which will operate as follows.
1. The game will begin by printing the board, three 2D Tic Tac Toe boards numbered 1 -- 27 (1 -- 9: first board, 10 -- 18: second board, 19 -- 27: third board).
2. The first player would be X, and the second, O
3. At each turn a player selects a position on board a board by selecting numbers from 1 -- 27
4. After each play, the program should check for a win and stop the game to declare the winner on the event of a win.
5. The game continues until a player wins or all positions are exhausted at which point the program declares a draw.

## Building a 2 player 3D Tic-Tac-Toe game with GenAI

Let us apply PSP to solve this problem
1. What are the subproblem?
2. Let us design prompts to solve each subproblem.
3. Let us solve the whole problem by stitching solutions of subproblems
4. Let evaluate and iterate and reflect.

Note:
Since Tic-Tac-Toe is a common game, you could easily prompt the LLM to produce code for the game and get a decent result. However, this process would rob you of the opportunity to develop your problem-solving skill; the ability to go from knowing nothing about a subject, to navigating little or vast amounts of information to address questions, and develop an understanding of the subject. This process is not straightforward, sometimes it involves trial and error through experimentation. It can be frustrating and difficult and requires patience and diligence. But developing good problem-solving skills is rewarding and gives you the ability to be entrusted with solving problems. And since a lot of the problems you'll face in the real world would not be easily solvable with one prompt, it's a good idea to start developoinog the skills needed to tackle such problems.

