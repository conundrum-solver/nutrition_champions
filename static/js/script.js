// Get the dark mode toggle button
const darkModeToggle = document.getElementById('dark-mode-toggle');

// Add click event listener to toggle dark mode
darkModeToggle.addEventListener('click', () => {
    // Toggle dark mode class on the body
    document.body.classList.toggle('dark-mode');

    // Toggle theme stylesheet
    const themeStyle = document.getElementById('theme-style');
    if (themeStyle.getAttribute('href') === 'styles.css') {
        themeStyle.href = 'dark-mode.css'; // Load dark mode stylesheet
    } else {
        themeStyle.href = 'styles.css'; // Load light mode stylesheet
    }

    // Optionally, store user preference in local storage
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
});

// Check if dark mode preference is stored in local storage
const isDarkMode = JSON.parse(localStorage.getItem('darkMode'));
if (isDarkMode) {
    // Apply dark mode styles if preference is true
    document.body.classList.add('dark-mode');
}
