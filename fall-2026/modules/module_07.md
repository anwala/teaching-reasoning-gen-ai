# Programming with LLMs

## Introduction

Whatever your career aspiration, programming is a useful fun way to increase your productivity. It used to be something just for the computer nerds/scientists but things have changed; especially since the release of Generative AI tools like ChatGPT which can generate code. Journalists, business analysts, researchers, etc., can now boost their productivity and convert ideas into software prototypes with programming aided of GenAI.

Here, we will learn how to develop applications in Python using Generative AI technologies guided by the our Problem Solving Philosophy (PSP):
* Decomposing non-trivial problems into actionable and testable subproblems
* Developing algorithms to solve subproblems
* Implementing and evaluating Python-based solutions and iterating.

## [Random Surfer on Wikipedia](https://en.wikipedia.org/wiki/Random_surfing_model)

**Goal:** Using the [Python wikipedia tool](https://pypi.org/project/wikipedia/), develop re-usable code for visiting Wikipedia pages randomly. Given a start Wikipedia page (at distance 0), e.g., [College of William and Mary](https://en.wikipedia.org/wiki/College_of_William_and_Mary)
and `max_distance`, the program should visit a random page (at distance 1) that the start page links to, and visit a random page (at distance 2) that the random page links to. This process should repeat `max_distance` times, at which point the program should return a random Wikipedia page. The program should plot a path illustrating the surfing.

Let's apply PSP to solve this problem:
1. What are the subproblem?
2. Design prompts to solve each subproblem.
3. Solve whole problem by stitching solutions of subproblems
4. Evaluate and iterate.

## Summary statistics program (In-class individual task)
**Goal:** Develop re-usable code for a company. Create a program that reads an employee's first name and salary and store them into two separate lists. The number of employees is unknown. To exit the program the user must input "done". Before exiting find the average salary and for each employee print if their salary is above or below average salary.

For example:
```
Welcome to Salary Audit:
Enter employee first names followed by their salary: Mary 2343, John 2134, George 5342, Nicole 5342, done.

Total Employees: 2
Average Salary is: $3790.25

Auditing:

Mary's salary is below average
John's salary is below average
George's salary is above average
Nicole's salary is above average
```

Apply PSP to solve this problem:
1. What are the subproblem?
2. Design prompts to solve each subproblem.
3. Solve whole problem by stitching solutions of subproblems
4. Evaluate and iterate.

Let's reflect.

### Tips:
* Be curious and adventurous. Ask question and test things out and learn why/how the code works
* Run code
* Errors are expected
* Try understanding any GenAI-produced code.
* Patience
* Evaluate
* Keep It Simple (KIS!): 