# Blockchain Simulation in Python

This project is a beginner-friendly implementation of a **blockchain** using Python. It simulates the core features of a blockchain such as creating blocks, adding transactions, mining, and validating the chain for integrity.

---

## 🛠️ Features
1. **Genesis Block**: Automatically creates the first block of the blockchain.
2. **Add Transactions**: Add custom transactions to a pending pool.
3. **Mine Blocks**: Uses a **proof-of-work (PoW)** mechanism to find a valid hash for the block.
4. **Validate Blockchain**: Checks the integrity of the blockchain and identifies tampering.
5. **Display Blockchain**: Print the entire blockchain in a readable format.

---

## 🔑 Key Concepts Covered
- **Blockchain Basics**: 
  - Blocks contain transactions, timestamps, hashes, and a reference to the previous block.
  - Uses a nonce to achieve PoW.
- **Proof of Work**:
  - A mining process that ensures block hashes meet a specific difficulty level.
- **Hash Verification**:
  - Each block's hash depends on its data, nonce, and previous block's hash.
- **Tamper Detection**:
  - Any alteration to a block's data or hash invalidates the blockchain.

---

## 📝 Project Workflow
1. **Add Transactions**:
   - Use the `addTransaction()` function to add a list of pending transactions.
2. **Create and Mine Blocks**:
   - The `createNewBlock()` function mines a block and appends it to the chain.
3. **Display Blockchain**:
   - Visualize the entire blockchain with the `displayChain()` function.
4. **Validate Blockchain**:
   - Check if the blockchain is valid with the `validateChain()` function.

---

## 🧩 Code Structure
### Classes
- `Block`: Represents a block in the blockchain.
  - Attributes: `idx`, `timestamp`, `transactions`, `prevHash`, `curHash`, `nonce`.
  - Methods: `calcHash()`.
- `Blockchain`: Manages the blockchain.
  - Attributes: `chain`, `difficulty`, `pendingTransactions`.
  - Methods: `createGenesisBlock()`, `getLatestBlock()`, `addBlock()`, `mineBlock()`, `addTransaction()`, `createNewBlock()`, `validateChain()`, `displayChain()`.

---

## 🛠️ Installation and Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/divyatapandey/BockChain-Simulation.git
   cd BockChain-Simulation
2. Run the script:
   ```bash
   python blockchain.py

3. Observe the blockchain simulation, including transactions, mining, and validation.
## 💡 Highlights

- **Beginner-friendly implementation**: Focuses on simplicity without compromising key blockchain principles.
- **Clear display of tamper detection**: Demonstrates how even minor tampering breaks the chain's integrity.
- **Dynamic transaction management**: Allows custom transactions to be mined into new blocks.

## 📖 Example Output
Mining block #1...
Block mined successfully! Nonce:13,Hash:0035903a88bb6fa332dc2962f6b96b17b53d8eefd61ace71aea4ed2c8ac13595
{
    "idx": 0,
    "timestamp": 1737726724,
    "transactions": "Genesis Block",
    "prevHash": "0",
    "nonce": 0,
    "curHash": "edcfe6ff5274e798fce69b8ed6cbb5e9e1d8fbee81e65f4b51db1079a1e53929"
}
--------------------------------------------------
{
    "idx": 1,
    "timestamp": 1737726724,
    "transactions": [
        {
            "from": "Divya",
            "to": "Soumya",
            "amount": 27
        },
        {
            "from": "Soumya",
            "to": "Ritu",
            "amount": 18
        }
    ],
    "prevHash": "edcfe6ff5274e798fce69b8ed6cbb5e9e1d8fbee81e65f4b51db1079a1e53929",
    "nonce": 13,
    "curHash": "0035903a88bb6fa332dc2962f6b96b17b53d8eefd61ace71aea4ed2c8ac13595"
}
--------------------------------------------------
Blockchain is valid.
Blockchain is valid.

## 🚀Future Improvements
-Add support for multiple nodes to simulate a decentralized network.
-Implement digital signatures for secure transaction validation.
-Extend the mining process to include rewards.

🤝 Contribution
Feel free to fork the repository and submit pull requests for improvements or additional features.



