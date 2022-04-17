#!/usr/bin/python3
import os
import time
import webbrowser

def db():
    os.system("sudo apt-get install -y mysql-server")
    print("\n[*] Configurando base de datos escriba la contraseña que proporcionó durante la instalación\n\n")
    print("\n\n[!] Copie y pegue lo siguiente vaya línea por línea:\n\nCREATE DATABASE joomladb;\n\nCREATE USER 'joomlauser'@'localhost' IDENTIFIED BY 'password123';")
    print("\n\nGRANT ALL PRIVILEGES on joomladb.* TO 'joomlauser'@'localhost';\n\nFLUSH PRIVILEGES;\n\nquit;")
    time.sleep(5)
    os.system("mysql -u root -p")
    
def installation():
    print("\n[*] Actualizando el sistema...\n")
    time.sleep(1)
    os.system("sudo apt-get update -y > /dev/null && sudo apt-get upgrade -y > /dev/null")
    time.sleep(1)
    print("\n[+] Sistema actualizado!\n")
    time.sleep(1)
    print("\n[*] Instalando LAMP...\n")
    time.sleep(1)
    os.system("sudo apt-get install -y apache2 apache2-utils")
    os.system("clear")
    print("\n[*] Instalando sql...\n")
    os.system("sudo apt-get install -y mysql-server")
    os.system("clear")
    print("\n[*] Instalando php\n")
    os.system("sudo apt-get install -y php5 libapache2-mod-php5 php5-cli php5-mysql")
    os.system("sudo apt-get install --fix-broken -y")
    time.sleep(2)
    os.system("sudo service apache2 start")
    os.system("sudo systemctl enable apache2")
    os.system("sudo ufw allow www > /dev/null")
    os.system("sudo ufw allow https > dev/null")
    print("\nConfigure algunos parametros...\n\n")
    time.sleep(2)
    print("\n[+] LAMP instalado\n")
    time.sleep(2)
    os.system("clear")
    print("\n[*] Configurando base de datos escriba la contraseña que proporcionó durante la instalación\n\n")
    print("\n\n[!] Copie y pegue lo siguiente vaya línea por línea:\n\nCREATE DATABASE joomladb;\n\nCREATE USER 'joomlauser'@'localhost' IDENTIFIED BY 'password123';")
    print("\n\nGRANT ALL PRIVILEGES on joomladb.* TO 'joomlauser'@'localhost';\n\nFLUSH PRIVILEGES;\n\nquit;")
    time.sleep(6)
    mydb = db()
    os.system("wget https://downloads.joomla.org/cms/joomla3/3-9-16/Joomla_3-9-16-Stable-Full_Package.zip")
    time.sleep(1)
    os.system("mkdir /var/www/html/joomla")
    os.system("mv Joomla_3-9-16-Stable-Full_Package.zip /var/www/html/joomla/joomla.zip")
    os.system("cd /var/www/html/joomla && unzip /var/www/html/joomla/joomla.zip")
    os.system("clear")
    os.system("chown -R www-data:www-data /var/www/html/joomla")
    os.system("find /var/www/html/joomla -type f -exec chmod 0644 {} \;")
    os.system("find /var/www/html/joomla -type d -exec chmod 0755 {} \;")
    os.system("sudo chmod -R 755 /var/www/html/joomla")
    ask = input("\n[*] Quiere cambiar el nombre del equipo (S/N)? \n")
    if ask == "S":
        hostname = input("\n\n>>> ")
        os.system("hostnamectl set-hostname "+hostname)
        print("\n[+] El equipo ha cambiado de nombre:\n")
        os.system("cat /etc/hostname")
    elif ask == "N":
        print("\n[*] El nombre del equipo quedará como:\n")
        os.system("cat /etc/hostname")
    
    time.sleep(5)
    print("\n[*] Configurando Servidor web Apache...\n")
    os.system("(echo <VirtualHost *:80>; echo ServerName joomla.example.com; echo ServerAdmin webmaster@example.com; DocumentRoot /var/www/html/joomla; echo  <Directory /var/www/html/joomla>; echo Allowoverride all; echo </Directory>; echo </VirtualHost>) >>/etc/apache2/sites-available/joomla.conf")
    os.system("sudo a2dissite 000-default.conf")
    os.system("sudo a2ensite joomla.conf")
    print("\n\[+] Apache web server configurado\n")
    os.system("sudo systemctl restart apache2")
    os.system("clear")
    print("\n[*] Abriendo el navegador...\n\n\n>Si ya contaba con algo mas corriendo por el puerto 80 debe pararlo por un momento\n>Puede probar accediendo con http://joomla.example.com (antes se debe modificar quien resuelve este dominio)\n>>Con la web de joomla iniciada debe poner los parametros configurados en la base de datos\n>>Las credenciales son: Base de datos -> joomladb; User -> joomlauser; password -> password123\n\n\n>(Siguiendo los pasos...) En la primera pantalla de Joomla debemos poner un correo con una contraseña para usar este CMS más adelante")
    time.sleep(15)
    webbrowser.open("http://localhost/joomla", new=2)
    
def menu():
    time.sleep(1)
    print("\n1 -> Instalar todo el CMS")
    time.sleep(1)
    print("\n2 -> Instalar solo base de datos")
    time.sleep(1)
    print("\n3 -> Salir")
    choose = input("\n\n--> ")
    
    if choose == "1":
        installation()
    if choose == "2":
        db()
    if choose == "3":
        exit()
    
if __name__ == "__main__":
    menu()