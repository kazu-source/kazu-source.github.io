// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.querySelector('.nav-toggle');
    const mainNav = document.querySelector('.main-nav');
    const body = document.body;

    if (navToggle && mainNav) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            mainNav.classList.toggle('active');
            body.classList.toggle('nav-open');
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!mainNav.contains(e.target) && !navToggle.contains(e.target) && mainNav.classList.contains('active')) {
                navToggle.classList.remove('active');
                mainNav.classList.remove('active');
                body.classList.remove('nav-open');
            }
        });

        // Handle dropdown toggles on mobile
        const dropdowns = mainNav.querySelectorAll('.dropdown');
        dropdowns.forEach(dropdown => {
            const dropdownToggle = dropdown.querySelector('a[aria-haspopup="true"]');

            if (dropdownToggle) {
                dropdownToggle.addEventListener('click', (e) => {
                    // On mobile, toggle the dropdown
                    if (window.innerWidth <= 768) {
                        e.preventDefault();
                        dropdown.classList.toggle('active');
                        const isExpanded = dropdown.classList.contains('active');
                        dropdownToggle.setAttribute('aria-expanded', isExpanded);
                    }
                });
            }
        });

        // Close menu when clicking a non-dropdown link
        const navLinks = mainNav.querySelectorAll('a:not([aria-haspopup="true"])');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                mainNav.classList.remove('active');
                body.classList.remove('nav-open');
            });
        });
    }
});