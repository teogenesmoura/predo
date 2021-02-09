import sys
MEDIA_MINIMA = 5
def get_mencao(media):
    if(media > 0 and media <= 2.9):
        return "II"
    elif (media >= 3 and media <= 4.9):
        return "MI"
    elif (media >= 5 and media <= 6.9):
        return "MM"
    elif (media >= 7 and media <= 8.9):
        return "MS"
    elif (media >= 9):
        return "SS"
    return "SR"

def calc_media(exercicios, trabalhos):
    return (0.4 * exercicios + 0.6 * trabalhos)

def avaliacao(exercicios, trabalhos):
    exercicios = float(exercicios)
    trabalhos = float(trabalhos)
    if (exercicios < MEDIA_MINIMA):
        return (exercicios, get_mencao(exercicios))
    if (trabalhos < MEDIA_MINIMA):
        return (trabalhos, get_mencao(trabalhos))
    media_final = calc_media(exercicios, trabalhos)
    return (media_final, get_mencao(media_final))

print(avaliacao(sys.argv[1], sys.argv[2]))
