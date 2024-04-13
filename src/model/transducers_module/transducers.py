from pyformlang.fst import FST

email = FST()

for c in range(ord("a"), ord("z") + 1):
    email.add_transition("s0", chr(c), "s0", [chr(c)])

for c in range(ord("A"), ord("Z") + 1):
    email.add_transition("s0", chr(c), "s0", [chr(c)])

for c in range(10):
    email.add_transition("s0", f"{c}", "s0", [f"{c}"])

for c in ["@",".","'","\"","-",",",";",":","(",")","[","]","{","}","<",">","¡","¿","ñ","Ñ","á","é","í","ó","ú","Á","É","Í","Ó","Ú","\\","/","&","%","$","#","*","+","^","`","~","|","!","?"]:
    email.add_transition("s0", c, "s0", [c])

email.add_transitions(
    [
        ("s0", " ", "s0", [" "]),
        ("s0", "_", "s0", [" "]),
        ("s0", "\n", "s0", ["\n"]),
        ("s0", ":", "s0", [":"]),
        ("s0", "?", "s0", ["?"]),
        ("s0", "!", "s0", ["! "]),
        ("s0", "=", "s1", [""]),
        ("s1", "\n", "s0", [""]),  # Salto de linea removible
        ("s1", "0", "s2", [""]),
        ("s1", "C", "s2", [""]),
        ("s2", "3", "s3", [""]),
        ("s2", "A", "s0", [""]),
        ("s3", "=", "s4", [""]),
        ("s4", "\n", "s3", [""]),  # Salto de linea removible
        # =
        ("s1", "3", "s13", [""]),
        ("s1", "2", "s14", [""]),
        ("s14", "1", "s0", ["!"]),
        ("s13", "D", "s0", ["="]),
        ("s13", "A", "s16", [""]),
        ("s16", "_", "s0", ["_"]),
        ("s2", "2", "s9", [""]),
        ("s9", "=", "s10", [""]),
        ("s10", "\n", "s9", [""]),  # Salto de linea removible
        ("s10", "A", "s11", [""]),
        ("s10", "B", "s12", [""]),
        # ¡
        ("s11", "1", "s0", ["¡"]),
        # ¿
        ("s12", "F", "s0", ["¿"]),
        ("s4", "A", "s5", [""]),
        ("s4", "B", "s6", [""]),
        ("s4", "8", "s7", [""]),
        ("s4", "9", "s8", [""]),
        # á
        ("s5", "1", "s0", ["á"]),
        # é
        ("s5", "9", "s0", ["é"]),
        # í
        ("s5", "D", "s0", ["í"]),
        # ó
        ("s6", "3", "s0", ["ó"]),
        # ú
        ("s6", "A", "s0", ["ú"]),
        # Á
        ("s7", "1", "s0", ["Á"]),
        # É
        ("s7", "9", "s0", ["É"]),
        # Í
        ("s7", "D", "s0", ["Í"]),
        # Ó
        ("s8", "3", "s0", ["Ó"]),
        # Ú
        ("s8", "A", "s0", ["Ú"]),
        # ñ
        ("s6", "1", "s0", ["ñ"]),
        # Ñ
        ("s8", "1", "s0", ["Ñ"]),
        # ¿
        ("s4", "C", "s9", ["¿"]),
    ]
)

email.add_start_state("s0")
email.add_final_state("s0")


def translate(value):
    translated = list(map(lambda x: "".join(x), list(email.translate(value))))
    if len(translated) > 0:
        return translated[0]
    return value