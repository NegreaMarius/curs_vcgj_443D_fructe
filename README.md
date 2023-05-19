# 0.1 Masina Virtuala

Virtual Box: https://download.virtualbox.org/virtualbox/7.0.8/VirtualBox-7.0.8-156879-Win.exe
Ubuntu: https://releases.ubuntu.com/kinetic/ubuntu-22.10-desktop-amd64.iso


sudo apt install vim -y

sudo apt install net-tools -y

sudo apt install build-essential dkms linux-headers-$(uname -r) -y

sudo mkdir /mnt/cdrom

sudo mount /dev/cdrom /mnt/cdrom

sudo ./VboxLinuxAdditions.run


Verificare functionare:

~merge copy paste de pe PCul de baza pe masina virtuala si invers

~rezolutia se schimba cand redimesionezi fereastra (nu ramane un patrat)



# 0.2 Git

Creare oriunde (Desktop, Home, etc) a unui folder numit "git"

![Figura1FolderGit](https://github.com/NegreaMarius/curs_vcgj_443D_fructe/assets/127781317/e48fdae6-965d-41b3-b258-180ea2674f85)

Click dreapta->New folder

Apoi click dreapta *in interiorul* folderului "git" -> Open in Terminal


sudo apt update

sudo apt install git-all

sudo apt intall python3.10-venv


Verificare functionare:

*IN TERMINAL:

git

![Figura2VerificareGit](https://github.com/NegreaMarius/curs_vcgj_443D_fructe/assets/127781317/a75eed49-a74b-4931-a11a-cda7b2ab9483)



# 0.3 Docker

sudo apt-get update

sudo apt-get install ca-certificates curl gnupg lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu 
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo chmod a+r /etc/apt/keyrings/docker.gpg

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose -y


Verificare functionare:

sudo docker --help

![Figura3VerificareDocker](https://github.com/NegreaMarius/curs_vcgj_443D_fructe/assets/127781317/dd68bbcc-eeb0-47b1-9701-c5fcdcd4172d)



# 0.4 Jenskins
java -version

sudo apt install openjdk-11-jdk -y

curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update

sudo apt install jenkins -y

sudo systemctl status jenkins

sudo ufw allow 8080

sudo ufw status

sudo ufw enable


Browser Firefox: http://localhost:8080

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

Copiere cod

Browser Firefox: Introducere cod

Browser Firefox: Buton “Install suggested plugins”

Browser Firefox: Configurare User & Parola


Instalare Blue Ocean

Browser Firefox: http://localhost:8080

In stanga Manage Jenkins

Plugins (La System Configurations)

Search "Blue Ocean"


![Figura4JenskinsBlueOcean](https://github.com/NegreaMarius/curs_vcgj_443D_fructe/assets/127781317/724f3e8e-f814-4ef8-8951-a2f035e3f894)



# 0.5 Verificari
git

sudo docker --help

Browser Firefox: http://localhost:8080



# 0.6 Installs
sudo apt install python3-pip

pip install flask

pip install pytest

sudo apt install gedit

sudo apt install python3.10-venv



# 0.7 Generare Token Git
https://github.com

Dreapta sus la poza ta: Settings

Scroll down putin, stanga jos: Developer Settings

Personal Access Tokens

Tokens (classic)

Generate new token (classic)

Note: 443D_fructe

Expirare: 30 zile

Bifat Repo

Generate Token

!!! copiat tokenul intr-un notepad !!!



# 1. Cod Aplicatie
Click dreapta in interiorul folderului git

Open in Terminal


git clone https://github.com/NegreaMarius/curs_vcgj_443D_fructe.git

cd curs_vcgj_443D_fructe/

git status

git branch devel/USERGIT_FRUIT

git checkout devel/USERGIT_FRUIT

gedit

CTRL+Z

bg

F9 (In gedit)


Folder app

443D_fructe.py

Introdus dupa ultimele functii si inainte de ”app.run(host = "127.0.0.1", port = 5002)


Folder lib

biblioteca_fructe.py


Folder tests

test_biblioteca_fructe.py


cd app

python3 443D_fructe.py


Browser Firefox http://127.0.0.1:5002/FRUIT

Screenshot 1: 1.1web_443D_fructe



# 6. Test Manual Aplicatie WEB
python3 -m pytest -v

Screenshot 2: 6.1teste_manuale



# 2. Cod GIT dev
git config --global user.email "MAILULTAU@yahoo.com" 

git config --global user.name "USERGIT"

git config credential.helper store

git status

git add *

git commit -m "Modificare coduri NUME"

git push --set-upstream origin devel/USERGIT_FRUIT



# 3. Pull Request + Review-uri
Browser Firefox: https://github.com/NegreaMarius/curs_vcgj_443D_fructe

Buton Compare and pull request



# 4. Integrare devel - main
Adaugare contributor/reviewers: NegreaMarius

Screenshot 3: 4.1integrare_in_main



# 5. Testare cu Jenkins
Browser Firefox: http://localhost:8080/

Stanga sus: New Item

Item Name: USERGIT_FRUIT

Selectare PipeLine

OK

PipeLine -> Definition -> Pipeline script from SCM

SCM = Git

Repository URL = https://github.com/NegreaMarius/curs_vcgj_443D_fructe.git

Branch Specifier = */devel/USERGIT_FRUIT

Apply

Save

Stanga sus - Build Now

Apasare pe #1 cu bifa verde

Stanga Open Blue Ocean

Apasare pe bulina "Unit Testing cu pytest"

Screenshot 4: 5.1jenkins_sus

Screenshot 5: 5.2jenkins_jos



# 7&8. Apel+test container
cd ..

Ne aflam in folderul principal 

sudo docker build -t 443d_fructe:v01 .

sudo docker run --name 443d_fructe -p 8020:5020 443d_fructe:v01

Browser Firefox: http://127.0.0.1:8020/FRUIT

Screenshot 6: 7.1docker



# 9. Documentatie personala
!!!INTRAT PE GIT DE PE WINDOWS!!

https://github.com/NegreaMarius/curs_vcgj_443D_fructe.git

Intra pe branchul tau

Add file

Create new file

Name= README_USERGIT_FRUIT.md

Vezi notepad Documentatie.txt pentru structura

lipeste pozele



# 10. Documentatie in main
editare README.md pe web:

NUME - FRUIT: 

[README_USERGIT_FRUIT](./README_USERGIT_FRUIT.md)



# Extra
Inchidere proces de pe portul 5002

fuser -k 5002/tcp


Stergere containere & imagini

sudo docker ps -a

sudo docker rm CONTAINER ID

sudo docker images -a

sudo docker rmi IMAGE ID



# README-uri PERSONALE



# NEGREA M. Marius-Ştefan - rodie: 
[README_NegreaMarius_rodie](./README_NegreaMarius_rodie.md)

# BĂNESCU A.F. Alexandru - capsuna: 
[README_BanescuAlexandru_capsuna](./README_BanescuAlexandru_capsuna.md)

# BELIŢOIU F.M. Rareş-Florian - mar: 
[README_BelitoiuRares_mar](./README_BelitoiuRares_mar.md)

# ŞPAN O. Lorin - vanata: 
[README_lorinspan_vanata](./README_lorinspan_vanata.md)

# VASILESCU P. Bogdan - piersica: 
[README_bogdanishere_piersica](./README_bogdanishere_piersica.md)

# VASILE M. Vlad-Andrei - kiwi: 
[README_vladvasile1_kiwi](./README_vladvasile1_kiwi.md)

# TUDOSE V.D. Bogdan-Mihai - portocala: 
[README_bobtudose_portocala](./README_bobtudose_portocala.md)

# STĂNCULESCU M. Andrei - avocado: 
[README_andstanc_avocado](./README_andstanc_avocado.md)

# URZICĂ C. Andrei-Octavian - ananas: 
[README_andreiurzica1_ananas](./README_andreiurzica1_ananas.md)

# PARPALEA I.V. Alexandra - pepene_galben: 
[README_alexandraparpalea1510_pepene_galben](./README_alexandraparpalea1510_pepene_galben.md)

# ROŞU E. Georgiana - pepene_rosu: 
[README_Georgiana008_pepene_rosu](./README_Georgiana008_pepene_rosu.md)

# ARNĂUTU V. Gabriel-Dorin - clementina: 
[README_gabrielarnautu_clementina](./README_gabrielarnautu_clementina.md)

# TEODORESCU T.I. Ciprian - banana: 
[README_ciprianteodorescu_banana](./README_ciprianteodorescu_banana.md)

# ŞTEFAN E. Ion-Alexandru - strugure: 
[README_StefanAlexandru18_strugure](./README_StefanAlexandru18_strugure.md)

# RODRIGUEZ-RAMIREZ-ZAHARIA J.A. Nicolas - mandarina: 
[README_nico130301_mandarina](./README_nico130301_mandarina.md)

# ŞERBULEA J. Ana-Corina - curmala: 
[README_CorinaSerbulea_curmala](./README_CorinaSerbulea_curmala.md)

# GHIOJDEANU C.O. Ştefan-Mihnea - cireasa: 
[README_StefanGhio_cireasa](./README_StefanGhio_cireasa.md)

# SIMA D. Andrei-Mihai - papaya: 
[README_AndreiSima10_papaya](./README_AndreiSima10_papaya.md)

# IANCU M. Matei-Theodor - smochina: 
[README_iancumatei67_smochina](./README_iancumatei67_smochina.md)

# ROCEANU E. Adelin-Adrian - caisa: 
[README_adelinjokeru_caisa](./README_adelinjokeru_caisa.md)
