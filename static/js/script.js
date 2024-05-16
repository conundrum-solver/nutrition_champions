// JavaScript (script.js)
document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const themeStyle = document.getElementById('theme-style');

    // Add click event listener to toggle dark mode
    darkModeToggle.addEventListener('click', () => {
        const isDarkMode = document.body.classList.toggle('dark-mode');
        themeStyle.href = isDarkMode ? 'dark-mode.css' : 'styles.css';
        saveDarkModePreference(isDarkMode);
    });

    // Check if dark mode preference is stored in cookie
    const isDarkMode = getDarkModePreference();
    if (isDarkMode) {
        // Apply dark mode styles if preference is true
        document.body.classList.add('dark-mode');
        themeStyle.href = 'dark-mode.css';
    }

    // Function to retrieve dark mode preference from cookie
    function getDarkModePreference() {
        const darkModeCookie = document.cookie.replace(/(?:(?:^|.*;\s*)darkModeEnabled\s*\=\s*([^;]*).*$)|^.*$/, '$1');
        return darkModeCookie === 'true';
    }

    // Function to save dark mode preference to cookie
    function saveDarkModePreference(isDarkMode) {
        const expires = new Date();
        expires.setTime(expires.getTime() + (365 * 24 * 60 * 60 * 1000)); // Set cookie expiration to 1 year
        document.cookie = `darkModeEnabled=${isDarkMode};expires=${expires.toUTCString()};path=/`;
    }
});
