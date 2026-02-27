import numpy as np

def calcular_medias(notas):
    media = notas.mean(axis=1)
    return media


def identificar_aprovados(medias):
    return medias >= 7

def normalizar_notas(notas):
    media = np.mean(notas, axis=0)
    desvioPadrao = np.std(notas, axis=0)
    return (notas - media) / desvioPadrao

def main():
    notas = np.array([
        [7.0, 8.5, 9.0, 6.5],
        [5.0, 4.5, 6.0, 5.5],
        [9.5, 9.0, 8.5, 9.0],
        [6.0, 7.0, 5.5, 6.5],
        [8.0, 7.5, 8.5, 8.0]
    ])

    medias = calcular_medias(notas)
    print("Médias dos alunos:")
    print(medias)

    aprovados = identificar_aprovados(medias)
    print("\nAlunos aprovados (True = aprovado):")
    print(aprovados)

    notas_normalizadas = normalizar_notas(notas)
    print("\nNotas normalizadas:")
    print(notas_normalizadas)

    notas_norm = normalizar_notas(notas)
    print("\n")
    print(np.mean(notas_norm, axis=0))
    print(np.std(notas_norm, axis=0))


if __name__ == "__main__":
    main()
