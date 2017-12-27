Title: Setting Up Ethereum 
Date: 2017-12-21
Category: Coding
Tags: webdev, ethereum, python, javascript
Slug: setup-ethereum
Authors: Adam Li
Summary: A short walkthrough of setting up an ethereum dAPP
status: draft

# Getting Setup with Ethereum
# By: Adam Li
### Table of Contents
<!-- MarkdownTOC -->

- Installation
- Setting Up Ethereum
    - 1. Setting Up a Node \(For Testing\):
    - 2. Modifying Migrations and Adding New Contracts
- 
    - 3. Creating Smart Contracts \(General\)
    - 4. General Thoughs on Ethereum
- References:

<!-- /MarkdownTOC -->

pragma solidity ^0.4.18;
web3@1.0.0-beta.27
truffle@4.0.4 
solc@0.4.19 
ethereumjs-testrpc@6.0.3 

# Installation
The following packages need to be installed for a test time environment:
* testrpc
* web3js
* solc
* truffle

    npm install ethereumjs-testrpc web3
    npm install solc
    npm install -g truffle

- Testrpc is an in-memory blockchain that can be used to test the development of the application.
- Web3 is essentially the web interface with the backend and frontend.
- Solc is a solidity code compiler
- Truffle is a web framework for building dAPPs using Ethereum

# Setting Up Ethereum
## 1. Setting Up a Node (For Testing):
You can either set up a node that fully connects to the ethereum network, or connect to a test node to test application development! Very cool, so we will probably start with testrpc to run a test client node.

    testrpc

In order to deploy, you need to setup a file directory. For those familiar with express for node.js and any other web framework, this is very similar.

    truffle init

Next, tell truffle how to deploy. You'll need to modify the truffle.js file.
    
    module.exports = {
      // See <http://truffleframework.com/docs/advanced/configuration>
      // to customize your Truffle configuration!
        networks: {
        development: {
            host: "localhost",
            port: 8545,
            network_id: "*", // match any network id
            gas: 4600000    // to ensure your test node has a lot of gas to run
        }
      }
    };

Then you can run

    truffle deploy

You should not see any errors at this point.

## 2. Modifying Migrations and Adding New Contracts
Any new contracts you write will go in the /contracts/ direcotry, and then the corresponding requirements need to be loaded in the /migrations/ directory. There is boiler code there that shows you how to add things.

#

## 3. Creating Smart Contracts (General)

## 4. General Thoughs on Ethereum
So it seems that ethereum is great for creating sets of smart contracts, but there will need to be platforms that are optimized for specific technologies built on top of smart contracts.

For example, Golem

# References:
1. https://medium.com/@ConsenSys/a-101-noob-intro-to-programming-smart-contracts-on-ethereum-695d15c1dab4
2. https://medium.com/@mvmurthy/full-stack-hello-world-voting-ethereum-dapp-tutorial-part-1-40d2d0d807c2
3. 
