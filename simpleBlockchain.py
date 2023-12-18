from flask import Flask, jsonify, request
import hashlib
import json
from time import time

class simpleBlockchain:
    def __init__(self):
        self.chain = []
        self.currentTransactions = []
        self.newBlock(previousHash='1', proof=100)

    def newBlock(self, proof, previousHash=None):
        block = {
            'index':len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.currentTransactions,
            'proof': proof,
            'previousHash': previousHash or 
                self.hash(self.chain[-1]) if self.chain else None,
        }
        self.currentTransactions = []
        self.chain.append(block)
        return block
    
    def newTransaction(self,sender, recipient, amount):
        self.currentTransactions.append({
            'sender':sender,
            'recipient':recipient,
            'amount': amount,
        })
        return self.lastBlock['index']+1
    
    @staticmethod
    def hash(block):
        blockString = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(blockString).hexdigest()
        
app = Flask(__name__)
blockchain = simpleBlockchain()

@app.route('/mining', methods=['GET'])
def mining():
    proof = 1
    previousHash = simpleBlockchain.hash(simpleBlockchain.last_block)
    simpleBlockchain.newTransaction(sender="0",recipient="address1", amount=1)
    block = simpleBlockchain.newBlock(proof, previousHash)
    response = {
        'message': "new block forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previousHash': block['previousHash'],
    }
    return jsonify(response),200

@app.route('/chain', methods=['GET'])
def fullChain():
    response={
        'chain': simpleBlockchain.chain,
        'length': len(simpleBlockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)