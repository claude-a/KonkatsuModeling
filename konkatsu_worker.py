import copy
from candidate_manager import CandidateManager


class KonkatsuWorker:
    def __init__(self) -> None:
        self.men_candidate_manager = CandidateManager()
        self.women_candidate_manager = CandidateManager()

    def run_one_konkatsu_cycle(self, candidates_max, contraction_rate):
        self.men_candidate_manager = CandidateManager()
        self.women_candidate_manager = CandidateManager()

        self.men_candidate_manager.initialize_candidates(
            candidates_max, contraction_rate)
        self.women_candidate_manager.initialize_candidates(
            candidates_max, contraction_rate)

        loop_num = 0
        loop_end_flag = False
        total_married_pairs_number = 0

        while loop_end_flag == False:
            men_name_list = self.men_candidate_manager.get_name_list()
            women_name_list = self.women_candidate_manager.get_name_list()

            if loop_num == 0:
                konkatsu_continue_flag = True
            else:
                konkatsu_continue_flag = False

            self.men_candidate_manager.make_select_new_candidates(
                women_name_list, konkatsu_continue_flag)
            self.women_candidate_manager.make_select_new_candidates(
                men_name_list, konkatsu_continue_flag)

            men_candidates_list = copy.deepcopy(
                self.men_candidate_manager.get_candidates_list())
            women_candidates_list = copy.deepcopy(
                self.women_candidate_manager.get_candidates_list())

            self.men_candidate_manager.match_candidates(women_candidates_list)
            self.women_candidate_manager.match_candidates(men_candidates_list)

            men_candidates_list = copy.deepcopy(
                self.men_candidate_manager.get_candidates_list())
            women_candidates_list = copy.deepcopy(
                self.women_candidate_manager.get_candidates_list())

            men_married_list = self.men_candidate_manager.judge_marriage(
                women_candidates_list)
            women_married_list = self.women_candidate_manager.judge_marriage(
                men_candidates_list)

            loop_num += 1

            total_married_pairs_number += len(men_married_list)

            if (self.men_candidate_manager.check_candidate_konkatsu_all_stopped() == True) and \
               (self.women_candidate_manager.check_candidate_konkatsu_all_stopped() == True):
                loop_end_flag = True

        return loop_num, total_married_pairs_number
