// Night Mode Functionality
function initNightMode() {
    const nightModeToggle = document.getElementById('night-mode-toggle');

    // Check for saved night mode preference or default to light mode
    const savedNightMode = localStorage.getItem('nightMode');
    if (savedNightMode === 'enabled') {
        document.documentElement.classList.add('night-mode');
        document.body.classList.add('night-mode');
    }

    // Toggle night mode on button click
    if (nightModeToggle) {
        nightModeToggle.addEventListener('click', function() {
            document.documentElement.classList.toggle('night-mode');
            document.body.classList.toggle('night-mode');

            // Save preference to localStorage
            if (document.body.classList.contains('night-mode')) {
                localStorage.setItem('nightMode', 'enabled');
            } else {
                localStorage.setItem('nightMode', 'disabled');
            }
        });
    }
}

// Grade Level Expansion Functionality
function toggleGradeLevel(header) {
    const content = header.nextElementSibling;
    const icon = header.querySelector('.toggle-icon');
    const gradeTitle = header.querySelector('h2').textContent;

    // Toggle the content visibility
    if (content.style.display === 'none' || !content.style.display) {
        content.style.display = 'block';
        icon.textContent = '−';
        header.setAttribute('aria-expanded', 'true');

        // Announce to screen readers
        announceToScreenReader(gradeTitle + ' section expanded');

        // Smooth scroll to the expanded section
        setTimeout(() => {
            content.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 100);
    } else {
        content.style.display = 'none';
        icon.textContent = '+';
        header.setAttribute('aria-expanded', 'false');

        // Announce to screen readers
        announceToScreenReader(gradeTitle + ' section collapsed');
    }
}

// Keyboard event handler for grade level headers
function handleKeyPress(event, header) {
    // Handle Enter and Space keys
    if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        toggleGradeLevel(header);
    }
}

// Screen reader announcement function
function announceToScreenReader(message) {
    const announcer = document.getElementById('sr-announcements');
    if (announcer) {
        announcer.textContent = message;
        // Clear the message after a brief delay so it can be announced again if needed
        setTimeout(() => {
            announcer.textContent = '';
        }, 1000);
    }
}

// Initialize grade level headers
document.addEventListener('DOMContentLoaded', function() {
    // Initialize night mode
    initNightMode();
    // Initialize grade level headers
    const gradeHeaders = document.querySelectorAll('.grade-level-header');
    gradeHeaders.forEach(header => {
        // Set initial state
        const content = header.nextElementSibling;
        content.style.display = 'none';
        
        // Add accessibility attributes
        header.setAttribute('role', 'button');
        header.setAttribute('tabindex', '0');
        header.setAttribute('aria-expanded', 'false');
        
        // Add keyboard support
        header.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                toggleGradeLevel(this);
            }
        });
    });

    // Expandable Card Functionality
    const gridItems = document.querySelectorAll('.grid-item');

    gridItems.forEach(item => {
        // Add click event listener to each card
        item.addEventListener('click', function(e) {
            // Prevent expanding when clicking on links inside the card
            if (e.target.tagName === 'A') {
                return;
            }

            // Toggle the expanded class on the clicked card
            const isExpanded = this.classList.contains('expanded');

            // Close all other expanded cards
            gridItems.forEach(otherItem => {
                if (otherItem !== this) {
                    otherItem.classList.remove('expanded');
                    const otherIcon = otherItem.querySelector('.expand-icon');
                    if (otherIcon) {
                        otherIcon.textContent = '+';
                    }
                }
            });

            // Toggle current card
            if (isExpanded) {
                this.classList.remove('expanded');
                const icon = this.querySelector('.expand-icon');
                if (icon) {
                    icon.textContent = '+';
                }
            } else {
                this.classList.add('expanded');
                const icon = this.querySelector('.expand-icon');
                if (icon) {
                    icon.textContent = '−';
                }

                // Smooth scroll to the card after a brief delay to allow expansion animation
                setTimeout(() => {
                    this.scrollIntoView({
                        behavior: 'smooth',
                        block: 'nearest'
                    });
                }, 100);
            }
        });

        // Add keyboard accessibility (Enter and Space keys)
        item.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });

        // Make cards focusable for keyboard navigation
        item.setAttribute('tabindex', '0');
        item.setAttribute('role', 'button');
        item.setAttribute('aria-expanded', 'false');

        // Update aria-expanded when card is toggled
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'class') {
                    const isExpanded = item.classList.contains('expanded');
                    item.setAttribute('aria-expanded', isExpanded);
                }
            });
        });

        observer.observe(item, { attributes: true });
    });

    // Optional: Close expanded cards when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.grid-item')) {
            gridItems.forEach(item => {
                item.classList.remove('expanded');
                const icon = item.querySelector('.expand-icon');
                if (icon) {
                    icon.textContent = '+';
                }
            });
        }
    });

    // Tab Navigation Functionality
    const tabButtons = document.querySelectorAll('.tab-button');

    tabButtons.forEach(button => {
        // Click event for tab switching
        button.addEventListener('click', function() {
            const domain = this.getAttribute('data-domain');
            const panelId = this.getAttribute('aria-controls');

            // Get all tabs and panels within the same domain (same tab-container)
            const tabContainer = this.closest('.tab-container');
            const allTabsInDomain = tabContainer.querySelectorAll('.tab-button');
            const allPanelsInDomain = tabContainer.querySelectorAll('.tab-panel');

            // Remove active class from all tabs and panels in this domain
            allTabsInDomain.forEach(tab => {
                tab.classList.remove('active');
                tab.setAttribute('aria-selected', 'false');
            });

            allPanelsInDomain.forEach(panel => {
                panel.classList.remove('active');
            });

            // Add active class to clicked tab and corresponding panel
            this.classList.add('active');
            this.setAttribute('aria-selected', 'true');

            const targetPanel = document.getElementById(panelId);
            if (targetPanel) {
                targetPanel.classList.add('active');
            }

            // Announce to screen readers
            const tabTitle = this.querySelector('h4').textContent;
            announceToScreenReader(tabTitle + ' tab selected');
        });

        // Keyboard navigation for tabs
        button.addEventListener('keydown', function(e) {
            const tabContainer = this.closest('.tab-container');
            const allTabsInDomain = Array.from(tabContainer.querySelectorAll('.tab-button'));
            const currentIndex = allTabsInDomain.indexOf(this);

            let targetTab = null;

            switch(e.key) {
                case 'ArrowDown':
                case 'ArrowRight':
                    e.preventDefault();
                    // Move to next tab
                    targetTab = allTabsInDomain[currentIndex + 1] || allTabsInDomain[0];
                    break;

                case 'ArrowUp':
                case 'ArrowLeft':
                    e.preventDefault();
                    // Move to previous tab
                    targetTab = allTabsInDomain[currentIndex - 1] || allTabsInDomain[allTabsInDomain.length - 1];
                    break;

                case 'Home':
                    e.preventDefault();
                    // Move to first tab
                    targetTab = allTabsInDomain[0];
                    break;

                case 'End':
                    e.preventDefault();
                    // Move to last tab
                    targetTab = allTabsInDomain[allTabsInDomain.length - 1];
                    break;

                case 'Enter':
                case ' ':
                    e.preventDefault();
                    // Activate current tab (same as click)
                    this.click();
                    return;
            }

            // Focus and activate the target tab
            if (targetTab) {
                targetTab.focus();
                targetTab.click();
            }
        });
    });

    // Tab list scroll indicators (mobile)
    // Update gradient visibility based on scroll position
    function updateScrollIndicators(tabList) {
        if (!tabList) return;

        const tabContainer = tabList.closest('.tab-container');
        if (!tabContainer) return;

        const scrollLeft = tabList.scrollLeft;
        const scrollWidth = tabList.scrollWidth;
        const clientWidth = tabList.clientWidth;
        const maxScroll = scrollWidth - clientWidth;

        // At start (hide left arrow)
        if (scrollLeft <= 5) {
            tabContainer.classList.add('at-start');
        } else {
            tabContainer.classList.remove('at-start');
        }

        // At end (hide right arrow)
        if (scrollLeft >= maxScroll - 5) {
            tabContainer.classList.add('at-end');
        } else {
            tabContainer.classList.remove('at-end');
        }
    }

    // Initialize scroll indicators for all tab lists
    const tabLists = document.querySelectorAll('.tab-list');
    tabLists.forEach(tabList => {
        // Initial check
        updateScrollIndicators(tabList);

        // Update on scroll
        tabList.addEventListener('scroll', () => {
            updateScrollIndicators(tabList);
        });

        // Update on window resize
        window.addEventListener('resize', () => {
            updateScrollIndicators(tabList);
        });

        // Update after images or content loads
        window.addEventListener('load', () => {
            updateScrollIndicators(tabList);
        });
    });

    // Resources Page - Grade-First Navigation
    const gradeTabButtons = document.querySelectorAll('.grade-tab-button');
    const domainTabButtons = document.querySelectorAll('.domain-tab-button');

    // Grade tab switching (horizontal tabs at top)
    gradeTabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const panelId = this.getAttribute('aria-controls');
            const schoolSection = this.closest('.school-section');

            if (!schoolSection) return;

            const allGradeTabs = schoolSection.querySelectorAll('.grade-tab-button');
            const allGradePanels = schoolSection.querySelectorAll('.grade-panel');

            // Remove active class from all grade tabs and panels
            allGradeTabs.forEach(tab => {
                tab.classList.remove('active');
                tab.setAttribute('aria-selected', 'false');
            });

            allGradePanels.forEach(panel => {
                panel.classList.remove('active');
            });

            // Add active class to clicked tab and corresponding panel
            this.classList.add('active');
            this.setAttribute('aria-selected', 'true');

            const targetPanel = document.getElementById(panelId);
            if (targetPanel) {
                targetPanel.classList.add('active');
            }

            // Announce to screen readers
            const gradeName = this.textContent.trim();
            announceToScreenReader(gradeName + ' selected');
        });

        // Keyboard navigation for grade tabs
        button.addEventListener('keydown', function(e) {
            const schoolSection = this.closest('.school-section');
            if (!schoolSection) return;

            const allGradeTabs = Array.from(schoolSection.querySelectorAll('.grade-tab-button'));
            const currentIndex = allGradeTabs.indexOf(this);
            let targetTab = null;

            switch(e.key) {
                case 'ArrowRight':
                    e.preventDefault();
                    targetTab = allGradeTabs[currentIndex + 1] || allGradeTabs[0];
                    break;
                case 'ArrowLeft':
                    e.preventDefault();
                    targetTab = allGradeTabs[currentIndex - 1] || allGradeTabs[allGradeTabs.length - 1];
                    break;
                case 'Home':
                    e.preventDefault();
                    targetTab = allGradeTabs[0];
                    break;
                case 'End':
                    e.preventDefault();
                    targetTab = allGradeTabs[allGradeTabs.length - 1];
                    break;
                case 'Enter':
                case ' ':
                    e.preventDefault();
                    this.click();
                    return;
            }

            if (targetTab) {
                targetTab.focus();
                targetTab.click();
            }
        });
    });

    // Domain tab switching (vertical tabs in sidebar)
    domainTabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const panelId = this.getAttribute('aria-controls');
            const gradePanel = this.closest('.grade-panel');

            if (!gradePanel) return;

            const allDomainTabs = gradePanel.querySelectorAll('.domain-tab-button');
            const allDomainPanels = gradePanel.querySelectorAll('.domain-panel');

            // Remove active class from all domain tabs and panels
            allDomainTabs.forEach(tab => {
                tab.classList.remove('active');
                tab.setAttribute('aria-selected', 'false');
            });

            allDomainPanels.forEach(panel => {
                panel.classList.remove('active');
            });

            // Add active class to clicked tab and corresponding panel
            this.classList.add('active');
            this.setAttribute('aria-selected', 'true');

            const targetPanel = document.getElementById(panelId);
            if (targetPanel) {
                targetPanel.classList.add('active');
            }

            // Announce to screen readers
            const domainName = this.textContent.trim();
            announceToScreenReader(domainName + ' domain selected');
        });

        // Keyboard navigation for domain tabs
        button.addEventListener('keydown', function(e) {
            const gradePanel = this.closest('.grade-panel');
            if (!gradePanel) return;

            const allDomainTabs = Array.from(gradePanel.querySelectorAll('.domain-tab-button'));
            const currentIndex = allDomainTabs.indexOf(this);
            let targetTab = null;

            switch(e.key) {
                case 'ArrowDown':
                case 'ArrowRight':
                    e.preventDefault();
                    targetTab = allDomainTabs[currentIndex + 1] || allDomainTabs[0];
                    break;
                case 'ArrowUp':
                case 'ArrowLeft':
                    e.preventDefault();
                    targetTab = allDomainTabs[currentIndex - 1] || allDomainTabs[allDomainTabs.length - 1];
                    break;
                case 'Home':
                    e.preventDefault();
                    targetTab = allDomainTabs[0];
                    break;
                case 'End':
                    e.preventDefault();
                    targetTab = allDomainTabs[allDomainTabs.length - 1];
                    break;
                case 'Enter':
                case ' ':
                    e.preventDefault();
                    this.click();
                    return;
            }

            if (targetTab) {
                targetTab.focus();
                targetTab.click();
            }
        });
    });
});
