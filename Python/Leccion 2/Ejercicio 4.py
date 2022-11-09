edad = int(input('Diguite su edad: '))
nota = None
if 0 <= edad < 10:
    nota = 'La infancia es increible y bella'
elif 10 <= edad < 19:
    nota = 'Tiene muchos cambios, mucho que estudar'
elif 20 <= edad < 30:
    nota = 'Amor y comienza el trabajo'
else:
    nota = 'Edad no reconocida'
print(f'Su edad es : {edad}, {nota}')