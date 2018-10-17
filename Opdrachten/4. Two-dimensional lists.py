studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]


def gemiddelde_per_student(studentencijfers):
    return [sum(studentencijfers[0]) / len(studentencijfers[0]), sum(studentencijfers[1]) / len(studentencijfers[1])
        , sum(studentencijfers[2]) / len(studentencijfers[2]), sum(studentencijfers[3]) / len(studentencijfers[3])]



def gemiddelde_van_alle_studenten(studentencijfers):
    return sum(gemiddelde_per_student(studentencijfers)) / len(gemiddelde_per_student(studentencijfers))

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))