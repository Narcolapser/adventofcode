times, distances = open('d06.sample').read().split('\n')
times, distances = open('d06.input').read().split('\n')

#times = [int(time) for time in times.split(' ') if time.isdigit()]
#distances = [int(distance) for distance in distances.split(' ') if distance.isdigit()]

times = [time for time in times.split(' ') if time.isdigit()]
distances = [distance for distance in distances.split(' ') if distance.isdigit()]

times = [int(''.join(times))]
distances = [int(''.join(distances))]

def calculate_distances(time):
    distances = []
    for i in range(time):
        hold_time = i
        travel_time = time - i
        distance = hold_time * travel_time
        distances.append(distance)
    return distances

result = 1
for i,time in enumerate(times):
    heat = [d for d in calculate_distances(time) if d > distances[i]]
    result *= len(heat)

print(result)