#!/bin/bash
# Install Python and dependencies
apt-get update
apt-get install -y python3 python3-pip

# Install Python packages
pip3 install numpy pandas scikit-learn

# Install Node.js dependencies
npm install