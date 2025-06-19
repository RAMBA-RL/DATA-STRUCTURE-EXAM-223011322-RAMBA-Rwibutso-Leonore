Employee Pay Calculator Project

Project Description

This project is my implementation of a C++ employee pay calculator. It shows dynamic arrays, class inheritance, polymorphism, pointer arithmetic, and resizing arrays. The program lets users enter different pay components for an employee and calculates total pay using both fixed and commission-based strategies. All code is fully commented for clarity.

Project Requirements

The requirements were:

1.	Define a struct PayComponent to store each pay component (description and amount) and allocate a dynamic array of these for each employee
   
2.	Create an abstract base class PayCalcBase with a pure virtual compute method
   
3.	Derive two classes (FixedPayCalc and CommissionPayCalc) from PayCalcBase to demonstrate inheritance and polymorphism
   
4.	Store pointers to calculator objects in a dynamic array (PayCalcBase* calculators) and use polymorphic calls to compute pay
   
5.	Use pointer arithmetic to sum amounts in the calculators and to apply commissions
   
6.	Implement addComponent(PayComponent) and removeComponent(int index) by resizing the dynamic array of pay components
   

How I Completed the Project

1. Dynamic Arrays
   
•	The PayComponent struct is used to store each pay item

•	A dynamic array of PayComponent is created based on user input

•	Memory is allocated and freed properly

2. Inheritance & Polymorphism
   
•	An abstract base class PayCalcBase defines the compute interface

•	FixedPayCalc and CommissionPayCalc derive from it and implement their own logic

•	Both classes override the pure virtual compute function

3. Dynamic Calculator Array
   
•	An array of PayCalcBase is created to demonstrate polymorphic calculation

•	Different calculator strategies are stored in the same array

•	Virtual function calls work through base class pointers

4. Pointer Arithmetic
   
•	All calculations in compute functions use pointer arithmetic instead of array indexing

•	The code uses const PayComponent* ptr = comps and increments the pointer with ++ptr

•	This shows how to access array elements through pointer movement

5. Memory Management
   
•	Dynamic memory allocation using new operator

•	Proper cleanup using delete and delete[]

•	All allocated memory is freed before program ends

Code Structure Explanation

PayComponent Structure

struct PayComponent {

    char desc[30];   // Stores description of pay item (like "Salary" or "Bonus")
    
    float amount;    // Stores the money amount for this pay item
};

This simple structure holds information about each part of an employee's pay.

Abstract Base Class

class PayCalcBase {

public:

    virtual float compute(const PayComponent*, int) = 0;  // Pure virtual function
    
    virtual ~PayCalcBase() {}  // Virtual destructor for safe cleanup
};

This is the parent class that defines what all pay calculators must do. The = 0 makes it abstract, so you cannot create 

objects of this class directly.

Fixed Pay Calculator

class FixedPayCalc : public PayCalcBase {

public:

    float compute(const PayComponent* comps, int n) override {
    
        float sum = 0;
        
        const PayComponent* ptr = comps;  // Start pointer at beginning of array
        
        for (int i = 0; i < n; ++i, ++ptr)  // Move pointer through array
        
            sum += ptr->amount;  // Add each amount to total
            
        return sum;
    }
};

This calculator simply adds up all the pay components. It uses pointer arithmetic (++ptr) instead of array indexing 

(comps[i]).

Commission Pay Calculator

class CommissionPayCalc : public PayCalcBase {

    float commission_rate_;  // Stores commission percentage
    
public:

    CommissionPayCalc(float rate = 0.10f) : commission_rate_(rate) {}
    
    float compute(const PayComponent* comps, int n) override {
    
        float sum = 0;
        
        const PayComponent* ptr = comps;  // Start pointer at beginning
        
        for (int i = 0; i < n; ++i, ++ptr)  // Move through array with pointer
        
            sum += ptr->amount;  // Add each amount
            
        return sum + sum * commission_rate_;  // Add commission to total
    }
};

This calculator adds up all components and then adds a commission percentage on top.

Polymorphic Array Usage

PayCalcBase* calculators[2];  // Array of base class pointers

calculators[0] = new FixedPayCalc();  // First calculator type

calculators[1] = new CommissionPayCalc(0.10f);  // Second calculator type

// Use polymorphism to call correct compute method

for (int i = 0; i < 2; ++i) {

    float result = calculators[i]->compute(comps, n_components);
    
    // Each calculator runs its own version of compute()
}

