import copy
import random


class Hat:

    # adds balls to the contents list
    def __init__(self, **hats):
        self.hats = hats
        self.contents = []
        self.contents_copy = copy.deepcopy(self.contents)

        for key, value in hats.items():
            for i in range(value):
                self.contents.append(key)

    # draws balls at random a certain amount of times
    def draw(self, balls_to_draw):

        balls_removed = []
        if balls_to_draw > len(self.contents):
            for ball in self.contents_copy:
                self.contents.append(ball)

        for i in range(balls_to_draw):
            if len(self.contents) > 0:
                index_to_remove = random.randrange(len(self.contents))
                removed_ball = self.contents.pop(index_to_remove)
                balls_removed.append(removed_ball)
            else:
                for ball in balls_removed:
                    self.contents.append(ball)

        return balls_removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    # copied from the hat object
    # balls_in_hat = copy.deepcopy(hat.contents)
    copied_hat = copy.deepcopy(hat)

    counter = 0
    loop_completed = True
    for i in range(num_experiments):

        balls_removed = copy.deepcopy(copied_hat).draw(num_balls_drawn)
        for balls in list(expected_balls.keys()):
            actual = balls_removed.count(balls)
            expected = expected_balls[balls]
            if actual < expected:
                break
        else:
            counter += 1

    result = counter / num_experiments

    return result
