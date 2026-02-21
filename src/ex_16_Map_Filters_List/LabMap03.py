response_times_ms = [1200, 1500, 1800]

def mil_sec(x):
    return x/100


# response_times_s = list(map(mil_sec, response_times_ms))
response_times = list(map(lambda x: x/100, response_times_ms))
print(response_times)