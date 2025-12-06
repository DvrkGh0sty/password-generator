
document.getElementById('generate-btn').addEventListener('click', () => {
    const length = document.getElementById('length').value;
    if(length < 6){
        alert("Password length must be at least 6.");
        return;
    }

    fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ length: length })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('password-display').textContent = data.password;
    })
    .catch(err => console.error(err));
});
