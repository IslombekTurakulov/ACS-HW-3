# ----------------------------------------------
import languages
import utilsIn


class Container:
    def __init__(self):
        self.store = []

    def staticIn(self, size):
        i = 0
        while i < size:
            self.store.append(utilsIn.inRnd())
            i += 1

    def print(self):
        print("Container is store", len(self.store), "languages:")
        for language in self.store:
            language.print()
        self.sort()
        print("\nSorted container:")
        for element in self.store:
            element.print()
        pass

    def write(self, stream):
        stream.write("Container is store {} languages:\n".format(len(self.store)))
        for shape in self.store:
            shape.write(stream)
            stream.write("\n")
        stream.write("\n")
        pass

    def sort(self):
        i = 0
        for first_element in self.store:
            min_index = i
            j = i
            for second_element in self.store:
                if j + 1 != len(self.store):
                    if round(first_element.quotient(), 2) < round(second_element.quotient(), 2):
                        min_index = j
                else:
                    continue
                j += 1
            tmp = self.store[i]
            self.store[i] = self.store[j]
            self.store[j] = tmp
            i += 1
