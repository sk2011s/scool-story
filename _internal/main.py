import json
from datetime import datetime
import os


print(
      f"""
this app Created By sk2011se
and Created For Write Your School Story\n""".replace("\n", "", 1)
      )


text = ""


def show_vars(config, vars):
    print("Teachers:")
    for i in config["teachers"].keys():
        print("\t" + i)
    print("\nvars:")   
    for i in vars["vars"].keys():
        print("\t" + i)

with open("config.json", "r") as f:
        config: object = json.load(f)
        f.close()
        
with open("vars.json", "r") as f:
        varsc: object = json.load(f)
        f.close()


save_folder = f"{config["save_Folder"]}"


with open(config["format_file"], "r") as f:
    text_format: str = f.read()
    f.close()


#print(datetime.now().date())

file_name = f"{datetime.now().date()}--{config['weekdays'][datetime.now().weekday()]}.txt"


full_path = os.path.join(save_folder, file_name)
if not os.path.exists(full_path):
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
with open(full_path, "w") as f:
    f.write(text_format)
    f.close()

show_vars(config, varsc)

os.system(f"call \"{os.path.join(save_folder, file_name)}\"")

with open(full_path, "r") as f:
    text = f.read()
    teachers = config["teachers"]
    for i in teachers.keys():
        if "%"+i+"%" in text:
            text = text.replace("%"+i+"%", teachers.get(i), 1)
    f.close()

    with open(full_path, "w") as ff:
        ff.write(text)

        ff.close()
    f.close()


        
        

with open(full_path, "r") as f:
    text = f.read()
    vars = varsc["vars"]
    for i in vars.keys():
        if "%"+i+"%" in text:
            text = text.replace("%"+i+"%", vars.get(i), 1)
    f.close()

    text = text.replace("%"+"date"+"%", str(datetime.now().date()))

    with open(full_path, "w") as ff:
        ff.write(text)

        ff.close()
    f.close()


while True:
    Enter = str(input("Press Enter"))
    if Enter == "":
        break
    else:
        continue