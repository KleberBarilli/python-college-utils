class Comprimir():
    def __init__(self):
        self.dict = {}
        self.dict_size = 256
        for i in range(255):
            self.dict[chr(i)] = i

    def comprime(self, palavra):
        w = ''
        result = []
        for c in palavra:
            wc = w + c

            if wc in self.dict:
                w = wc
            else:
                result.append((self.dict[w]))
                self.dict[wc] = self.dict_size
                self.dict_size += 1
                w = c
        if w:
            result.append(self.dict[w])


        print(result)

        print(self.dict)
c = Comprimir()
c.comprime('A_ASA_DA_CASA')
c.comprime('AUSTRALIA')



