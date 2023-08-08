import prob_calculator

hat1 = prob_calculator.Hat(yellow=5, blue=3)

print(prob_calculator.experiment(hat1,
                           expected_balls={"yellow": 1, "blue": 1},
                           num_balls_drawn=2,
                           num_experiments=50))
