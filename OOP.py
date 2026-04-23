class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]
        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"

    def find(self, find):
        misto = []
        for id, cislo in enumerate(self.scores):
            if cislo == find:
                misto.append(id)
        return misto


    def get_sorted(self):
        novy_seznam = self.scores.copy()
        zmena = True
        while zmena:
            zmena = False

            for i in range(len(novy_seznam) - 1):
                if novy_seznam[i + 1] < novy_seznam[i]:
                    novy_seznam[i + 1], novy_seznam[i] = novy_seznam[i], novy_seznam[i + 1]
                    zmena = True
        return novy_seznam

if __name__ == '__main__':


    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())          # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)
    print(results.get_grade(3))# [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.find(100))
    print(results.get_sorted())


