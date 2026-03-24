#Smart Email Validator & Analyzer

print("Welcome to Email Validator\n")

email = input("Enter your email: ").strip()

#Basic checks
if "@" in email and "." in email:
    
    parts = email.split("@")

    #Ensure only one @
    if len(parts) == 2:
        username = parts[0]
        domain_part = parts[1]
        
        # Check domain structure
        if "." in domain_part:
            domain_parts = domain_part.split(".")
            
            domain_name = domain_parts[0]
            extension = domain_parts[-1]
            
            # Final validation
            if username != "" and domain_name != "" and extension != "":
                
                print("\n Valid Email Address")
                print(f" Username   : {username}")
                print(f" Domain     : {domain_name}")
                print(f" Extension  : .{extension}")
            
            else:
                print("Invalid Email (missing parts)")
        else:
            print("Invalid Email (no domain extension)")
    
    else:
        print(" Invalid Email (multiple @ symbols)")
else:
    print(" Invalid Email format")
