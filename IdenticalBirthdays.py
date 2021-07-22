import random
from array import *


class ProbabilityIdenticalBirthdays:
    MAX_PEOPLE = 100
    empirical_probability = array('d', [])
    theoretical_probability = array('d', [])
    isledovanie_teoretical = array('d', [])
    isledovanie_empirical = array('d', [])

    def __init__(self):
        self.experience()
        self.theoretical()
        #self.isledovanie_teoretical_inite()

    def isledovanie_teoretical_inite(self):
        i = 0
        while i < 1000:
            self.isledovanie_teoretical.extend([self.theoretical_probability[23]])
            self.isledovanie_empirical.extend([self.fixed_empirical(i)])
            i += 1

    def fixed_empirical(self, NUMBER_ATTEMPTS):
        if NUMBER_ATTEMPTS == 0:
            return 0

        people = 23
        attempt = 0
        identical_birthdays_count = 0
        while attempt < NUMBER_ATTEMPTS:
            birthday_recognition = 0
            stop = False
            birthdays_of_people = array('i', [])
            while birthday_recognition < people:
                this_birthday = random.randint(0, 365)
                for birthday in birthdays_of_people:
                    if birthday == this_birthday:
                        identical_birthdays_count += 1
                        stop = True
                        break
                if stop:
                    break
                birthdays_of_people.extend([this_birthday])
                birthday_recognition += 1
            attempt += 1
        probability = identical_birthdays_count / NUMBER_ATTEMPTS
        return probability


    def experience(self):
        NUMBER_ATTEMPTS = 1000
        people = 0
        while people < self.MAX_PEOPLE:
            attempt = 0
            identical_birthdays_count = 0
            while attempt < NUMBER_ATTEMPTS:
                birthday_recognition = 0
                stop = False
                birthdays_of_people = array('i', [])
                while birthday_recognition < people:
                    this_birthday = random.randint(0, 365)
                    for birthday in birthdays_of_people:
                        if birthday == this_birthday:
                            identical_birthdays_count += 1
                            stop = True
                            break
                    if stop:
                        break
                    birthdays_of_people.extend([this_birthday])
                    birthday_recognition += 1
                attempt += 1
            probability = identical_birthdays_count / NUMBER_ATTEMPTS
            self.empirical_probability.extend([probability])
            people += 1

    def theoretical(self):
        people = 0
        while people < self.MAX_PEOPLE:
            numerator = 1
            numerator_count = 0
            while numerator_count < people:
                numerator *= 365 - numerator_count
                numerator_count += 1

            denominator = 1
            denominator_count = 0
            while denominator_count < people:
                denominator *= 365
                denominator_count += 1

            probability = 1 - (numerator / denominator)
            self.theoretical_probability.extend([probability])
            people += 1

    def getEmpiricalProbability(self):
        return self.empirical_probability

    def getTheoreticalProbability(self):
        return self.theoretical_probability

    def getMaxPeople(self):
        return self.MAX_PEOPLE

    def getIsledovanieTeoretival(self):
        return self.isledovanie_teoretical

    def getIsledovanieEmpirical(self):
        return self.isledovanie_empirical