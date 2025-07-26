class BankAccount {
  #accountHolder;   
  #balance;    

  constructor(accountHolder, initialBalance = 0) {
    this.#accountHolder = accountHolder;
    this.#balance = initialBalance;
  }

  credit(amount) {
    if (amount > 0) {
      this.#balance += amount;
      console.log(`₹${amount} credited successfully.`);
    } else {
      console.log("Invalid amount. Credit failed.");
    }
  }

  getBalance() {
    return this.#balance;
  }

  getAccountHolder() {
    return this.#accountHolder;
  }
}


const account = new BankAccount("Hema", 5000);
console.log("Initial Balance:", account.getBalance());

account.credit(1500); 
console.log("Updated Balance:", account.getBalance());

account.credit(-200); 