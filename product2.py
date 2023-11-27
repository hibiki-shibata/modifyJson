import json

print('Type the file name babygirl')
input_file = input()
# input_file = "test.json"

try:
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    def remove_product_hierarchy(item):
        if isinstance(item, dict):
            if "product_hierarchy_level_id" in item:
                del item["product_hierarchy_level_id"]
            else:
                for key, value in item.items():
                    remove_product_hierarchy(value)
        elif isinstance(item, list):
            for element in item:
                remove_product_hierarchy(element)


    def remove_restrictions(item):
        if isinstance(item, dict):
            if "restrictions" in item:
                del item["restrictions"]
            else:
                for key, value in item.items():
                    remove_restrictions(value)
        elif isinstance(item, list):
            for element in item:
                remove_restrictions(element)

    
    def true_to_false(item):
        if isinstance(item, dict):
            if "is_over_the_counter" in item and item["is_over_the_counter"] == True:
               item["is_over_the_counter"] = False
            else:
                for key, value in item.items():
                    true_to_false(value)
        elif isinstance(item, list):
            for element in item:
                true_to_false(element)


    if "items" in data:
        
        # Call the functions to remove "product_hierarchy_level_id" and "restrictions"
        remove_product_hierarchy(data["items"])
        remove_restrictions(data["items"])
        true_to_false(data["items"])



        with open(input_file, 'w') as outfile:
            json.dump(data, outfile, indent=2)

        print("Successful")
    else:
        print("The 'items' key is not present in the JSON file.")

except Exception as e:
    print(f"An error occurred: {str(e)}")