// script.js

// Get all the grid items (language blocks)
const gridItems = document.querySelectorAll('.grid-item');

// Get the element where the selected language will be displayed
const selectedLangDisplay = document.getElementById('selectedLang');

// Loop through each grid item and add a click event listener
gridItems.forEach(item => {
    item.addEventListener('click', function() {
        // Get the language name from the data attribute
        const selectedLang = this.getAttribute('data-lang');
        
        // Update the selected language display
        selectedLangDisplay.textContent = selectedLang;
        
        // Optionally, you can store the selected language in localStorage or sessionStorage
        // localStorage.setItem('selectedLanguage', selectedLang);
    });
});

// Optional: Retrieve selected language from localStorage on page load
// const storedLanguage = localStorage.getItem('selectedLanguage');
// if (storedLanguage) {
//     selectedLangDisplay.textContent = storedLanguage;
// }
