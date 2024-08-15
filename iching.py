import random
import pandas as pd

print('Welcome to virtual i-ching')

J1 = []
J2 = []
J3 = []
J4 = []
J5 = []
J6 = []
soma = []

def jogada(x):
    moeda1 = random.randint(2,3)
    moeda2 = random.randint(2,3)
    moeda3 = random.randint(2,3)
    x.append(moeda1)
    x.append(moeda2)
    x.append(moeda3)

input("Think of a question, and then press the Enter key: ")
jogada(J1)
print(J1)
input("Press the Enter key to continue: ")
jogada(J2)
print(J2)
input("Press the Enter key to continue: ")
jogada(J3)
print(J3)
input("Press the Enter key to continue: ")
jogada(J4)
print(J4)
input("Press the Enter key to continue: ")
jogada(J5)
print(J5)
input("Press the Enter key to continue: ")
jogada(J6)
print(J6)
input("Press the Enter key see the result: ")

jogadas = (J6, J5, J4, J3, J2, J1)

moedas = ['M1', 'M2', 'M3']
linhas = ['L1', 'L2', 'L3','L4', 'L5', 'L6']

resultado = pd.DataFrame(jogadas, columns=moedas, index=linhas)

resultado['soma'] = {'L1': resultado.loc['L1'].sum(), 'L2': resultado.loc['L2'].sum(), 'L3': resultado.loc['L3'].sum(), 'L4': resultado.loc['L4'].sum(), 'L5': resultado.loc['L5'].sum(), 'L6': resultado.loc['L6'].sum()}

#print(resultado)


def hexagrama(x):
    if resultado.iloc[x, 3] == 6:
        soma.append('__ X __')
    elif resultado.iloc[x, 3] == 7:
        soma.append('_______')
    elif resultado.iloc[x, 3] == 8:
        soma.append('__   __')
    elif resultado.iloc[x, 3] == 9:
        soma.append('___O___')
    else:
        print('a soma é inválida')

hexagrama(5)
hexagrama(4)
hexagrama(3)
hexagrama(2)
hexagrama(1)
hexagrama(0)

hexagrama_df = pd.DataFrame(soma)
print(hexagrama_df)

linhas_hex = list(resultado.loc[:,'soma'])
#print(linhas_hex)

hex = []

for num in linhas_hex:
    if (num == 6) or (num == 8):
        hex.append(False)             
    elif (num == 7) or (num) == 9:
        hex.append(True)
    else: 
        pass

hexagramas = {
    '1. The Creative (乾)': [True, True, True, True, True, True],  # Hexagram 1
    '2. The Receptive (坤)': [False, False, False, False, False, False],  # Hexagram 2
    '3. Difficulty at the Beginning (屯)': [True, False, False, False, True, False],  # Hexagram 3
    '4. Youthful Folly (蒙)': [False, True, False, False, False, True],  # Hexagram 4
    '5. Waiting (需)': [True, True, True, False, True, False],  # Hexagram 5
    '6. Conflict (訟)': [False, True, False, True, True, True],  # Hexagram 6
    '7. The Army (師)': [False, True, False, False, False, False],  # Hexagram 7
    '8. Holding Together (比)': [False, False, False, False, True, False],  # Hexagram 8
    '9. Small Taming (小畜)': [True, True, True, False, True, True],  # Hexagram 9
    '10. Treading (履)': [True, True, False, True, True, True],  # Hexagram 10
    '11. Peace (泰)': [True, True, True, False, False, False],  # Hexagram 11
    '12. Standstill (否)': [False, False, False, True, True, True],  # Hexagram 12
    '13. Fellowship with Men (同人)': [True, False, True, True, True, True],  # Hexagram 13
    '14. Great Possession (大有)': [True, True, True, True, False, True],  # Hexagram 14
    '15. Modesty (謙)': [False, False, True, False, False, False],  # Hexagram 15
    '16. Enthusiasm (豫)': [False, False, False, True, False, False],  # Hexagram 16
    '17. Following (隨)': [True, False, False, True, True, False],  # Hexagram 17
    '18. Work on the Decayed (蠱)': [False, True, True, False, False, True],  # Hexagram 18
    '19. Approach (臨)': [True, True, False, False, False, False],  # Hexagram 19
    '20. Contemplation (觀)': [False, False, False, False, True, True],  # Hexagram 20
    '21. Biting Through (噬嗑)': [True, False, False, True, False, True],  # Hexagram 21
    '22. Grace (賁)': [True, False, True, False, False, True],  # Hexagram 22
    '23. Splitting Apart (剝)': [False, False, False, False, False, True],  # Hexagram 23
    '24. Return (復)': [True, False, False, False, False, False],  # Hexagram 24
    '25. Innocence (無妄)': [True, False, False, True, True, True],  # Hexagram 25
    '26. Great Taming (大畜)': [True, True, True, False, False, True],  # Hexagram 26
    '27. Mouth Corners (頤)': [True, False, False, False, False, True],  # Hexagram 27
    '28. Great Preponderance (大過)': [False, True, True, True, True, False],  # Hexagram 28
    '29. The Abysmal (坎)': [False, True, False, False, True, False],  # Hexagram 29
    '30. The Clinging (離)': [True, False, True, True, False, True], # Hexagram 30
    '31. Influence (咸)': [False, False, True, True, True, False],  # Hexagram 31
    '32. Duration (恒)': [False, True, True, True, False, False],  # Hexagram 32
    '33. Retreat (遯)': [False, False, True, True, True, True],  # Hexagram 33
    '34. Great Power (大壯)': [True, True, True, True, False, False],  # Hexagram 34
    '35. Progress (晉)': [False, False, False, True, False, True],  # Hexagram 35
    '36. Darkening of the Light (明夷)': [True, False, True, False, False, False],  # Hexagram 36
    '37. The Family (家人)': [True, False, True, False, True, True],  # Hexagram 37
    '38. Opposition (睽)': [True, True, False, True, False, True],  # Hexagram 38
    '39. Obstruction (蹇)': [False, False, True, False, True, False],  # Hexagram 39
    '40. Deliverance (解)': [False, True, False, True, False, False],  # Hexagram 40
    '41. Decrease (損)': [True, True, False, False, False, True],  # Hexagram 41
    '42. Increase (益)': [True, False, False, False, True, True],  # Hexagram 42
    '43. Breakthrough (夬)': [True, True, True, True, True, False],  # Hexagram 43
    '44. Coming to Meet (姤)': [False, True, True, True, True, True],  # Hexagram 44
    '45. Gathering Together (萃)': [False, False, False, True, True, False],  # Hexagram 45
    '46. Pushing Upward (升)': [False, True, True, False, False, False],  # Hexagram 46
    '47. Oppression (困)': [False, True, False, True, True, False],  # Hexagram 47
    '48. The Well (井)': [False, True, True, False, True, False],  # Hexagram 48
    '49. Revolution (革)': [True, False, True, True, True, False],  # Hexagram 49
    '50. The Cauldron (鼎)': [False, True, True, True, False, True],  # Hexagram 50
    '51. The Arousing (震)': [True, False, False, True, False, False],  # Hexagram 51
    '52. The Keeping Still (艮)': [False, False, True, False, False, True],  # Hexagram 52
    '53. Development (漸)': [False, False, True, False, True, True],  # Hexagram 53
    '54. The Marrying Maiden (歸妹)': [True, True, False, True, False, False],  # Hexagram 54
    '55. Abundance (豐)': [True, False, True, True, False, False],  # Hexagram 55
    '56. The Wanderer (旅)': [False, False, True, True, False, True],  # Hexagram 56
    '57. The Gentle (巽)': [False, True, True, False, True, True],  # Hexagram 57
    '58. The Joyous (兌)': [True, True, False, True, True, False],  # Hexagram 58
    '59. Dispersion (渙)': [False, True, True, False, False, True],  # Hexagram 59
    '60. Limitation (節)': [False, True, False, False, True, True],  # Hexagram 60
    '61. Inner Truth (中孚)': [True, True, False, False, True, True],  # Hexagram 61
    '62. Small Preponderance (小過)': [False, False, True, True, False, False],  # Hexagram 62
    '63. After Completion (既濟)': [True, False, True, False, True, False],  # Hexagram 63
    '64. Before Completion (未濟)': [False, True, False, True, False, True]  # Hexagram 64
}

for key, val in hexagramas.items():
    if val == hex:
        print(key)
    else:
        pass

for line in linhas_hex:
    if line == 6:
        print('(Special Yin)')
    elif line == 9:
        print('(Special Yang)')
    else:
        pass

print('You should now research for the interpretation of the hexagram.')
print('https://iching.com.br/o-i-ching/os-64-hexagramas-do-iching/')
print('Thank you for consulting virtual i-ching. Good Luck!')

