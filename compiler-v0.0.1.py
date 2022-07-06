
print("""

function printf(val: any) {
    val = val + ""
    _printf(val)
}

function _printf(val: string) {
    for (let i of val) {
        basic.showString(i, 40)
        basic.clearScreen()
        basic.pause(30)
    }
    basic.pause(240)
}

""")

with open("script.js", "r") as script:
    script = script.readlines()

for line in script:
    if line.strip().startswith("printf"):
        line = line.split("::")[1]
        print("printf("+str(line).strip()+")")
    elif line.strip().startswith("loop"):
        line = line.split("::")[1]
        print("for(let _val = 0;_val < "+str(line).strip()+";_val++){let loop_index = _val")
    elif line.strip().startswith("end"):
        print("\n}")
    
    elif line.strip().startswith("forever"):
        print("while (true){")

    elif line.strip().startswith("if::btn_a"):
        print("if(input.buttonIsPressed(Button.A)) {")

    elif line.strip().startswith("if::btn_b"):
        print("if(input.buttonIsPressed(Button.B)) {")



