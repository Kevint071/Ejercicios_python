import js2py

js = 'console.log("Hello world")'

python = js2py.eval_js(js)

print(python)

js2 = '''function add (a, b){
    return a + b
    
    }

'''

a = int(input("Digite un numero: "))

python = js2py.eval_js(js2)

print(python)