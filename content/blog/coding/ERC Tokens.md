Title: Setting Up ERC Standard Tokens
Date: 2018-06-10
Category: Coding
Tags: webdev, ethereum, javascript, blockchain
Slug: setup-erc-token
Authors: Adam Li
Summary: A short walkthrough of setting up an ethereum token.

# Getting Setup with Ethereum
# By: Adam Li
### Table of Contents
<!-- MarkdownTOC -->

- Installation
- Set Up
    - 1. Creating Your Project Directory
        - 1b. Project Directory
    - 2. Contracts and FrontEnd
- Implementation
    - ERC Standards
        - 1. ERC20
        - 2. ERC721
- Testing
    - 1. Remix \(http://remix.ethereum.org/\)
    - 2. Ropsten Test Network \(https://ropsten.etherscan.io \)
    - 3. Javascript Truffle Tests
    - 4. Metamask and Ganache
- Deployment
    - 1. truffle.js \(http://truffleframework.com/docs/advanced/configuration\)
    - 2. Crowdsalable Ethereum Token
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

# Set Up
## 1. Creating Your Project Directory

    mkdir MyToken && cd MyToken
    truffle init
    npm init -y
    npm install -E zeppelin-solidity

This will install zeppelin-solidity for testing code and initialize your project directory using truffle.s

### 1b. Project Directory
- contracts: this is your directory for any solidity contracts
- migrations: this is your directory for scriptable deployment files (how do we want to release the functionality of our entire project?)
- test: for testing your entire application
- truffle.js: a configuration file for truffle

## 2. Contracts and FrontEnd
Next, you need to implement your contracts and frontend to create your unique token(s).

# Implementation
## ERC Standards
### 1. ERC20
Requirements for it are:
- The Token’s Name
- The Token’s Symbol
- The Token’s Decimal Places
- The Number of Tokens in Circulation
- balanceOf 
- allowance
- approve 
- transferFrom

It also defines two events: Transfer and Approval .

### 2. ERC721
These are tokens that are non-fungible. One token does not necessarily equal another. It is slightly more complicated then the erc20 token.

The standard defines the functions:
- name 
- symbol 
- totalSupply 
- balanceOf 
- ownerOf 
- approve 
- takeOwnership 
- transfer 
- tokenOfOwnerByIndex
- tokenMetadata 

It also defines two events: Transfer and Approval .

# Testing
## 1. Remix (http://remix.ethereum.org/)
You can test using a web tool (solidity online compiler), hosted by the Ethereum foundation: http://remix.ethereum.org/.

You can easily test contract functionality, but beware you can't test your whole dapp functionality, so there could be bugs in synchronizing the front/back end with the contracts.

## 2. Ropsten Test Network (https://ropsten.etherscan.io )
Using remix, or another tool to deploy your contract, you can check basic outputs here on the test network.

## 3. Javascript Truffle Tests
These will be customized test suites that you write in the truffle directory.

    npm i ethereumjs-tx
    truffle develop
    truffle(develop)> test

This command will install the ethereum-tx package, boot a test blockchain using truffle and then run all tests within "/test/" directory.

## 4. Metamask and Ganache
This is a blockchain utility web app that can run in your web2.0 browser. It can help debug your entire dapp.

Ganache is a personal Ethereum development network that runs on your computer.  Using Ganache you can quickly see how your application affects the blockchain, and introspect details like your accounts, balances, contract creations and gas costs. 

# Deployment
## 1. truffle.js (http://truffleframework.com/docs/advanced/configuration)
Inside your truffle.js file, you'll find the line module.exports. You can modify the contents of this json object, to manage your deployment testing.

- networks: Specifies which networks are available for deployment during migrations, as well as specific transaction parameters when interacting with each network (such as gas price, from address, etc.). 
    
    - name: development, test, ropste, live, etc.
    - (options): gas, gasPrice, from, provider

- providers: Specifies the local test network. Make sure you wrap truffle-hdwallet providers in a function closure as shown below to ensure that only one network is ever connected at a time.

    networks: {
      ropsten: {
        provider: function() {
          return new HDWalletProvider(mnemonic, "https://ropsten.infura.io/");
        },
        network_id: '3',
      },
      test: {
        provider: function() {
          return new HDWalletProvider(mnemonic, "http://127.0.0.1:8545/");
        },
        network_id: '*',
      },
    }

- contracts_build_directory: for where to build the contracts into byte code.
- mocha: configuration options for mochajs testing framework.

You can create an ethereum mnemonic and set it, so your providers can see it within the config file. Here is an example of 

    truffle migrate --network ropsten

## 2. Crowdsalable Ethereum Token

    mkdir crowdsalable-eth-token && cd crowdsalable-eth-token
    truffle unbox git@github.com:ajb413/crowdsalable-eth-token.git


# References:
1. https://medium.com/@ConsenSys/a-101-noob-intro-to-programming-smart-contracts-on-ethereum-695d15c1dab4
2. https://medium.com/@mvmurthy/full-stack-hello-world-voting-ethereum-dapp-tutorial-part-1-40d2d0d807c2
3. http://truffleframework.com/docs/getting_started/project#exploring-the-project
4. https://www.pubnub.com/blog/testing-and-deploying-an-ethereum-token-part-2/
