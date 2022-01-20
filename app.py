from browser import document,console,alert

input = document['input']
button = document['btn']
output = document['output']
select = document['select']
def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan angka')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp

def formula(x, y):
    match x:
        case'handphone':
            return y * 2500000
        case'laptop':
            return y * 13000000
        case'komputer':
            return y * 7000000
        
def main(ev):
    num = getNum(input.value)
    result = formula(select.value, num)
    output.textContent = str(result)

def keyEnter(ev):
    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)
input.bind("keypress", keyEnter)

