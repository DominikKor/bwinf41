def find_heaviest_container(container_data):
    heaviest_containers = []
    outruled_heaviest_containers = []

    for line in container_data:
        heavier_container, lighter_container = line.split()

        outruled_heaviest_containers.append(lighter_container)

        if heavier_container not in (heaviest_containers + outruled_heaviest_containers):
            heaviest_containers.append(heavier_container)

        if lighter_container in heaviest_containers:
            heaviest_containers.remove(lighter_container)

    if len(heaviest_containers) == 1:
        return heaviest_containers[0]
    else:
        return " ".join(heaviest_containers)


def main():
    with open("../Junior2/container2.txt") as file:
        data = file.readlines()

    heaviest_container = find_heaviest_container(data)

    print(heaviest_container)


if __name__ == "__main__":
    main()
