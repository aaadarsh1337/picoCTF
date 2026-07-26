pragma solidity ^0.6.12;

contract IntOverflowBank {
    mapping(address => uint256) public balances;
    address public owner;
    string private flag;
    bool public revealed;

    event Deposit(address indexed who, uint256 amount);
    event Withdraw(address indexed who, uint256 amount);
    event FlagRevealed(string flag);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner");
        _;
    }

    constructor() public {
        owner = msg.sender;
        revealed = false;
    }

    function setFlag(string memory _flag) external onlyOwner {
        flag = _flag;
    }

    function deposit(uint256 amount) external {
        uint256 oldBalance = balances[msg.sender];
        balances[msg.sender] = balances[msg.sender] + amount;

        emit Deposit(msg.sender, amount);
        if (!revealed && balances[msg.sender] < amount) {
            revealed = true;
            emit FlagRevealed(flag);
        }
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender] - amount;
        emit Withdraw(msg.sender, amount);
    }

    function getFlag() external view returns (string memory) {
        require(revealed, "Flag not revealed yet");
        return flag;
    }
}