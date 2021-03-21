
## Team12 Project
# PaperGap_Wallet

___________________

<summary><h3 style="display: inline-block">Table of Contents</h3></summary>
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

___________________
### Abstract

Secure Live-Boot Linux Environment For Bitcoin Paper Wallet Generation

This app creates a live bootable USB linux distribution. When booted shows a simplstic one-app system, completely air-gapped with no networking intefaces
and no desktop environment. A simplistic UI created using Pythons frontend framework Kivi will help the user create/restore a valid bitcoin wallet in the 
simplest and easiest way possible, while being completely secure at the same time.

- **NOTE:** Unfortunately our custom Linux distribution is not ready for deployment as the scope of our project was too large. So we are releasing the application as a standalone Windows app. 
  It all works as intended, same as the other Paper Wallet Generators out there, it's just the superb security aspect of our project that's lacking.

### Authors

- Ozzak Jure Matic
- Oliver Cunnington
- Robert O'Brien
- John Furlong
- Janine Dunlea


### Prerequisites

* [Installing Python](https://www.python.org/downloads/) - Installing Python
* [Kivi Install Pycharm](https://www.youtube.com/watch?v=RYF73CKGV6c&list=PLhTjy8cBISEpobkPwLm71p5YNBzPH9m9V) - Installing Kivy On Pycharm
* [Kivi Install Windows](https://kivy.org/doc/stable/installation/installation-windows.html) - Installing Kivy On Windows
* [Kivi Install Other Platforms](https://kivy.org/doc/stable/gettingstarted/installation.html) - Installing Kivy on all other platforms (including linux, mac, pip, conda etc)
* [Bitcoin Library Install](https://github.com/primal100/pybitcointools) - Installing Bitcoin tools (see Readme on Linked github page)




### Built With

* [Kivi](https://kivy.org/#home) - The  Python Frontend framework used
* [pybitcointools](https://github.com/primal100/pybitcointools) - Python library for interaction with Bitcoin network 
* [Linux From Scratch](http://linuxfromscratch.org/lfs/view/stable/index.html) - Linux Distro Builder manual used as the template for our custom distro





___________________

# User Guide

## Installation

- **ONLY WORKS ON WINDOWS**

The installation assumes that:

-  _Python 3_ or above is already installed on your machine

-  An up to date version of _Pip_ is also available on your machine

-  As referenced before your machine running on a working _Windows_ operating system

-  A stable internet connection is present

### Instructions
First extract the zipped file as provided

<a href="https://ibb.co/KF4cLgL"><img src="https://i.ibb.co/r48Kchc/Extract-Image.png" alt="Extract-Image" border="0"></a>

Navigate to the extracted folder. 

You should see the following files:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/FXzMP01/Project-Files.png" alt="Project-Files" border="0"></a>

- Then double click on the Windows Batch File called `runscript`


If a red warning comes up, simply allow the file to run.

Following this a `cmd` terminal window will show up and 
the script will install all needed dependencies and run the project for you.

If you need to re-run the app, no need to run the Batch script again, just double click `main.py`


___________________

## Application walk-through

### Step 1
Upon running the app you will land on our "welcome page" there are 3 options to choose from here:

1. **Create a New Wallet**: choose this one if you are first time user and don't have an existing wallet seed. If you choose this option go to Step 2

2. **Restore Previous Wallet**: choose this one if you already have a seed and wish to generate more addresses from the same seed. If you choose this option go to Step 4

3. **Reset App**: if you need to generate another seed 

<a href="https://ibb.co/7VZLv6H"><img src="https://i.ibb.co/bLCD18x/HomePage.png" alt="HomePage" border="0"></a>

### Step 2
- Now you need to specify what type of wallet/seed you wish to generate.

There are three dropdown menus: 


  1. **Coin Type**: only Bitcoin works at the moment

  2. **Word Number**: there are 4 options: 12, 16, 20 and 24. We recommend using **24 words** as the safest option. Alternatively if you are using some of the older wallets as your hot wallet choose 12 words. (like Electrum for example).
  
  3. **Mnemonic Language**: there are 3 options: English, Spanish and French. Pick one you are most comfortable with.

After choosing the options click **Generate Wallet** and go to Step 3

<a href="https://ibb.co/ChtgTfY"><img src="https://i.ibb.co/PwYKfdP/Create-AWallet.png" alt="Create-AWallet" border="0"></a>

### Step 3

This step is **VERY important.** Your "recovery phrase" represents your seed which is used to generate your PRIVATE keys.

Your PRIVATE keys need to be PRIVATE and kept a secret!

**Do not** enter them on any machine with network access.

**Do not** lose them (you will lose your Bitcoin).

**Do not** share them with anyone.

Use **pen and paper** to write down the seed by hand. And **store the paper** in a safe and dry place.


<a href="https://ibb.co/dBfgTcQ"><img src="https://i.ibb.co/cJyLBvN/Mnemonic-Generation-Page.png" alt="Mnemonic-Generation-Page" border="0"></a>

Example:

<a href="https://ibb.co/Hqrkdw8"><img src="https://i.ibb.co/yq8bSvj/seed.jpg" alt="seed" border="0"></a>

After writing down the seed tick the box *"I have safely stored my recovery phrase offline"* and click **Continue to Wallet** and go to Step 4

- Note: if you have want different words go back to Step 1 and click Reset App to start over

### Step 4

Here you will need to enter the seed you just wrote down back to the application to confirm that you stored it correctly.
After clicking **Submit Phrase** if you entered the seed correctly the application will forward you to the next screen, and go to Step 5

- If you didn't generate the seed now (steps 2 and 3) but are using previously generated seed (came here from step 1) enter that previously generated seed now.


<a href="https://ibb.co/TkCjKmw"><img src="https://i.ibb.co/MsXw8Mg/Confirm-Mnemonic-Page.png" alt="Confirm-Mnemonic-Page" border="0"></a>

### Step 5

At this stage we are almost there. The applicaton will offer you to choose the number of PUBLIC addresses asociated with the PRIVATE seed/key you provided.

Public addresses will be stored in a .pdf file and are safe to share.

You will use them to send Bitcoin to your wallet.

We recommend choosing 50 or 100 to increase privacy (use different one every time you send yourself Bitcoin)


After choosing a number of addresses tick *"Add QR code"* box for future convinience. And enter a name/label for your waller (example "TestWallet1")

<a href="https://ibb.co/NVNR5Kh"><img src="https://i.ibb.co/f1NJfHR/Create-PDF.png" alt="Create-PDF" border="0"></a>


### Step 6

A scrolldown summary of all your adresses will be shown
you are free to observe and then return to home to perform another action or simply close the app.

- You will be able to download your PDF wallet from your local filespace.

<a href="https://ibb.co/YddQmpj"><img src="https://i.ibb.co/0992ThJ/PDFPreview-Page.png" alt="PDFPreview-Page" border="0"></a>

- You will be able to download your PDF wallet from your local filespace.

### Step 7

Final result is composed of two items:

1. your hand written seed (12-24 words) that you need to keep private and secure (you can find the example in Step 3)

2. your public keys .pdf file that you use to send yourself Bitcoin (this is safe to share with other people)

Example:

<a href="https://ibb.co/VwTfJ10"><img src="https://i.ibb.co/BnB0cpH/Sample-Wallet.png" alt="Sample-Wallet" border="0"></a>

