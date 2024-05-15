# Giammarco Prudenzi 
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
    def __init__(self, animals: list[Animal], area: float, temperature: float, habitat: str):
        self.animals = animals
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        
class ZooKeeper:
    def __init__(self, name: str, surname: str, id: int):
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal: Animal, fence: Fence):
        if animal.preferred_habitat != fence.habitat and animal.height * animal.width > fence.area:
            pass

        else:
            fence.animals.append(animal)

            fence.area = (animal.height * animal.width) - fence.area

    def remove_animal(self, animal: Animal, fence: Fence):
        fence.animals.remove(animal)
        fence.area = (animal.height * animal.width) + fence.area

    def feed(self, animal: Animal):
       # while >= animal.height * animal.width:
            animal.health *= 1.01
            animal.height *= 1.02
            animal.width *= 1.02
        
        #return animal.health, animal.height

    def clean(self, fence: Fence) -> float:
        if fence.area == 0:
            return "L'area è occupata"
        
        animals_area: float = 0
        animals_height: int = 0
        animals_width: int = 0

        for f in range(len(fence.animals)):
            animals_width += fence.animals[f]
            animals_height += fence.animals[f]
            animals_area = animals_height*animals_width

        if fence.area / animals_area <= 0:
            return "L'area è occupata"
        
        else:
            return fence.area / animals_area
        

class Zoo:
    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]):
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def describe_zoo(self):
        for i in self.fences:
            return f" Fences = {self.fences[i.animals[i]]}"
        
        return f"Zookeepers = {self.zoo_keepers}"
        

        
a1 = Animal(name="Sirio",species="Rinoceronte",age=10,height=1500,width=335,preferred_habitat="Savana",health=7)
a2 = Fence(animals=["Lillo"], area= 70, temperature= 25, habitat= "Savana")
a3 = ZooKeeper(name="Giancarlo",surname="Strizzi",id=123)

print(a3.feed(a1))
