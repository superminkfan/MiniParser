# data_processing.py

def clean_data(records):
    """
    Clean and convert the extracted log records into numeric formats.

    :param records: list of dict, each dict with keys:
                    timestamp, curLoad, avgLoad, heapUsed, heapFree,
                    defaultUsedRam, defaultFreeRam (all strings or None)
    :return: list of dict with the same keys but numeric values where applicable
    """
    cleaned_records = []
    for rec in records:
        # Convert string to float or int
        # curLoad, avgLoad, heapFree, defaultFreeRam are floats
        # heapUsed, defaultUsedRam are ints

        # Note: We can have some None values if the log didn't provide all data
        # We'll just skip those or convert them if possible
        new_rec = {
            "timestamp": rec["timestamp"]
        }

        # Convert curLoad, avgLoad, heapFree, defaultFreeRam to float
        for key in ["curLoad", "avgLoad", "heapFree", "defaultFreeRam"]:
            val = rec.get(key)
            if val is not None:
                new_rec[key] = float(val)
            else:
                new_rec[key] = None

        # Convert heapUsed, defaultUsedRam to int
        for key in ["heapUsed", "defaultUsedRam"]:
            val = rec.get(key)
            if val is not None:
                new_rec[key] = int(val)
            else:
                new_rec[key] = None

        # Append cleaned record
        cleaned_records.append(new_rec)

    return cleaned_records
