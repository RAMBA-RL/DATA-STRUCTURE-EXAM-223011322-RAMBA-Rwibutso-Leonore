#include <iostream>      // Includes functionality for input and output streams (cin, cout)
#include <limits>        // Provides numeric_limits, used here to clear the input buffer
#include <cstring>       // Includes string manipulation functions (not strictly necessary in this example)
using namespace std;     // Brings all standard library symbols into global scope (so we can use cout, cin, etc. directly)

// Structure to represent a pay component (such as salary, bonus, allowance, etc.)
struct PayComponent {
    char desc[30];   // Description of the pay component, up to 29 characters + null terminator
    float amount;    // Amount for this pay component
};

// Abstract base class to define a common interface for all pay calculators
class PayCalcBase {
public:
    // Pure virtual function; must be implemented by derived classes.
    // It computes total pay given an array of PayComponent and the number of components.
    virtual float compute(const PayComponent*, int) = 0;
    virtual ~PayCalcBase() {} // Virtual destructor for safe cleanup
};

// Derived class that sums all pay components (fixed pay calculation)
class FixedPayCalc : public PayCalcBase {
public:
    // Override the compute method to sum all component amounts using pointer arithmetic
    float compute(const PayComponent* comps, int n) override {
        float sum = 0;
        // Use a pointer to iterate through the array
        const PayComponent* ptr = comps;
        for (int i = 0; i < n; ++i, ++ptr)
            sum += ptr->amount; // Add the amount of each component to sum
        return sum; // Return the total pay
    }
};

// Derived class that sums all components and adds commission (e.g., sales commission)
class CommissionPayCalc : public PayCalcBase {
    float commission_rate_; // Stores the commission rate (for example, 0.10 for 10%)
public:
    // Constructor to set the commission rate
    CommissionPayCalc(float rate = 0.10f) : commission_rate_(rate) {}
    // Override the compute method to sum all amounts and apply commission
    float compute(const PayComponent* comps, int n) override {
        float sum = 0;
        const PayComponent* ptr = comps;
        for (int i = 0; i < n; ++i, ++ptr)
            sum += ptr->amount; // Sum component amounts
        return sum + sum * commission_rate_; // Add commission to the total
    }
};

int main() {
    int n_components; // Variable to store the number of pay components
    cout << "Enter number of pay components: ";
    cin >> n_components;  // Prompt user for number of components

    // Dynamically allocate an array for pay components based on user input
    PayComponent* comps = new PayComponent[n_components];

    // Loop to read each pay component from the user
    for (int i = 0; i < n_components; ++i) {
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clear input buffer before getline
        cout << "Enter description for component " << i + 1 << ": ";
        cin.getline(comps[i].desc, 30); // Read component description
        cout << "Enter amount for component " << i + 1 << ": ";
        cin >> comps[i].amount;         // Read component amount
    }

    // Create an array of calculator pointers (demonstrate polymorphism)
    PayCalcBase* calculators[2];
    calculators[0] = new FixedPayCalc();             // First calculator: sums all components
    calculators[1] = new CommissionPayCalc(0.10f);   // Second: sums all components and adds 10% commission

    // Loop through each calculator and compute/display the pay
    for (int i = 0; i < 2; ++i) {
        float result = calculators[i]->compute(comps, n_components); // Call compute using base class pointer
        if (i == 0)
            cout << "[FixedPayCalc] Total Pay: $" << result << endl;
        else
            cout << "[CommissionPayCalc] Total Pay (with 10% commission): $" << result << endl;
    }

    // Free dynamically allocated memory for calculators and components
    delete calculators[0];
    delete calculators[1];
    delete[] comps;

    // Pause before program exits (especially useful for Windows)
    cout << "Press Enter to exit...";
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    cin.get();
    return 0;
}
