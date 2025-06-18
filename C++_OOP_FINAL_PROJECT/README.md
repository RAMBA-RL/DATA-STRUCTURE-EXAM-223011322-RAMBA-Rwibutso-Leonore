 93.EMPLOYEE PAY CALCULATOR PROJECT 
1.	PROJECT DESCRIPTION
This project is my implementation of a C++ employee pay calculator. It demonstrates dynamic arrays, class inheritance, polymorphism, pointer arithmetic, and resizing arrays. The program lets users enter different pay components for an employee and calculates total pay using both fixed and commission-based strategies. All code is fully commented for clarity.
1.1.	Dynamic Arrays:
   - The PayComponent struct is used to store each pay item.
   - An EmployeePayComponents class manages a dynamic array of these, supporting adding and removing components.

1.2.	Inheritance & Polymorphism:
   - An abstract base class PayCalcBase defines the compute interface.
   - FixedPayCalc and CommissionPayCalc derive from it and implement their own logic.

1.3.	Pointer Arithmetic:
   - All calculations in compute functions use pointer arithmetic instead of array indexing.

1.4.	Dynamic Calculator Array:
   - An array of PayCalcBase* is created to demonstrate polymorphic calculation using different strategies.

1.5.	Array Resizing:  
   - The addComponent and removeComponent methods in EmployeePayComponents demonstrate dynamic resizing.

2.	Annotated Code

The code in Employee_pay_calculator.cpp is thoroughly annotated with comments explaining the purpose of each line or block.

