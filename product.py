import json

print('Type the file name babygirl')
input_file = input()
# input_file = "test.json"

try:
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    def remove_product_hierarchy(item):

        if isinstance(item, dict):
            keys_to_remove = []
            
            for key, value in item.items():

                if key == "product_hierarchy_level_id":
                    keys_to_remove.append(key)
                    
                remove_product_hierarchy(value)

            for key in keys_to_remove:
                del item[key] # this line delte keys and values
                # print(item[key])

        elif isinstance(item, list):
            for element in item:             
                remove_product_hierarchy(element)

    if "items" in data:
        # print(data["items"])
        remove_product_hierarchy(data["items"])

        with open(input_file, 'w') as outfile:
            json.dump(data, outfile, indent=2)

        print("Successfull")
    else:
        print("The 'items' key is not present in the JSON file.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
