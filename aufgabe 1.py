text = 'Betty Botter Bought Some Butter But the Butter is Bitter, So She Better Bought Some Better Butter.'


def lz77(text):
    """

    :param text:
    :type text: str
    :return ergebnis:
    """
    counter = 0  # Stelle an der der String geprüft wird
    ergebnis = []  # hier werden die Tripel eingefügt

    while counter < len(text):
        # tue folgendes solange wir uns im Text befinden
        backwardsWindow = text[:counter]  # Das Fenster wo wir die wiederholungen suchen (der gesamte string vorne dran)

        lookahead = text[counter:]  # Das lookahead Fenster (potenziell der ganze String))

        if lookahead[0] not in backwardsWindow:
            # Wenn der erste Buchstabe i, lookahead Fenster nicht im backwards Fenster vorhanden ist, erstelle
            # das Tripel für einzelne Buchstaben/Zeichen
            tripel = (0,0,lookahead[0])
            ergebnis.append(tripel)
            # und erhöhe den counter um 1 damit der nächste Buchstabe abgearbeitet werden kann
            counter += 1

        else:
            #Erstelle einen Prüfstring der dafür verwendet wird abgeglichen zu werden im backwards Fenster
            prüfstring = lookahead[0]

            # iteriere durch das lookahead fenster solange, bis der prüfstring nicht mehr im backwards fenster
            # auffindbar ist
            for char in lookahead[1:]:
                # Füge dem Prüfstring den jetzigen Charakter hinzu
                prüfstring += char

                if prüfstring not in backwardsWindow:
                    # Wenn prüfstring sich nicht mehr im backwards Fenster befindet, dann breche die Schleife ab
                    # und fülle das Tripel mit den jeweiligen Werten

                    # Platzhalter ist der letzte String der noch ins backwardsfenster passte
                    platzhalter = prüfstring[:-1]

                    # hier finden wir denjenige Index, der als letztes mit dem Prüfstring im backwards fenster matcht
                    index = (backwardsWindow).rfind(platzhalter)
                    index_differenz = len(backwardsWindow) - index

                    # befülle den string mit den jeweiligen werten
                    tripel = (-index_differenz, len(prüfstring)-1, prüfstring[-1])
                    ergebnis.append(tripel)

                    # passe den counter an damit die nächste iteration an der richtigen stelle beginnt
                    counter += len(prüfstring)
                    print(counter)

                    # beende die for-Schleife, sodass die nächste while-iteration beginnen kann
                    break
                else:
                    continue

    return ergebnis




def decrypt_lz77(cipher):

    # in diesem String bauen wir unseren String wieder auf
    string = ''

    # tue das für jedes Tupel
    for tupel in cipher:

        back = tupel[0]  # wie viele Schritte man zurückgehen muss
        len = tupel[1]  # wie lange das Fragment ist, welches man kopieren muss

        if tupel[0] == 0:
            # Wenn ein einzelnes Zeichen nicht vorhanden ist füge es einfach an
            string += tupel[2]

        else:
            # Wenn das zu ergänmzende fragment 2 lang ist, tue dies
            if tupel[1] == 1:
                fragment = string[back] + tupel[2]

                string += fragment
            # Wenn es länger als 2 ist tue das
            else:
                wort = ''  # Fragment wird stück für stück aufgebaut
                for i in range(len):
                    wort += string[back + i]

                wort += tupel[2]  # Fragment wird um das neue Zeichen ergänzt
                string += wort  # Füge fertiges wort hinzu

    return string

hi = lz77(text)
for i in hi:
    print(i)

hi2 = decrypt_lz77(hi)
print(hi2)

gedicht = ''' gedicht = 
In einem Wald, so tief und grün,
Wo Sonnenstrahlen tanzen, leicht und kühn.
Die Blumen wiegen sich im leisen Wind,
Ein Ort, wo die Seele Ruhe findet.'''

haha = lz77(gedicht)

for i in haha:
    print(i)

hehe = decrypt_lz77(haha)

print(hehe)