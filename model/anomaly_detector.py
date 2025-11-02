import statistics

def detect_anomalies(builds):
    durations = [b['duration'] for b in builds]
    mean = statistics.mean(durations)
    stddev = statistics.pstdev(durations)
    
    for b in builds:
        z = (b['duration'] - mean) / (stddev if stddev else 1)
        b['anomaly'] = abs(z) > 2  # anomaly if Z-score > 2
    return builds
