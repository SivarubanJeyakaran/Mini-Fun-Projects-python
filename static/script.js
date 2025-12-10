document.getElementById('flamesForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const name1 = document.getElementById('name1').value.trim();
    const name2 = document.getElementById('name2').value.trim();
    const calculateBtn = document.getElementById('calculateBtn');
    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');
    
    // Clear previous messages
    errorDiv.classList.add('hidden');
    resultDiv.classList.add('hidden');
    
    // Disable button during request
    calculateBtn.disabled = true;
    calculateBtn.textContent = 'Calculating...';
    
    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name1, name2 })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            // Display result
            document.getElementById('namesDisplay').textContent = `${data.name1} ❤️ ${data.name2}`;
            document.getElementById('count').textContent = data.count;
            document.getElementById('outcome').textContent = data.result + ' 💕';
            resultDiv.classList.remove('hidden');
        } else {
            // Show error message
            errorDiv.textContent = data.error || 'An error occurred';
            errorDiv.classList.remove('hidden');
        }
    } catch (error) {
        errorDiv.textContent = 'Network error: ' + error.message;
        errorDiv.classList.remove('hidden');
        console.error('Error:', error);
    } finally {
        // Re-enable button
        calculateBtn.disabled = false;
        calculateBtn.textContent = 'Calculate';
    }
});

// Clear error when typing
document.getElementById('name1').addEventListener('focus', () => {
    document.getElementById('error').classList.add('hidden');
});

document.getElementById('name2').addEventListener('focus', () => {
    document.getElementById('error').classList.add('hidden');
});
