
#include <iostream>      // For input/output streams
#include <limits>        // For numeric_limits, used to clear input buffer
#include <cstring>       // For strcpy, in order to use it
using namespace std;

// Structure to store each pay component (e.g., salary, allowances, etc.)
struct PayComponent {
    char desc[30];   // Description of the component
    float amount;    // Amount for this component
};

// Abstract base class for pay calculation (demonstrates polymorphism)
class PayCalcBase {
public:
    // Pure virtual method to compute total pay; must be overridden by derived classes
    virtual float compute(const PayComponent*, int) = 0;
    virtual ~PayCalcBase() {} // Virtual destructor for base class
};

// Calculator that just sums all component amounts
class FixedPayCalc : public PayCalcBase {
public:
    float compute(const PayComponent* comps, int n) override {
        float sum = 0;
        // Loop through the array using pointer arithmetic
        const PayComponent* ptr = comps;
        for (int i = 0; i < n; ++i, ++ptr)
            sum += ptr->amount;
        return sum;
    }
};

// Calculator that sums all components and adds a commission
class CommissionPayCalc : public PayCalcBase {
    float commission_rate_; // Commission rate (e.g., 0.10 for 10%)
public:
    CommissionPayCalc(float rate = 0.10f) : commission_rate_(rate) {}
    float compute(const PayComponent* comps, int n) override {
        float sum = 0;
        const PayComponent* ptr = comps;
        for (int i = 0; i < n; ++i, ++ptr)
            sum += ptr->amount;
        return sum + sum * commission_rate_;
    }
};

int main() {
    int n_components;
    cout << "Enter number of pay components: ";
    cin >> n_components;  // Read how many pay components

    // Dynamically allocate array for pay components
    PayComponent* comps = new PayComponent[n_components];

    // Read pay components from user
    for (int i = 0; i < n_components; ++i) {
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clear input buffer
        cout << "Enter description for component " << i + 1 << ": ";
        cin.getline(comps[i].desc, 30); // Get description
        cout << "Enter amount for component " << i + 1 << ": ";
        cin >> comps[i].amount;         // Get amount
    }

    // Create an array of calculator pointers (demonstrates polymorphism)
    PayCalcBase* calculators[2];
    calculators[0] = new FixedPayCalc();             // First calculator: fixed pay
    calculators[1] = new CommissionPayCalc(0.10f);   // Second: commission pay

    // Compute and display results using each calculator
    for (int i = 0; i < 2; ++i) {
        float result = calculators[i]->compute(comps, n_components); // Polymorphic call
        if (i == 0)
            cout << "[FixedPayCalc] Total Pay: $" << result <<endl;
        else
            cout << "[CommissionPayCalc] Total Pay (with 10% commission): $" << result <<endl;
    }

    // Clean up dynamic memory
    delete calculators[0];
    delete calculators[1];
    delete[] comps;

    // Pause so output doesn't disappear instantly (for Windows)
    cout << "Press Enter to exit...";
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    cin.get();
    return 0;
}
