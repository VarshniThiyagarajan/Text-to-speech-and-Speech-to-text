let phoneNumber = '';

function addNumber(number) {
    if (phoneNumber.length < 15) {
        phoneNumber += number;
        document.getElementById('phoneNumberDisplay').innerText = phoneNumber;
    }
}

function deleteLast() {
    if (phoneNumber.length > 0) {
        phoneNumber = phoneNumber.slice(0, -1);
        document.getElementById('phoneNumberDisplay').innerText = phoneNumber || 'Enter Number';
    }
}

function startCall() {
    if (phoneNumber.length > 0) {
        alert(`Calling ${phoneNumber}`);
        window.location.href = '/speech-to-text';
    } else {
        alert('Please enter a phone number first!');
    }
}


