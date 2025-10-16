// Grade Level Expansion Functionality
function toggleGradeLevel(header) {
    const content = header.nextElementSibling;
    const icon = header.querySelector('.toggle-icon');
    
    // Toggle the content visibility
    if (content.style.display === 'none' || !content.style.display) {
        content.style.display = 'block';
        icon.textContent = '−';
        header.setAttribute('aria-expanded', 'true');
        // Smooth scroll to the expanded section
        setTimeout(() => {
            content.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 100);
    } else {
        content.style.display = 'none';
        icon.textContent = '+';
        header.setAttribute('aria-expanded', 'false');
    }
}

// Initialize grade level headers
document.addEventListener('DOMContentLoaded', function() {
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
});
