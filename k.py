from datetime import datetime, timedelta

def calculate_work_hours(target_hours=8):
    fmt = "%H:%M"
    total_work = timedelta()
    last_in = None

    print("Enter your IN/OUT times (HH:MM IN/OUT). Type 'done' when finished:")

    while True:
        entry = input("> ").strip()
        if entry.lower() == "done":
            break
        try:
            time_str, status = entry.split()
            time_obj = datetime.strptime(time_str, fmt)
            if status.upper() == "IN":
                last_in = time_obj
            elif status.upper() == "OUT" and last_in:
                total_work += (time_obj - last_in)
                last_in = None
        except:
            print("Invalid format. Use HH:MM IN/OUT (e.g., 10:07 IN)")

    current_time = input("Enter current time (HH:MM): ").strip()
    now = datetime.strptime(current_time, fmt)

    if last_in:
        total_work += (now - last_in)

    target = timedelta(hours=target_hours)
    remaining = target - total_work
    end_time = now + remaining if remaining > timedelta(0) else now

    print("\n--- Work Summary ---")
    print("Total worked:", total_work)
    print("Remaining:", remaining if remaining > timedelta(0) else "Completed")
    print("Expected end time:", end_time.strftime(fmt))

# Run the function
calculate_work_hours(target_hours=8)

there some changes m doing in the stashy area let see how it works S