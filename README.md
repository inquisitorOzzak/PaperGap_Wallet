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

If using Pycharm.
The .idea file will contain all required dependancy/interpreter information for running both the kivy and bitcoin libraries/code.
If using another platform to view code,you  may need to use a language-agnostic package manager such as Conda or Pip.
Will be running on a USB linux distribution


### Built With

* [Kivi](https://kivy.org/#home) - The  Python Frontend framework used
* [Bitcoin Tool](https://github.com/primal100/pybitcointools) - Bitcoin wallet code
* [Linux Distro](http://linuxfromscratch.org/lfs/view/stable/index.html) - Linux Distro Information

### Progress Of Project
#### Frontend
Skeletal UI has been implemented for all required views. Will now be working on integrating the UI into the bitcoin wallet code, so a demo of the project can be delivered
in the near future.

#### Bitcoin wallet code
The first draft of the mnemonic generator has been created. Now working towards completing the wallet restoration feature of app.

#### Linux Distro
A test version of distro is already up and running with all network interfaces disabled. Will be working towards integrating the dependency sizes into the distro.


