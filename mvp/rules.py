"""AXIOM = "X"
RULES = {
    "X": [
        {"rule": "F[+X][-X]FX",   "prob": 0.5},
        {"rule": "F[-X]FX",       "prob": 0.05},
        {"rule": "F[+X]FX",       "prob": 0.05},
        {"rule": "F[++X][-X]FX",  "prob": 0.1},
        {"rule": "F[+X][--X]FX",  "prob": 0.1},
        {"rule": "F[+X][-X]FA",   "prob": 0.1},
        {"rule": "F[+X][-X]FB",   "prob": 0.1},
    ],
    "F": 
    [
        {"rule": "FF",  "prob": 0.5},
        {"rule": "F",    "prob": 0.5},
    ]
}"""

"""AXIOM = "X"
RULES = {
    "X": [
        {"rule": "F[+X][-X]",        "prob": 0.4},
        {"rule": "F[+X][X]F[-X]",    "prob": 0.2},
        {"rule": "F[+X]F[-X]FX",     "prob": 0.2},
        {"rule": "F[-X]F[++X]",      "prob": 0.1},
        {"rule": "F[+X]FX",          "prob": 0.1},
    ],
    "F": [
        {"rule": "FF",               "prob": 0.4},  # Crescimento contínuo
        {"rule": "F",                "prob": 0.4},  # Sem multiplicar tanto
        {"rule": "F[+F][-F]",        "prob": 0.2},  # Ramificações intermediárias
    ]
}"""

AXIOM = "X"
RULES = {
    "X": [
        {"rule": "(F[+X][-X]FX)",       "prob": 0.5},
        {"rule": "(F[-X]FX)",        "prob": 0.05},  # Adiciona frutas A
        {"rule": "(F[+X]FX)",        "prob": 0.05},  # Adiciona frutas B
        {"rule": "(F[++X][-X]FX)",        "prob": 0.1},  # Ramificação simples
        {"rule": "(F[+X][--X]FX)",        "prob": 0.1},  # Crescimento moderado
        {"rule": "(F[+X][-X]FXA)",         "prob": 0.1},  # Crescimento básico
        {"rule": "(F[+X][-X]FXB)",         "prob": 0.1},  # Cres
    ],
    "F": [
        {"rule": "F(F)",                "prob": 0.2},  # Multiplicação moderada
        {"rule": "F(FF)",               "prob": 0.4},  # Multiplicação contínua
        {"rule": "F",                   "prob": 0.4},  # Sem multiplicação
    ]
}
