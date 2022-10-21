HOW TO RUN
-----------
To run all the algorithms at once:
    'python Analysis.py'
By default it runs on 1000 random initial states. 
To specify the number of initial states to generate:
    'python Analysis.py 500'

To run only Hill-Climbing algorithms on one case: 'python HillClimbing.py'
To run only Simulated-Annealing on one case: 'python SimulatedAnnealing.py'

RESULTS
--------
- Both Hill-Climbing algorithms without any sideways moves can solve around 14% of all the test cases.
- With a maximum of 100 consecutive sideways moves allowed, they can both solve 94% of the test cases.

- Steepest-Ascent takes 4 steps on average when it finds the solution
- Whereas, 'First Choice' takes 6 steps on average.

- Simulated Annealing needs a significantly higher number of steps to solve the problem.
- The same was observed with many different scheduling functions: 500/(t^3), 0.2/log(t+1), 400x(0.99^t), 100/10^(t+1)

- With the schedule 500/(t^3) it solved ~60% of the cases and took around 231.5 steps per solved case on average.