LuxeBroodjes = ["Krentenbol", "Eierkoek", "Croissantje", "Kadetje"]
verpakkingen = ["Per 1", "Per 4", "Per 8"]
GecombineerdeVerpakking = []
for Luxebroodje in LuxeBroodjes:
    for verpakking in verpakkingen:
        EindProduct = Luxebroodje + " " + verpakking
        GecombineerdeVerpakking.append(EindProduct)
print(GecombineerdeVerpakking)
