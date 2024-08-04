import hashlib
import csv

#Step 1: Create a class for the current block and pass in an instance of itself, the hash of the previous block and transaction list
class YPCoinBlock:
    def __init__(self, prevHash, transList):
        #Pass the hash of the previous block information into the current block
        self.prevHash = prevHash 
        self.transList = transList 

        #Concatenate all the transaction in the transaction list using a common seperator and the linking point. I will be using "_"
        #Once concatenated I will to append the previous blocks hash code to the list
        self.blockData = "_".join(transList) + "_" + prevHash

        #To generate a new hash code for the current block, I will use the "haslib" library to perform some 256 bit encoding to the blockData
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()


#Step 2: Retrieve transactions from csv file and assign each transaction to an index in an array
    #Initialise transactions array
    transactions = []

    #Open and read csv file
    with open('transactions.csv', 'r') as transactionsFile:
        csvReader = csv.read(transactionsFile)
        for transaction in csvReader:
            transactions.append(transaction)


#Step 3: Create a block using the class you made earlier, passing in a string, the transactions in the block
initBlock = YPCoinBlock("yoyoy", [transactions[1], transactions[2]])

#Print the contents of the block
print(initBlock.blockData)


    




