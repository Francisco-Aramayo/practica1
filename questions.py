import random
import sys
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

puntaje = 0.0
#Se seleccionan 3 preguntas aleatorias
questions_to_ask = random.sample(list(zip(questions,answers,correct_answers_index)), k=3)

# Se recorre la lista de preguntas seleccionadas
for question, answers, correct_index in questions_to_ask:
     # Se muestra la pregunta y las respuestas posibles
    print(question)
    
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    acierto = False
    for intento in range(2):
        user_answer = input("Respuesta: ") 
    
        # Se verifica si la respuesta es correcta
        if not user_answer.isdigit():
            print("La respuesta no es valida!")
            sys.exit(1)

        user_answer = int(user_answer) - 1

        if user_answer < 0 or user_answer >= len(answers):
                print("La respuesta no es valida!")
                sys.exit(1)
        elif user_answer == correct_index:
            print("¡Correcto!")
            puntaje += 1
            acierto = True
            break
        else:
            print("Incorrecto!")
            puntaje -= 0.5
    # Si el usuario no responde correctamente después de 2 intentos,
    # se muestra la respuesta correcta
    if not acierto:
        print("La respuesta correcta es:")
        print(answers[correct_index])
             
    # Se imprime un blanco al final de la pregunta
    print()

print('Puntaje final: ',puntaje)
