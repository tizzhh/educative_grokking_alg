def sort_colors(colors: list[int]) -> list[int]:
    red, white, blue = 0, 0, len(colors) - 1

    while white <= blue:
        if colors[white] == 0:
            if colors[red] != 0:
                colors[white], colors[red] = colors[red], colors[white]
            white += 1
            red += 1
        elif colors[white] == 1:
            white += 1
        else:
            if colors[blue] != 2:
                colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1

    return colors


print(sort_colors([0, 1, 0]))
