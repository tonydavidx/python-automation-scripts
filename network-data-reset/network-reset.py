import datetime, os

today = datetime.date.today()
with open(
    "D:/Documents/python/Automation/network-data-reset/last_run_date.txt", "r"
) as f:
    last_run = f.read()
print("today" + str(today))
print("last Run " + last_run)

if str(today) != last_run:
    try:
        print("Resetting Network Data")
        os.system("C:/programs/reset_network_data_usage/reset_data_usage.cmd")
        with open(
            "D:/Documents/python/Automation/network-data-reset/last_run_date.txt", "w"
        ) as f:
            f.write(str(today))
    except Exception as e:
        print(e)

else:
    print("Already reseted today")
    exit()
