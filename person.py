import random


class Person:
    def __init__(self, name, contraction_rate):
        self.name = name
        self.candidates_name = []
        self.konkatsu_during = 0
        self.is_married = False

        self.contraction_rate = contraction_rate

    def get_name(self):
        return self.name

    def set_candidates_name(self, candidates_name):
        self.candidates_name = candidates_name

    def get_candidates_name(self):
        return self.candidates_name

    def remove_candidates(self):
        self.candidates_name = []
        self.konkatsu_during = 0

    def get_konkatsu_during(self):
        return self.konkatsu_during

    def select_new_candidate(self):
        if len(self.candidates_name) > 0:
            sample_list = round(len(self.candidates_name)
                                * self.contraction_rate)
            if sample_list == 0:
                sample_list = 1
            elif sample_list == len(self.candidates_name):
                sample_list = len(self.candidates_name) - 1

            random_list = random.sample(
                self.candidates_name, sample_list)

            self.candidates_name = random_list
            self.konkatsu_during += 1
        else:
            return

    def set_is_married(self, is_married):
        self.is_married = is_married
