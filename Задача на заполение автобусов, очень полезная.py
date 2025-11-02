num_tickets = 98   #кол-во проданных билетов (пассажиров)
bus_capacity = 20  #кол-во мест в автобусе

bus_quantity = num_tickets//bus_capacity  #кол-во полных автобусов
num_tickets_left = num_tickets % bus_capacity  #кол-во оставшихся пассажиров

has_partial_bus = False #неполный автобус (True - если есть, False - если нет)
empty_seats = 0 #кол-во пустых мест, если автобус неполный

if num_tickets_left: # num_tickets_left = 0, т.е False
    if num_tickets_left >= bus_capacity / 2: #если кол-во оставшихся пассажиров хватает на полавтобуса,
        bus_quantity += 1 #прибавляем наполовину заполненный автобус к кол-ву полных автобусов
        has_partial_bus = True

        empty_seats = bus_capacity - num_tickets_left #кол-во пустых мест, если автобус неполныйв
        num_tickets_left = 0  #равно 0, т.к. не будет оставшихся пассажиров, мы их разместили в неполный автобус

print(bus_quantity, num_tickets_left, has_partial_bus, empty_seats )







