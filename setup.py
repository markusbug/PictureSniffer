from setuptools import setup, find_packages
import os
os.system("pip install numpy")
os.system("pip install scipy")
os.system("yum install opencv-python")
os.system("mkdir pictures")
os.system("mkdir faces")
setup(
    name="ARPSpoofer",
    version="0.1",
    packages=find_packages(),
    scripts=['bin/MailSniffer'],
)