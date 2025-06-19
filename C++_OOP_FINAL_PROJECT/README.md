Employee Pay Calculator

Project Description

This project is my implementation of a C++ employee pay calculator that demonstrates dynamic arrays, class inheritance, polymorphism, pointer arithmetic, and array resizing. The program allows users to enter different pay components for an employee and calculates total pay using both fixed and commission-based strategies. All code is fully commented for clarity 

Project Requirements

The assignment required implementing the following features:

1.	PayComponent Structure: Define a struct to store each pay component (description and amount) and allocate a dynamic array of these for each employee
2.	Abstract Base Class: Create PayCalcBase with a pure virtual compute method
3.	Inheritance & Polymorphism: Derive FixedPayCalc and CommissionPayCalc classes from PayCalcBase
4.	Dynamic Calculator Array: Store pointers to calculator objects in a dynamic array (PayCalcBase* calculators) and use polymorphic calls
5.	Pointer Arithmetic: Use pointer arithmetic to sum amounts and apply commissions in calculators
6.	Dynamic Array Operations: Implement addComponent(PayComponent) and removeComponent(int index) with array resizing

How the Program Works

1. User Input Phase
   
The program prompts the user to:
•	Enter the number of pay components

•	Provide description and amount for each component

2. Dynamic Memory Allocation

•	Creates a dynamic array of PayComponent structures

•	Allocates memory based on user-specified component count

3. Polymorphic Calculation
   
•	Creates two different calculator objects stored in base class pointers

•	Uses virtual function dispatch to call appropriate calculation methods

4. Results Display
   
•	Shows results from both calculation methods: 

o	Fixed pay (sum of all components)

o	Commission pay (sum + 10% commission)

Code Structure and Annotations

Key Components

PayComponent Structure

struct PayComponent {
    char desc[30];   // Description of pay component (max 29 chars + null terminator)
    float amount;    // Monetary amount for this component
};
Abstract Base Class
class PayCalcBase {
public:
    virtual float compute(const PayComponent*, int) = 0;  // Pure virtual function
    virtual ~PayCalcBase() {}  // Virtual destructor for proper cleanup
};
Derived Calculator Classes
class FixedPayCalc : public PayCalcBase {
    // Sums all pay components using pointer arithmetic
};

class CommissionPayCalc : public PayCalcBase {
    // Sums components and adds commission percentage
};
Pointer Arithmetic Implementation
The code uses pointer arithmetic instead of array indexing:
const PayComponent* ptr = comps;  // Initialize pointer to array start
for (int i = 0; i < n; ++i, ++ptr)  // Increment pointer each iteration
    sum += ptr->amount;  // Access amount through pointer
Polymorphic Dispatch
PayCalcBase* calculators[2];  // Array of base class pointers
calculators[0] = new FixedPayCalc();
calculators[1] = new CommissionPayCalc(0.10f);

// Polymorphic function calls
calculators[i]->compute(comps, n_components);

