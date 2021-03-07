
## Team12 Project
# PaperGap_Wallet


<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#abstract">Abstract</a></li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#user-guide">User Guide</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#application-walk-through">Application walk-through</a></li>
      </ul>
    </li>
  </ol>
</details>

### Abstract

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






# User Guide

## Installation

**Note: This manual install is only for the beta release, as later in production,
we will have containerized the app within an air-gapped distro, this is still
currently in production, for now, just to demo our product we will require that all
dependencies be installed manually.**


Before we get into the core installations, please ensure you have the latest version of
**Python** ​installed, as well as a somewhat updated version of ​ **pip**
You can check if you have the latest versions of both installed with the following.
**_python --version
pip --version_**


If you have not got python installed follow the simplistic tutorial at this link, please
ensure python is also on your ​ **PATH** ​environment variables.

Note: In theses examples ​ **_python_** ​on its own is used to run python commands, if this
does not work try replacing ​ **_python_** ​with ​ **_python3_** ​in the command line

Likewise if ​ **_pip_** ​itself does not work on the command line than ​ **_pip3_** ​is the version
installed on your machine and you should use that.
[install python](https://www.youtube.com/watch?v=UvcQlPZ8ecA&t=51s)

To update/install pip please run this command in terminal​ _(you can ignore if you already
have pip installed)_
**_python3 -m pip install --upgrade pip_**

Provided in the submission is a zipped folder containing all raw files/directories needed
to run the project.

- Please extract the zipped file into a directory of your choice.
- Open up your terminal and locate the ​ **PaperGap_Wallet-BetaTest** ​directory
- If you have not already ‘​ **cd** ​ _’_ ​ into this directory
- To ensure your in the right place type ‘​ **_ls’_** ​ , the following files should present
    themselves
    
       **- app derived_addresses.txt main.py README.md**
       
Next we will create the virtual environment.


First make sure that you have the virtual environment library installed. Run the following
command...

**_pip install virtualenv_**

To create the virtual environment type the following command into the terminal (ensure
you are in the correct directory as listed above)

**_python -m virtualenv venv_**

Next we will activate the virtual environment by typing the following
For Windows:

**_venv\Scripts\activate_**

For bash:
**_Source venv/Scripts/activate_**

For Linux
**_venv/bin/activate_**

You should see something like this in your terminal...
**(venv)**

Finally we can install the dependencies, each command must be run one by one. I
recommend typing in each command individually so that no small errors are made.
These commands will install our crypto libraries.

**_pip install bitmerchant_**

**_pip install cryptos_**

These commands will install our QR code and PDF generators
**_pip install qrcode[pil]_**

 **_pip install Pillow_**
 
pip install reportlab_**

And this command will install our GUI Kivy, the most important part!

**_python -m pip install kivy[full]_**

Finally we can now run the app with this command...


**_python main.py_**





## Application walk-through

### Step 1
Upon running the app you will land on our "welcome page" there are only 2 options to choose from here
1. **Create a New Wallet**: choose this one if you are first time user and don't have an existing wallet seed. If you choose this option go to Step 2
2. **Restore Previous Wallet**: choose this one if you already have a seed and wish to generate more addresses from the same seed. If you choose this option go to Step 4

<a href="https://ibb.co/XbZ2HLS"><img src="https://i.ibb.co/6mRnQwg/1.png" alt="1" border="0"></a>

### Step 2
Now you need to specify what type of wallet/seed you wish to generate.
There are three dropdown menus: 
1. **Coin Type**: only Bitcoin works at the moment
2. **Word Number**: there are 4 options: 12, 16, 20 and 24. We recommend using **24 words** as the safest option. Alternatively if you are using some of the older wallets as your hot wallet choose 12 words. (like Electrum for example).
3. **Mnemonic Language**: there are 3 options: English, Spanish and French. Pick one you are most comfortable with.

After choosing the options click **Generate Wallet** and go to Step 3

<a href="https://ibb.co/LrRRHqF"><img src="https://i.ibb.co/XDLLMdQ/image.png" alt="image" border="0"></a>


### Step 3

This step is **VERY important.** Your "recovery phrase" represents your seed which is used to generate your PRIVATE keys.

Your PRIVATE keys need to be PRIVATE and kept a secret!

**Do not** enter them on any machine with network access.

**Do not** lose them (you will lose your Bitcoin).

**Do not** share them with anyone.

Use **pen and paper** to write down the seed by hand. And **store the paper** in a safe and dry place.


<a href="https://ibb.co/HV25DT3"><img src="https://i.ibb.co/7XzsJtL/image.png" alt="image" border="0"></a>

Example:

<a href="https://ibb.co/Hqrkdw8"><img src="https://i.ibb.co/yq8bSvj/seed.jpg" alt="seed" border="0"></a>

After writing down the seed tick the box *"I have safely stored my recovery phrase offline"* and click **Continue to Wallet** and go to Step 4

### Step 4

Here you will need to enter the seed you just wrote down back to the application to confirm that you stored it correctly.
After clicking **Submit Phrase** if you entered the seed correctly the application will forward you to the next screen, and go to Step 5

- If you didn't generate the seed now (steps 2 and 3) but are using previously generated seed (came here from step 1) enter that previously generated seed now.


<a href="https://ibb.co/mtGzymZ"><img src="https://i.ibb.co/XpbJ590/20.png" alt="20" border="0"></a>


### Step 5

At this stage we are almost there. The applicaton will offer you to choose the number of PUBLIC addresses asociated with the PRIVATE seed/key you provided.

Public addresses will be stored in a .pdf file and are safe to share.

You will use them to send Bitcoin to your wallet.

We recommend choosing 50 or 100 to increase privacy (use different one every time you send yourself Bitcoin)
<a href="https://ibb.co/sC2hYbn"><img src="https://i.ibb.co/w7RTmBV/image.png" alt="image" border="0"></a>


After choosing a number of addresses tick *"Add QR code"* box to the wallet easier to use. And enter a name/label for your waller (example "MyPaperWallet_01")


<a href="https://ibb.co/pbjd9Sd"><img src="https://i.ibb.co/tQpDW9D/image.png" alt="image" border="0"></a>

### Step 6

A scrolldown summary of all your adresses will be shown
you are free to observe and then return to home to perform another action or simply close the app.
You will be able to download your PDF wallet from your local filespace.

<a href="https://ibb.co/DGjyngy"><img src="https://i.ibb.co/N1GPznP/image.png" alt="image" border="0"></a>

### Step 7

Final result is composed of two items:
1. your hand written seed (12-24 words) that you need to keep private and secure (you can find the example in Step 3)
2. your public keys .pdf file that you use to send yourself Bitcoin (you can also share it with other people)

Example:

<a href="https://ibb.co/4Z98R18"><img src="https://i.ibb.co/kgk42m4/wallet.png" alt="wallet" border="0"></a>

There are still issues with the screen transitions of the GUI that will be fixed over time.

