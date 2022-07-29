# igs-manager

## 1 - Install Python:
Version 3.10.1 <br>
link: https://www.python.org/downloads/ <br>
## 2 - Clone project or Download ZIP<br>
git: https://github.com/tavares51/igs-manager.git <br>
## 3 - Create Virtualenv: <br>
in project diretory, open CMD.
install: pip install virtualenv <br>
command: python -m venv ./venv <br>
activate: venv\Scripts\activate.bat <br>
## 4 - Install Requirements <br>
command: pip install -r requirements.txt <br>
## 5 - Configure Database: <br>
Database has already been configured.
## 6 - Create Superuser: <br>
command: python manage.py createsuperuser <br>
choice or login, e-mail and pasword. <br>
## 7 - Run Project <br>
command: python manage.py runserver <br>
access: http://127.0.0.1:8000/ <br>
employee route: http://127.0.0.1:8000/employee/ (list, add, delete) <br>
departament route: http://127.0.0.1:8000/departament/ (list, add, delete) <br>
### 7.1 - When opening, we have the employee and department routes, just click on the desired route
![image](https://user-images.githubusercontent.com/54647142/181620240-45ae8af0-05a0-4930-a9f3-35c4d4b624b6.png)
#### 7.1.1 - Route: Employee
![image](https://user-images.githubusercontent.com/54647142/181620446-49c969b6-a79c-43d7-9a53-00d7002c3da2.png)
#### 7.1.2 - Route: Departament
![image](https://user-images.githubusercontent.com/54647142/181620592-ad0d0a02-44f7-4129-a441-549dc9aa74f5.png) <br>
## 8 - Admin <br>
access: http://127.0.0.1:8000/admin/
### 8.1 - Sign-in whith superuser (created in step 6)
![image](https://user-images.githubusercontent.com/54647142/181621214-e80058d2-8a32-49e7-8852-4a5ff49491ad.png)
### 8.2 - Employee management screen
![image](https://user-images.githubusercontent.com/54647142/181621454-65afab4d-acb0-42e9-8579-97f5f45b3ef0.png)
#### 8.2.1 - Departament screen
![image](https://user-images.githubusercontent.com/54647142/181623899-ef016c26-ea86-4232-b9f0-f1f140839090.png)
#### 8.2.2 - Employee screen
![image](https://user-images.githubusercontent.com/54647142/181624001-3fe62909-acec-444a-90fe-c7c1060b1ca5.png)
## 9 - Employee List <br>
access: https://igs-manager.herokuapp.com/ (public website) or http://127.0.0.1:8000/list-employees/ (local)
![image](https://user-images.githubusercontent.com/54647142/181623618-5fe740ef-01de-4276-8a4f-f6f2964aed0b.png)
## 10 - Swagger (Plus) <br>
access: http://127.0.0.1:8000/swagger/schema/
![image](https://user-images.githubusercontent.com/54647142/181624725-ca36f8ab-e481-4cd8-bb21-20cf2b6c27cc.png)
#### Obs: When entering an invalid e-mail address, the system automatically returns an error
![image](https://user-images.githubusercontent.com/54647142/181634141-2ea9bedc-d350-40c3-92b4-12bfa4c116ac.png)
