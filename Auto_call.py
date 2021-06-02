import time
count = 1
while count:
      print("Ingestion Initiated")
      exec(open('data_ingestion.py').read())
      time.sleep(60)
      print("Ingestion Re-Initiated")

