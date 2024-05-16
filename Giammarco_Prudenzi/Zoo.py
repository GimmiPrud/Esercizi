
# Giammarco Prudenzi 

# Progetto Zoo:
'''
1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.
2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).
3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.
4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.
Funzionalità:
1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.
2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.
3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.
4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.
5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 
'''
# Svolgimento Progetto Zoo:
    
class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str, health: float):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / self.age), 3)


class Fence:
    def __init__(self, area: float, temperature: float, habitat: str):
        self.animals = []
        self.area = area
        self.temperature = temperature
        self.habitat = habitat


class ZooKeeper:
    def __init__(self, name: str, surname: str, id: int):
        self.name = name
        self.surname = surname
        self.id = id


    def feed(self, animal: Animal, fence):
        if fence.area > animal.height * animal.width:
            animal.health *= 1.01
            animal.height *= 1.02
            animal.width *= 1.02
        
        return round(animal.health, 3), round(animal.height, 3), round(animal.width ,3)


    def clean(self, fence: Fence) -> float:
        for a in fence.animals:
            occupied_area = a.height * a.width
            remaning = fence.area - occupied_area

        if fence.area <= 0:
            return round(occupied_area,3)
        
        else:
            return round(occupied_area/remaning,3)
        

class Zoo:
    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]):
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def add_animal(self, animal: Animal, fence: Fence):
        if animal.preferred_habitat != fence.habitat and fence.area < animal.height * animal.width:
            pass

        else:
            fence.animals.append(animal)
            fence.area -= (animal.height * animal.width)


    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += (animal.height * animal.width)


    def describe_zoo(self):
        for zookeeper in self.zoo_keepers:
            pass
        for fence in self.fences:
            pass
            for animal in fence.animals:
                pass
        
        
        


a1 = Animal(name="lupo",species="mammifero",age=3,height=12,width=3,preferred_habitat="continent")
a2 = Animal(name="scimmia",species="mammifero",age=10,height=15,width=2,preferred_habitat="continent")
f1 = Fence(area=23,temperature=15,habitat="continent")
f2 = Fence(area=12,temperature=3,habitat="tropical")
z1 = ZooKeeper(name="Lapo",surname="Elkan",id=121)
z2 = ZooKeeper(name="alessio",surname="sisti",id=344)
zoo = Zoo(zoo_keepers=[z1,z2],fences=[f1,f2])
zoo.describe_zoo()


