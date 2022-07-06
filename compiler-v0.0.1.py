print("""
function printf(val: any) {
    val = val + ""
    _printf(val)
}
function _printf(val: string) {
    for (let i of val) {
        basic.showString(i, 20)
        basic.showString(i, 20)
        basic.clearScreen()
        
    }
}
function printresp(val: any) {
    val = val + "";
    _printresp(val)
}
function _printresp(val: string) {
    for (let i of val) {
        basic.showString(i, 20)
    }
}
""")

with open("script.js", "r") as script:
    script = script.readlines()

for line in script:
    if line.strip().startswith("printf"):
        line = line.split("::")[1]
        print("printf("+str(line).strip()+")")
    elif line.strip().startswith("printresp"):
        line = line.split("::")[1]
        print("printresp("+str(line).strip()+")")
    elif line.strip().startswith("loop"):
        line = line.split("::")[1]
        print("for(let _val = 0;_val < "+str(line).strip()+";_val++){let loop_index = _val")
    elif line.strip().startswith("end"):
        print("\n}")
    
    elif line.strip().startswith("forever"):
        print("while (true){")



    elif line.strip().startswith("new"):
        line = line.split("::")
        line1 = line[1]
        line2 = line[2].strip()
        
        print("let " + line1 + ' = ' + line2)

    elif line.strip().startswith("change"):
        line = line.split("::")
        line1 = line[1]
        line2 = line[2].strip()
        
        print("" + line1 + ' = ' + line2)

    elif line.strip().startswith("if"):
        try:
            linen = line.split("::")
            line1 = linen[1].strip()
            line2 = linen[2].strip()
        except:
            pass;
        if line1 == "btn_a":
            print("if(input.buttonIsPressed(Button.A)) {")
        elif line1 == "btn_b":
            print("if(input.buttonIsPressed(Button.B)) {")
        else:
            print("if ("+line1+line2.strip()+line.strip().split("::")[3]+"){")
