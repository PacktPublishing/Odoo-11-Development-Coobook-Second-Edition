
### Get this product for $5

<i>Packt is having its biggest sale of the year. Get this eBook or any other book, video, or course that you like just for $5 each</i>


<b><p align='center'>[Buy now](https://packt.link/9781788471817)</p></b>


<b><p align='center'>[Buy similar titles for just $5](https://subscription.packtpub.com/search)</p></b>


# Odoo 11 Development Cookbook - Second Edition
This is the code repository for [Odoo 11 Development Cookbook - Second Edition](https://www.packtpub.com/application-development/odoo-11-development-coobook-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781788471817), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
Odoo is a full-featured open source ERP with a focus on extensibility. The flexibility and sustainability of open source are also a key selling point of Odoo. It is built on a powerful framework for rapid application development, both for back-end applications and front-end websites. Version 11 offers better usability and speed: a new design (as compared to the current Odoo Enterprise version) and a mobile interface.

The book starts by covering Odoo installation and administration and Odoo Server deployment. It then delves into the implementation of Odoo modules, the different inheritance models available in Odoo. You will then learn how to define access rules for your data; how to make your application available in different languages; how to expose your data models to end users on the back end and on the front end; and how to create beautiful PDF versions of your data.

By the end of the book, you will have a thorough knowledge of Odoo and will be able to build effective applications by applying Odoo development best practices

## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter03.



The code will look like the following:
```
from odoo import models, fields, api 
class LibraryBook(models.Model): 
    # [...] 
    state = fields.Selection([('draft', 'Unavailable'), 
                              ('available', 'Available'), 
                              ('borrowed', 'Borrowed'), 
                              ('lost', 'Lost')], 
                             'State') 
```

The setup recipes in Chapter 1, Installing the Odoo Development Environment, and Chapter 16, Web Client Development, expect that you are working on a server running Debian GNU/Linux, or a derivative distribution such as Ubuntu, in a reasonably up-to-date release. If you are running another distribution, things should be fairly straightforward; the main differences should be in the names of the packages to install, and possibly the location of the configuration files of PostgreSQL and Nginx.

If your workstation is running Windows or MacOS, we advise you to set up a Debian virtual machine to work with Odoo. While it is possible to develop natively on Windows or Mac, having a development environment as close to the deployment environment as possible is a good way to avoid nasty surprises, and GNU/Linux is the recommended deployment platform for Odoo.

Is there a recommended Integrated Development Environment (IDE) for Odoo? This is a frequently asked question by newcomers. The best answer is to use whatever tool you are familiar with. Popular choices include Eclipse or PyCharm, but a very high number of experimented developers, including the core Odoo developers, just use a programming text editor such as vim, GNU emacs, or Sublime Text to have syntax highlighting and useful helpers such as automatic indentation, while using the Python debugger for debugging. It is recommended that you start with the basic tools, because IDEs have a tendency to hide complexity that you should be familiar with in order to fix the more difficult problems.

## Related Products
* [Odoo 10 Implementation Cookbook](https://www.packtpub.com/application-development/odoo-10-implementation-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781787123427)

* [Working with Odoo 10 - Second Edition](https://www.packtpub.com/application-development/working-odoo-10-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781786462688)

* [Working with Odoo 11 - Third Edition](https://www.packtpub.com/application-development/working-odoo-11-third-edition?utm_source=github&utm_medium=repository&utm_campaign=9781788476959)
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781788471817">https://packt.link/free-ebook/9781788471817 </a> </p>