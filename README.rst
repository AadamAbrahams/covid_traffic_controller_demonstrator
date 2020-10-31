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
The following list of hardware devices and software packages are required to execute the demonstrator.

Hardware devices:
    * Parallax 555-28027 PIR motion sensor (It would be possible to use any PIR motion sensor that has a single output pin, and that outputs 1 when triggered and 0 while untriggered).
    * Omron D6T-1A-02 temperature sensor
    * Raspberry Pi
    * Any device capable of connecting to a router and executing python programs.

Software packages:
    * pigpio 
    * smbus2 
    * crcmod
    * omlaxtcp
These can all be installed using the following pip command::

    pip install pigpio smbus2 crcmod omlaxtcp

At a minimum, devices may communicate over the Local Area Network. If the user wishes to exchange data between devices over the internet, the device acting as the server is required to have its router port forwarding, on the relevant socket port, to the device in question.

Quick Usage
-----
**Step 1**
Connect the hardware modules in accordance to the circuit diagram below:

**Step 2**
Execute the following line of code on the device that is acting as a server::

    python server.py

**Step 3**
Determine the IP address of the server device.

**Step 4**
Execute the following line of code on the device that is acting as a client::

    sudo pigpiod
    
Followed by::

    python client.py HostIP
    
where HostIP is the IP address of the server device.
    
**Complete**
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
