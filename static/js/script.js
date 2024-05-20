// JavaScript (script.js)
document.addEventListener("DOMContentLoaded", () => {
  const darkModeToggle = document.getElementById("dark-mode-toggle");
  const darkModeToggleMobile = document.getElementById(
    "dark-mode-toggle-mobile"
  );
  const themeStyle = document.getElementById("theme-style");

  // Function to toggle dark mode
  const toggleDarkMode = () => {
    const isDarkMode = document.body.classList.toggle("dark-mode");
    themeStyle.href = isDarkMode ? "dark-mode.css" : "styles.css";
    saveDarkModePreference(isDarkMode);
  };

  // Add click event listener to toggle dark mode
  darkModeToggle.addEventListener("click", toggleDarkMode);
  darkModeToggleMobile.addEventListener("click", toggleDarkMode);

  // Check if dark mode preference is stored in cookie
  const isDarkMode = getDarkModePreference();
  if (isDarkMode) {
    // Apply dark mode styles if preference is true
    document.body.classList.add("dark-mode");
    themeStyle.href = "dark-mode.css";
  }

  // Function to retrieve dark mode preference from cookie
  function getDarkModePreference() {
    const darkModeCookie = document.cookie.replace(
      /(?:(?:^|.*;\s*)darkModeEnabled\s*\=\s*([^;]*).*$)|^.*$/,
      "$1"
    );
    return darkModeCookie === "true";
  }

  // Function to save dark mode preference to cookie
  function saveDarkModePreference(isDarkMode) {
    const expires = new Date();
    expires.setTime(expires.getTime() + 365 * 24 * 60 * 60 * 1000); // Set cookie expiration to 1 year
    document.cookie = `darkModeEnabled=${isDarkMode};expires=${expires.toUTCString()};path=/`;
  }
});

// Adding functionality for mobile devices
document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.getElementById("menu-toggle");
  const mobileNav = document.getElementById("mobile-nav");

  menuToggle.addEventListener("click", function () {
    if (mobileNav.style.display === "block") {
      mobileNav.style.display = "none";
    } else {
      mobileNav.style.display = "block";
    }
  });
});
