import copy
from person import Person


class CandidateManager:
    def __init__(self) -> None:
        self.name_list = []
        self.candidates_list = []
        self.candidate_latest_number = 0

        self.married_list = []

    def get_name_list(self):
        return self.name_list

    def get_candidates_list(self):
        return self.candidates_list

    def initialize_candidates(self, candidates_max, contraction_rate):
        name_list = []
        candidate_latest_number = 0

        for i in range(1, candidates_max + 1):
            name_list.append(str(i))
            candidate_latest_number += 1

        self.name_list = name_list
        self.candidate_latest_number = candidate_latest_number

        candidates_list = []
        for i, val in enumerate(self.name_list):
            candidates_list.append(Person(name_list[i], contraction_rate))

        self.candidates_list = candidates_list

    def make_select_new_candidates(self, all_companion_list, continue_flag):
        for i in range(0, len(self.candidates_list)):
            if (len(self.candidates_list[i].get_candidates_name()) == 0) and continue_flag:
                self.candidates_list[i].set_candidates_name(all_companion_list)

            self.candidates_list[i].select_new_candidate()

    def match_candidates(self, companion_candidates_list):
        for i, self_candidate in enumerate(self.candidates_list):
            next_candidates_name_list = []
            self_candidates_name = self_candidate.get_candidates_name()

            for self_candidate_name in self_candidates_name:
                index = None
                for companion_candidate in companion_candidates_list:
                    if companion_candidate.get_name() == self_candidate_name:
                        index = companion_candidates_list.index(
                            companion_candidate)
                        break

                companion_candidates_name = companion_candidates_list[index].get_candidates_name(
                )

                common_elements = [
                    element for element in companion_candidates_name if element in [self_candidate.get_name()]]

                if len(common_elements) > 0:
                    next_candidates_name_list.append(self_candidate_name)
                else:
                    continue

            if len(next_candidates_name_list) > 0:
                self.candidates_list[i].set_candidates_name(
                    next_candidates_name_list)
            else:
                self.candidates_list[i].set_candidates_name(
                    next_candidates_name_list)
                # print("No match candidate.")

    def judge_marriage(self, companion_candidates_list):
        married_list = []
        new_candidates_list = copy.deepcopy(self.candidates_list)
        new_name_list = copy.deepcopy(self.name_list)
        for i, self_candidate in enumerate(self.candidates_list):
            self_candidates_name = self_candidate.get_candidates_name()

            if len(self_candidates_name) == 1:
                index = None
                for companion_candidate in companion_candidates_list:
                    if companion_candidate.get_name() == self_candidates_name[0]:
                        index = companion_candidates_list.index(
                            companion_candidate)
                        break

                if index is None:
                    continue

                companion_candidates_name = companion_candidates_list[index].get_candidates_name(
                )

                if len(companion_candidates_name) == 1 and companion_candidates_name[0] == self_candidate.get_name():
                    self_candidate.set_is_married(True)
                    married_list.append(self_candidate)

                    pop_index = 0
                    for j, name in enumerate(new_name_list):
                        if name == self_candidate.get_name():
                            pop_index = j
                            break
                    new_candidates_list.pop(pop_index)
                    new_name_list.pop(pop_index)

        self.candidates_list = new_candidates_list
        self.name_list = new_name_list

        self.married_list.extend(married_list)

        married_name_list = []
        for married in married_list:
            company_name = married.get_candidates_name()
            married_name_list.append(
                married.get_name() + " -> " + company_name[0])

        return married_name_list

    def check_candidate_konkatsu_all_stopped(self):
        all_stopped_flag = True
        for candidate in self.candidates_list:
            if len(candidate.get_candidates_name()) > 0:
                all_stopped_flag = False

        return all_stopped_flag
