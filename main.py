import template as tmp
from city_grid import CityGrid


def app():
    # task1
    print(tmp.TASK1)
    print(tmp.UNDERLINE)
    n = int(input(tmp.INPUT3))
    m = int(input(tmp.INPUT4))
    p = float(input(tmp.INPUT5))

    city = CityGrid(n, m, p)
    city.visualize_grid()
    print(tmp.UNDERLINE)

    # task2
    print(tmp.TASK2)
    print(tmp.UNDERLINE)
    print(tmp.INF)
    city2 = CityGrid(10, 10, 0.3)
    city2.place_tower(4, 5, 2)
    city2.visualize_grid()
    print(tmp.UNDERLINE)

    # task3
    print(tmp.TASK3)
    print(tmp.UNDERLINE)

    msg = 1
    # Рендерим матрицу до тех пор пока не перекроем все кварталы
    while msg != 0:

        # Подсчитываем сколько осталось неперекрытых кварталов
        msg = city.count_zeros()

        list_n = city.count_neighbors()
        first_n = list_n[0]
        # Проверяем остались ли неперекрытые кварталы в радиусе башен
        count_n = first_n[2]

        if count_n != 0:
            city.render_matrix()
        elif msg == 0:
            print(tmp.INF1)
            city.render_matrix()
            city.visualize_grid()
        else:
            city.render_matrix()
            city.visualize_grid()
            print(tmp.INF2)
            break
    print(tmp.UNDERLINE)

    # task4
    print(tmp.TASK4)
    print(tmp.UNDERLINE)

    start = tuple(int(item) for item in input(tmp.INPUT1).split())
    end = tuple(int(item) for item in input(tmp.INPUT2).split())

    path = city.find_path(start, end)

    if path:
        path.insert(0, start)
        print("Path:")
        for point in path:
            print(point)
    else:
        print("The path cannot be built...")
    print(tmp.UNDERLINE)

    # task5
    print(tmp.TASK5)
    print(tmp.UNDERLINE)
    print("Plotting...")
    city.visualize_city(tower_positions=[start, end], path=path)
    print(tmp.UNDERLINE)


if __name__ == "__main__":
    try:
        app()
    except Exception as error:
        print(f"Error: {error}")
