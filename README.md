# E-commerce Model

This project aims to create a simple e-commerce model.
Things you can do:

- Create and update new users
- Add to Cart and make an order
- View Cart summary and set shipping information

In the future I'll be working on an administrator app to create, update and delete new products from site instead od Django Administrator. Also I'll be working on some fixed in checkout section.

On the following video you can see all the steps you need to follow to make this app run. 
https://drive.google.com/file/d/1sonK3Xh4ghtXQO55zp_bxHlDZdm1rhAf/view?usp=sharing

# Install 

For installing this software you need to do:

## Check python version
This project was written with python 3.9.12 so I strongly suggest you to test with this version or higher just to not have any compatibility issues.

How I check my python version, 

in *nix systems:

```bash
> python --version
> Python 3.9.12
```

in windows:

```bash
c:\> py --version
c:\> Python 3.9.12
```

## Install Dependencies

In order to install dependencies you need to run `pip install`, make sure you are in the project folder and you can see the `requirements.txt` file when you do a `ls` or `dir`:

```bash
> pip install -r requirements.txt
```
This last will return a bunch of stuff in the terminal.

`Some operative systems will required you to use pip3 instead of pip `

## Setting Up the Django Application

Once you finish the dependencies installation you need to run some django commands.

### Migrations

Initialize the database
*nix:
```bash
> python mananage.py migrate
```
windows:
```bash
c:\> py mananage.py migrate
```
### Create a superuser
In order to see the functions, you need to create some products in the database. To do this you need to create a superuser.

windows:
```bash
c:\> py mananage.py createsuperuser
Username (leave blank to use 'pc-user'):
Email address:
Password:  -> It is invisible.
Password (again): -> It is invisible too.
Superuser created succesfully.
```
Once you create the superuser, you will be able to access Django Project Administrator. Follow next steps to access to the app.

### Run the test server

```bash
> python mananage.py runserver
```
windows:
```bash
c:\> py mananage.py runserver
```
Go to http://127.0.0.1:8000/

to have access to the app.

If everthing goes well you should be able to open the browser and see the application run

