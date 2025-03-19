
document.addEventListener('DOMContentLoaded', function() {
    // Existing accordion code
    var toggles = document.getElementsByClassName("skill-toggle");
    var skillAccordion = document.querySelector('.skill-accordion');

    // ... (keep the existing accordion code) ...

    // Dark mode toggle
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const body = document.body;

    // Check for saved user preference
    if (localStorage.getItem('darkMode') === 'enabled') {
        body.classList.add('dark-mode');
    }

    darkModeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        
        // Save user preference
        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'enabled');
        } else {
            localStorage.setItem('darkMode', null);
        }
    });
// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
            const headerOffset = 60; // Adjust this value to match your header height
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: "smooth"
            });
        }
    });
});
});


document.addEventListener('DOMContentLoaded', function() {
    var toggles = document.getElementsByClassName("skill-toggle");
    var skillAccordion = document.querySelector('.skill-accordion');

    // Add loaded class to trigger animation
    setTimeout(function() {
        skillAccordion.classList.add('loaded');
    }, 100);

    for (var i = 0; i < toggles.length; i++) {
        toggles[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
                content.classList.remove('active');
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
                content.classList.add('active');
            }
        });
    }

    // Animate progress bars when they come into view
    var progressBars = document.querySelectorAll('.progress-bar');
    var observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.width = entry.target.getAttribute('aria-valuenow') + '%';
            }
        });
    }, {threshold: 0.5});

    progressBars.forEach(bar => {
        observer.observe(bar);
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var triggerTabList = [].slice.call(document.querySelectorAll('#researchTabs button'))
    triggerTabList.forEach(function (triggerEl) {
        var tabTrigger = new bootstrap.Tab(triggerEl)

        triggerEl.addEventListener('click', function (event) {
            event.preventDefault()
            tabTrigger.show()
        })
    })
});