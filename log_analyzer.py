filename ="application.log"
try:
    if not filename.strip():
        raise ValueError("the file name is empty")
    with open(filename, "r") as file:
        count=0
        warning_count = 0
        errors = {}
        warnings = {}
        infos = {}
        malformed_count=0
        info_count=0
        for line in file:
            if not line.strip():
                 continue
            parts=line.split()
            if len(parts)<4 or parts[2] not in ("ERROR", "WARNING", "INFO"):
                malformed_count+=1
                continue
                

            if parts[2] == "WARNING":
                    warning_count+=1
                    warning_message = " ".join(parts[3:])
                    if warning_message in warnings:
                        warnings[warning_message]+=1
                    else:
                        warnings[warning_message] =1
         
                    

            if parts[2] == "INFO":
                info_count+=1
                info_message = " ".join(parts[3:])
                if info_message in infos:
                    infos[info_message]+=1
                else:
                    infos[info_message]=1
        
            if parts[2] == "ERROR":
                count+=1
                # parts= line.split()
                # if len(parts)<4 or parts[2]!="ERROR":
                #     malformed_count+=1
                #     continue
                # count+=1
                message = " ".join(parts[3:])
                if message in errors:
                    errors[message] += 1
                else:
                    errors[message]=1
    with open("analysis_report.txt", "w") as file:
        file.write("IT Support Log Analysis Report\n\n")

        file.write("Error summary:\n")

        result=  sorted(
            errors.items(), key = lambda item: item[1], 
            reverse = True
        )
        for message, occurences in result:
            file.write(f" {message}: {occurences} occurrences \n")

        if result:
            top_error = result[0][0]
            top_count = result[0][1]
            file.write(f" Most frequent error: {top_error} \n ")
            file.write(f"Occurrences:{top_count} \n ")
        else:
            file.write(f"there are no errors logs, so there are no frequent errors: \n\n ")
 
        file.write("\nwarnings summary:\n")
        warning_result = sorted(
        warnings.items(),key = lambda item: item[1],
        reverse = True
        )
        for warning_message , occurrences in warning_result:
            file.write(f"{warning_message}: {occurrences} occurrences \n")
        if  warning_result:
            top_warning = warning_result[0][0]
            top_count = warning_result[0][1]
            file.write(f"Most frequent warnings: {top_warning}\n")
            file.write(f"Occurrences {top_count}\n ")

        else: 
            file.write(f" there are no warning logs, so there are no frequent warnings\n ")

        
        file.write("\nINFO summary:\n")

        info_result = sorted(
            infos.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for info_message, occurrences in info_result:
            file.write(f"{info_message}: {occurrences} occurrences\n")

        if info_result:
            top_info = info_result[0][0]
            highest_count = info_result[0][1]

            counter = 0
            for info_message, occurrences in info_result:
                if occurrences == highest_count:
                    counter += 1

            if counter == 1:
                file.write(f"Most frequent INFO message: {top_info}\n")
                file.write(f"Occurrences: {highest_count}\n")
            else:
                file.write(
                    f"{counter} INFO messages are tied "
                    f"for the highest frequency ({highest_count}).\n"
                )

                for info_message, occurrences in info_result:
                    if occurrences == highest_count:
                        file.write(f"INFO message: {info_message}\n")
        else:
            file.write("There are no INFO logs.\n")


        file.write(f"\nTotal errors: {count}\n")
        file.write(f"Total warnings: {warning_count}\n")
        file.write(f"Total malformed entries: {malformed_count}\n")
        file.write(f"Total info entries: {info_count}\n")


except FileNotFoundError:
    print("application.log file not found")

except ValueError as e:
    print(e)

finally:
    print("Log analysis attempt is finished")


    