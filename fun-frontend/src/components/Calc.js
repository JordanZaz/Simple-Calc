import React, { useState } from 'react';
import axios from 'axios';

function Calculator() {
    const [step, setStep] = useState(1); // 1: operator, 2: first number, 3: second number
    const [operator, setOperator] = useState('');
    const [firstNumber, setFirstNumber] = useState('');
    const [secondNumber, setSecondNumber] = useState('');
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);
  
    const unaryOperators = ["sqrt", "!"];

    const resetCalculator = () => {
        setStep(1);
        setOperator('');
        setFirstNumber('');
        setSecondNumber('');
        setResult(null);
        setError(null);
    };
  
    const handleOperatorSubmit = () => {
      setStep(2);
    };
  
    const handleFirstNumberSubmit = () => {
      if (unaryOperators.includes(operator)) {
        submitCalculation();
      } else {
        setStep(3);
      }
    };
  
    const handleSecondNumberSubmit = () => {
      submitCalculation();
    };
  
    const submitCalculation = async () => {
      try {
        const response = await axios.post('http://localhost:8000/calculate/', {
          operator,
          first_number: parseFloat(firstNumber),
          second_number: parseFloat(secondNumber),
        });
        setResult(response.data.result);
        setError(null);
      } catch (e) {
        if (e.response && e.response.data) {
          setError(e.response.data.error);
        } else {
          setError('An error occurred');
        }
        setResult(null);
      }
    };
  
    return (
      <div>
        {step === 1 && (
          <>
            <input type="text" placeholder="Operator" value={operator} onChange={e => setOperator(e.target.value)} />
            <button onClick={handleOperatorSubmit}>Submit Operator</button>
          </>
        )}
  
        {step === 2 && (
          <>
            <input type="text" placeholder="First Number" value={firstNumber} onChange={e => setFirstNumber(e.target.value)} />
            <button onClick={handleFirstNumberSubmit}>Submit First Number</button>
          </>
        )}
  
        {step === 3 && (
          <>
            <input type="text" placeholder="Second Number" value={secondNumber} onChange={e => setSecondNumber(e.target.value)} />
            <button onClick={handleSecondNumberSubmit}>Submit Second Number</button>
          </>
        )}
  
        {result !== null && (
                <div>
                    <div>Result: {result}</div>
                    <button onClick={resetCalculator}>Reset</button>
                </div>
            )}
            {error && (
                <div>
                    <div>Error: {error}</div>
                    <button onClick={resetCalculator}>Reset</button>
                </div>
            )}
        </div>
    );
}
  
  

export default Calculator;
