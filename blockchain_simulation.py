import hashlib
import time
import json

#Block class
class Block:
    def __init__(self,idx,timestamp,transactions,prevHash):
        self.idx=idx
        self.timestamp=timestamp
        self.transactions=transactions
        self.prevHash=prevHash
        self.nonce=0  #Used for mining
        self.curHash=self.calcHash()

    def calcHash(self):
        #Combine block data into a single string
        blockData = (
            str(self.idx) +
            str(self.timestamp) +
            json.dumps(self.transactions) +
            self.prevHash +
            str(self.nonce)
        )
        #Generate a hash from the block data
        return hashlib.sha256(blockData.encode('utf-8')).hexdigest()


#Blockchain class
class Blockchain:
    def __init__(self):
        self.chain=[self.createGenesisBlock()] #Start with the genesis block
        self.difficulty=2 #Difficulty level for mining
        self.pendingTransactions=[] #Transactions waiting to be added to a block

    #Create the first block in the chain
    def createGenesisBlock(self):
        return Block(0, int(time.time()),"Genesis Block","0")

    #Get the last block in the chain
    def getLatestBlock(self):
        return self.chain[-1]

    #Add a mined block to the chain
    def addBlock(self,block):
        self.chain.append(block)

    def mineBlock(self,block):
        print(f"Mining block #{block.idx}...")
        while True:
            #Keep trying different nonces until the hash starts with the required number of zeros
            block.curHash=block.calcHash()
            if block.curHash[:self.difficulty]=='0'*self.difficulty:
                print(f"Block mined successfully! Nonce:{block.nonce},Hash:{block.curHash}")
                return
            block.nonce+=1

    def addTransaction(self,transaction):
        self.pendingTransactions.append(transaction)

    #Create,mine,and add a new block to the chain
    def createNewBlock(self):
        newBlock=Block(
            idx=self.getLatestBlock().idx+1,
            timestamp=int(time.time()),
            transactions=self.pendingTransactions,
            prevHash=self.getLatestBlock().curHash,
        )
        self.mineBlock(newBlock) #Mine the block before adding it
        self.addBlock(newBlock)
        self.pendingTransactions=[] #Clear pending transactions

    #Check the integrity of the blockchain
    def validateChain(self):
        for i in range(1,len(self.chain)):
            curBlock = self.chain[i]
            prevBlock = self.chain[i-1]
            #Verifying hash
            if curBlock.curHash != curBlock.calcHash():
                return f"Tampered Block #{curBlock.idx}"

            if curBlock.prevHash != prevBlock.curHash:
                return f"Broken Link at Block #{curBlock.idx}"
        return "Blockchain is valid."

    def displayChain(self):
        for block in self.chain:
            print(json.dumps(block.__dict__,indent=4))
            print("-"*50)



if __name__ == "__main__":
    blockchainSim = Blockchain()
    #Add transactions
    blockchainSim.addTransaction({"from":"Divya","to":"Soumya","amount":27})
    blockchainSim.addTransaction({"from":"Soumya","to":"Ritu","amount":18})

    blockchainSim.createNewBlock() #Create and mine a new block
   
    blockchainSim.displayChain() #Display blockchain
   
    print(blockchainSim.validateChain()) #Validate blockchain

    #Tamper with a block
    blockchainSim.chain[1].transactions=[{"from": "Divya", "to": "Dinesh", "amount":11}]
    blockchainSim.chain[1].curHash=blockchainSim.chain[1].calcHash()

    print(blockchainSim.validateChain())  #Validate blockchain after tampering
