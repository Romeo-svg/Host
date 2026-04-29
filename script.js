document.getElementById('rsvpForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('guestName').value;
    const email = document.getElementById('guestEmail').value;
    const status = document.getElementById('statusMessage');

    status.innerText = "Sending RSVP...";

    fetch('/submit-rsvp', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name, email: email })
    })
    .then(res => res.json())
    .then(data => {
        status.innerText = data.message;
        if (data.status === "success") {
            document.getElementById('rsvpForm').reset();
        }
    })
    .catch(err => {
        status.innerText = "Error sending RSVP";
        console.log(err);
    });
});