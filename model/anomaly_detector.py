def detect_anomalies(builds):
    """
    Detect anomalies based on build duration and failure status.
    A build is marked as anomaly if:
    - duration > 100 seconds, OR
    - status == 'FAILURE'
    """
    results = []
    for b in builds:
        build_id = b.get("build_id", "N/A")
        duration = b.get("duration", 0)
        status = b.get("status", "").upper()

        # Define anomaly condition
        is_anomaly = (duration > 100) or (status == "FAILURE")

        note = ""
        if is_anomaly:
            if status == "FAILURE":
                note = "Build Failed"
            elif duration > 100:
                note = f"Long Duration: {duration}s"
        else:
            note = "Normal"

        results.append({
            "build_id": build_id,
            "is_anomaly": is_anomaly,
            "note": note
        })

    return results
