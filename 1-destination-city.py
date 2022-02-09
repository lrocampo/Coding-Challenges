# Our weird solution
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a = paths[0][1] # a = "C"
        for i in range(len(paths)-1): # to-do: cuantas veces tiene que recorrer la lista hasta que identifique el destino final
            for j in range(len(paths)):
                try:
                    b = paths[j].index(a)
                    if b == 0:
                        a = paths[j][1]
                except:
                    continue
        return a

# Solution from Keith Galli

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_count = {}
        for path in paths:
            city_a, city_b = path
            outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
            outgoing_count[city_b] = outgoing_count.get(city_b, 0)

            for city in outgoing_count:
                if outgoing_count[city] == 0:
                    return city

