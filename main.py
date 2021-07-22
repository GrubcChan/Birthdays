from IdenticalBirthdays import ProbabilityIdenticalBirthdays
import matplotlib.pyplot as plt


def main():
    probability = ProbabilityIdenticalBirthdays()
    #fig = plt.figure()
    #fig.patch.set_facecolor('black')
    #fig.patch.set_alpha(0.5)
    #ax = fig.add_subplot(111)
    #ax.patch.set_facecolor('black')
    #ax.patch.set_alpha(0.9)
    #plt.title('Probability identical birthdays')
    #plt.xlabel('attempts')
    #plt.ylabel('P(23)')
    #plt.plot(list(range(0, 1000)), probability.getIsledovanieEmpirical(),
    #        label="Empirical probability", linewidth=2, color='#0B61A4')
    #plt.plot(list(range(0, 1000)), probability.getIsledovanieTeoretival(),
    #         label="Teoretical probability", linewidth=2,  color='#FF9200')
    #plt.legend()
    #plt.show()
    for x in probability.getTheoreticalProbability():
        print(x)
    print("__________________________________________________")
    for x in probability.getEmpiricalProbability():
        print(x)


if __name__ == '__main__':
    main()
