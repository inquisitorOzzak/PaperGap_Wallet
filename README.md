## Team12 Project
# PaperGap_Wallet

Secure Live-Boot Environment For Bitcoin Paper Wallet Generation
This app creates a live bootable USB linux distribution. When booted shows a simplstic one-app system, completely air-gapped with no networking intefaces
and no desktop environment. A simplistic UI created using Pythons frontend framework Kivi will help the user create/restore a valid bitcoin wallet in the 
simplest and easiest way possible, while being completely secure at the same time.

### Authors
```
Ozzak Matic
Oliver Cunnington
Robert O'Brien
John Furlong
Janine Dunlea
```

### Prerequisites

* [Installing Python](https://www.python.org/downloads/) - Installing Python
* [Kivi Install Pycharm](https://www.youtube.com/watch?v=RYF73CKGV6c&list=PLhTjy8cBISEpobkPwLm71p5YNBzPH9m9V) - Installing Kivy On Pycharm
* [Kivi Install Windows](https://kivy.org/doc/stable/installation/installation-windows.html) - Installing Kivy On Windows
* [Kivi Install Other Platforms](https://kivy.org/doc/stable/gettingstarted/installation.html) - Installing Kivy on all other platforms (including linux, mac, pip, conda etc)
* [Bitcoin Library Install](https://github.com/primal100/pybitcointools) - Installing Bitcoin tools (see Readme on Linked github page)



Will be running on a USB linux distribution


### Built With

* [Kivi](https://kivy.org/#home) - The  Python Frontend framework used
* [Bitcoin Tool](https://github.com/primal100/pybitcointools) - Bitcoin wallet code
* [Linux Distro](http://linuxfromscratch.org/lfs/view/stable/index.html) - Linux Distro Information

### Progress Of Project
#### Frontend
Frontend fully integrated with bitcoin library code. Now working towards PDF generation and Unit testing.

#### Bitcoin wallet code
Wallet restoration feature implemented, focusing on adding other kinds of crypto wallets.

#### Linux Distro
A test version of distro is already up and running with all network interfaces disabled. Will be working towards integrating the dependency sizes into the distro.


