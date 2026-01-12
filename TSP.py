import random
import math

NUM_CITIES = 20
MAP_SIZE = 100

POP_SIZE = 250
GENERATIONS = 1000
MUTATION_RATE = 0.12
TOURNAMENT_SIZE = 5
ELITISM = 2

cities = [
    (random.uniform(0, MAP_SIZE), random.uniform(0, MAP_SIZE))
    for _ in range(NUM_CITIES)
]



def euclidean(a, b):
    """
    Calculeaza distanta euclidiana dintre doua orase.
    a si b sunt tuple de forma (x, y)
    """
    return math.hypot(a[0] - b[0], a[1] - b[1])


def total_distance(route):
    """
    Calculeaza distanta totala a unei rute TSP.
    Ruta este ciclica: ultimul oras se leaga cu primul.
    route = lista de indici ai oraselor (permutare)
    """
    dist = 0.0
    n = len(route)

    for i in range(n):
        city_a = cities[route[i]]
        city_b = cities[route[(i + 1) % n]]
        dist += euclidean(city_a, city_b)

    return dist


def fitness(route):
    """
    Functia de fitness.
    Dorim sa MINIMIZAM distanta, dar GA maximizeaza fitness-ul,
    asa ca folosim inversul distantei.
    """
    return 1.0 / total_distance(route)



def create_individual(n):
    """
    Creeaza un individ (o solutie).
    Practic o permutare aleatoare a oraselor.
    """
    individual = list(range(n))
    random.shuffle(individual)
    return individual


def create_population(pop_size, n):
    """
    Creeaza populatia initiala
    = lista de indivizi aleatori.
    """
    return [create_individual(n) for _ in range(pop_size)]

def tournament_selection(population, k=TOURNAMENT_SIZE):
    """
    Selectie prin turneu:
    - alegem k indivizi aleator
    - il returnam pe cel cu fitness maxim
    """
    contestants = random.sample(population, k)
    return max(contestants, key=fitness)


def order_crossover(parent1, parent2):
    """
    Crossover special pentru permutari (TSP).
    1. Alegem un segment aleator din parent1
    2. Il copiem in copil
    3. Completam restul oraselor in ordinea din parent2
    """
    n = len(parent1)
    a, b = sorted(random.sample(range(n), 2))
    child = [None] * n

    # Copiem segmentul din primul parinte
    child[a:b] = parent1[a:b]

    # Completam genele lipsa din al doilea parinte
    idx = b
    for city in parent2:
        if city not in child:
            if idx >= n:
                idx = 0
            child[idx] = city
            idx += 1

    return child



def swap_mutation(route, rate=MUTATION_RATE):
    """
    Mutatie simpla:
    - cu o anumita probabilitate
    - interschimba doua orase din ruta
    """
    if random.random() < rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]



def genetic_algorithm():
    """
    Implementarea completa a algoritmului genetic:
    - initializare
    - selectie
    - crossover
    - mutatie
    - elitism
    """
    population = create_population(POP_SIZE, NUM_CITIES)


    best = min(population, key=total_distance)

    for gen in range(1, GENERATIONS + 1):

        new_population = []


        population_sorted = sorted(population, key=total_distance)


        new_population.extend(population_sorted[:ELITISM])


        while len(new_population) < POP_SIZE:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)

            child = order_crossover(parent1, parent2)
            swap_mutation(child)

            new_population.append(child)

        population = new_population


        current_best = min(population, key=total_distance)
        if total_distance(current_best) < total_distance(best):
            best = current_best


        if gen % 50 == 0 or gen == 1:
            print(f"Generatia {gen:4d} | distanta minima = {total_distance(best):.3f}")

    return best


if __name__ == "__main__":

    print("Orase generate random:")
    for i, c in enumerate(cities):
        print(f"{i}: {c}")

    best_route = genetic_algorithm()

    print("\n=== REZULTAT FINAL ===")
    print("Ruta optima (ordine orase):", best_route)
    print("Distanta totala:", total_distance(best_route))

    print("\nRuta ca puncte (x, y):")
    for idx in best_route:
        print(f"{idx}: {cities[idx]}")
