from typing import List


def find_heaviest_containers(container_data) -> List:
    heavier_containers = set()
    lighter_containers = set()

    for line in container_data:
        heavier_container, lighter_container = line.split()

        heavier_containers.add(heavier_container)
        lighter_containers.add(lighter_container)

    # Get all containers that are in the heavier_containers set but not in the lighter_containers set
    heaviest_containers = list(heavier_containers.difference(lighter_containers))

    return heaviest_containers


def main():
    with open("container3.txt") as file:
        data = file.readlines()

    heaviest_containers = find_heaviest_containers(data)

    if len(heaviest_containers) == 1:
        print(f"Der schwerste Container ist: {heaviest_containers[0]}")
    elif len(heaviest_containers) == 0:
        print("Der schwerste Container lässt sich nicht bestimmen.")
    else:
        print("Der schwerste Container lässt sich nicht eindeutig bestimmen. "
              "Alle möglichen schwersten Container sind: "
              f"{', '.join(heaviest_containers[:-1])} und {heaviest_containers[-1]}.")


if __name__ == "__main__":
    main()
