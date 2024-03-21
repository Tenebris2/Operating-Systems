def get_data_for_resource_request(path):
    data = []

    with open(path, "r") as file:
        for line in file:
            elements = [int(element) for element in line.split(' ')]
            data.append(elements)
    resources = data[0]
    length = int(len(data[1]) / 2)
    allocation = [sub_array[:length] for sub_array in data][1:]
    max = [sub_array[length:] for sub_array in data][1:]

    max_allocation = [0] * len(allocation)
    for i in range(len(allocation[0])):
        for j in range(len(allocation)):
            max_allocation[i] += allocation[j][i]

    available = [0] * 3
    for i in range(len(resources)):
        available[i] = resources[i] - max_allocation[i]

    need = []
    for i in range(len(allocation)):
        need_element = [0] * len(allocation[0])
        for j in range(len(allocation[0])):
            need_element[j] = max[i][j] - allocation[i][j]
        need.append(need_element)

    data = []
    data.extend([allocation, need, available])

    return data

def get_data_for_detection(path):
    data = []

    with open(path, "r") as file:
        for line in file:
            elements = [int(element) for element in line.split(' ')]
            data.append(elements)
    resources = data[0]

    length = int(len(data[1]) / 2)
    allocation = [sub_array[:length] for sub_array in data][1:]
    request = [sub_array[length:] for sub_array in data][1:]

    max_allocation = [0] * len(allocation)
    for i in range(len(allocation[0])):
        for j in range(len(allocation)):
            max_allocation[i] += allocation[j][i]

    available = [0] * 3
    for i in range(len(resources)):
        available[i] = resources[i] - max_allocation[i]
        
    data = []

    data.extend([allocation, request, available])

    return data
