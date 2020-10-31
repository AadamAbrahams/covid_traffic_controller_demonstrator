=====================================
COVID Traffic Controller Demonstrator
=====================================


.. image:: https://img.shields.io/pypi/v/covid_traffic_controller_demonstrator.svg
        :target: https://pypi.python.org/pypi/covid_traffic_controller_demonstrator

.. image:: https://img.shields.io/travis/AadamAbrahams/covid_traffic_controller_demonstrator.svg
        :target: https://travis-ci.com/AadamAbrahams/covid_traffic_controller_demonstrator

.. image:: https://readthedocs.org/projects/covid-traffic-controller-demonstrator/badge/?version=latest
        :target: https://covid-traffic-controller-demonstrator.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




This demonstrator is used to determine inward/outward human traffic for a store, using two PIR motion sensors, and relay this data to a host system to be displayed, on a monitor, at the storefront. The device also includes a thermal sensor to detect the temperature of an entering customer to establish whether they should be allowed entry. The use case purpose is to monitor and control the number of individuals within a store to limit the maximum shoppers at a given time, as well as determine eligibility of entry, as per COVID regulation.


* Free software: MIT license
* Documentation: https://covid-traffic-controller-demonstrator.readthedocs.io.


Features
--------

* Determine whether or not an individual is entering or exiting a building.
* Determine the temperature of an individual, and based on the result, illustrate whether they are applicable for entry.
* Updates a GUI to reflect any changes corresponding to the afformentioned actions.
* Security buzzer implementation, to warn an individual whom attempts to enter without scanning or with an above normal temperature.

Hardware and Software Prerequisites
-----------------------------------
The following list of hardware devices and software packages are required to execute the demonstrator:
Hardware devices:
    * Parallax 555-28027 PIR motion sensor
    * Omron D6T-1A-02 temperature sensor
    * Raspberry Pi
    * Any device capable of connecting to a router and executing python programs.

Software package:
    * pigpio 
    * smbus2 
    * crcmod
    * omlaxtcp
These can all be installed using the following pip command::

    pip install pigpio smbus2 crcmod omlaxtcp

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
