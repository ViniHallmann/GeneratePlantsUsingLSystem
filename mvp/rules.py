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
        {"rule": "F[+X][-X]FX",       "prob": 0.4},
        {"rule": "F[+X][-X]A",        "prob": 0.1},  # Adiciona frutas A
        {"rule": "F[+X][-X]B",        "prob": 0.1},  # Adiciona frutas B
        {"rule": "F[+X]F[-X]",        "prob": 0.2},  # Ramificação simples
        {"rule": "F[-X]F[+X]",        "prob": 0.1},  # Crescimento moderado
        {"rule": "F[+X][-X]",         "prob": 0.1},  # Crescimento básico
    ],
    "F": [
        {"rule": "FF",                "prob": 0.4},  # Tronco principal cresce
        {"rule": "F",                 "prob": 0.3},  # Sem multiplicação excessiva
        {"rule": "F[+F][-F]",         "prob": 0.3},  # Pequenas ramificações
    ]
}
