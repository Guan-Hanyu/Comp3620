import csv
import random

def load_data(filename):
    age = []
    hg = []
    cls = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for i in reader:
            age.append(float(i[0]))
            hg.append(float(i[1]))
            cls.append(int(i[2]))

    return age, hg, cls



def perceptron(age, hg, cls):
    random.seed(0)

    w0 = random.uniform(-1, 1)
    w_age = random.uniform(-1, 1)
    w_hg = random.uniform(-1, 1)

    for n in range(999999999):
        errors = 0

        for i in range(len(cls)):
            y = w0 + w_age * age[i] + w_hg * hg[i]

            if y >= 0:
                prediction = 1
            else: 
                prediction = 0

            if prediction != cls[i]:

                if cls[i] == 1:
                    w0 += 1
                    w_age += age[i]
                    w_hg += hg[i]
                else:
                    w0 -= 1
                    w_age -= age[i]
                    w_hg -= hg[i]

                errors += 1

        if errors == 0:
            break

    return w0, w_age, w_hg