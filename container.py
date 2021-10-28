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
        sorted_list = self.sort()
        print("\n")
        for element in sorted_list:
            element.print()
            print("\n")
        pass

    def write(self, stream):
        stream.write("Container is store {} languages:\n".format(len(self.store)))
        for shape in self.store:
            shape.write(stream)
            stream.write("\n")

        sorted_list = self.sort()
        stream.write("\n")
        for element in sorted_list:
            element.write(stream)
            stream.write("\n")
        pass

    def sort(self):
        i = 0
        for first_element in self.store:
            if i != len(self.store):
                min_index = i
                j = i
                for second_element in self.store:
                    if j != len(self.store):
                        if first_element.quotient() < second_element.quotient():
                            min_index = j
                    j += 1
                tmp = self.store[i]
                self.store[i] = self.store[j]
                self.store[j] = tmp
                i += 1
        return self.store
