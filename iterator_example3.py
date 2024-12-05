def rotace(image):
    return rotated_image

class ImageIterator:
    def __init__(self, list_snimku, kolik_snimku_budeme_potrebovat):
        self.list_snimku = list_snimku
        self.kolik_snimku_budeme_potrebovat = kolik_snimku_budeme_potrebovat
        self.kolik_snimku_jsme_vratili = 0

    def __iter__(self):
        return self

    def __next__(self):
        import random
        self.kolik_snimku_jsme_vratili += 1
        if self.kolik_snimku_jsme_vratili > self.kolik_snimku_budeme_potrebovat:
            raise StopIteration
        random_index = random.randint(0, len(self.list_snimku))
        rotovany_snimek = rotace(self.list_snimku[random_index])
        return rotovany_snimek

for snimek in ImageIterator(snimky):
    funkce_treninku_neuronove_site(snimek)