filename ="application.log"
try:
    if not filename.strip():
        raise ValueError("the file name is empty")
    with open(filename, "r") as file:
        count=0
        warning_count = 0
        errors = {}
        warnings = {}
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
        print("Error summary:")

        result=  sorted(
            errors.items(), key = lambda item: item[1], 
            reverse = True
        )
        for message, occurences in result:
            print(f" {message}: {occurences} occurrences")

        if result:
            top_error = result[0][0]
            top_count = result[0][1]
            print(" Most frequent error:" , top_error)
            print("Occurrences:" , top_count)
        else:
            print("there are no errors logs, so there are no frequent errors")

        print("warnings summary")
        warning_result = sorted(
        warnings.items(),key = lambda item: item[1],
        reverse = True
        )
        for warning_message , occurrences in warning_result:
            print(f" {warning_message}: {occurrences} occurrences")
        if  warning_result:
            top_warning = warning_result[0][0]
            top_count = warning_result[0][1]
            print("Most frequent warnings:", top_warning)
            print("Occurreneces" , top_count)

        else: 
            print(" there are no warning logs, so there are no frequent warnings")
    print("Total errors:" , count)
    print("Total warnings:" , warning_count)
    print("Total malformed entries:", malformed_count)
    print("Total info entries:" , info_count)


except FileNotFoundError:
    print("application.log file not found")

except ValueError as e:
    print(e)

finally:
    print("Log analysis attempt is finished")


    