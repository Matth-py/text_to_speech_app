const form = document.getElementById('text-form');
form.addEventListener('submit', async function(event) {
    event.preventDefault();

    const textInput = document.getElementById('text-input').value;
    if (textInput.trim() === "") {
        alert("Please enter some text!");
        return;
    }

    const response = await fetch('https://your-app-name.onrender.com/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: textInput }),
    });

    const data = await response.blob();
    const downloadLink = document.getElementById('download-link');
    const downloadSection = document.getElementById('download-section');
    downloadLink.href = URL.createObjectURL(data);
    downloadSection.style.display = 'block';
});