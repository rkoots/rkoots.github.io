/**
 * Canonical URL Enforcer
 * Handles URL parameters and ensures clean canonical URLs
 * Prevents duplicate content indexing from parameter-based URLs
 */

(function() {
    'use strict';

    // List of parameters to remove for canonical URLs
    const PARAMS_TO_REMOVE = ['src', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'ref', 'fbclid', 'gclid', 'msclkid'];

    /**
     * Get clean canonical URL without tracking parameters
     */
    function getCanonicalURL() {
        const url = new URL(window.location.href);
        
        // Remove all tracking parameters
        PARAMS_TO_REMOVE.forEach(param => {
            url.searchParams.delete(param);
        });

        return url.toString();
    }

    /**
     * Check if current URL has parameters that should be removed
     */
    function hasParametersToRemove() {
        const urlParams = new URLSearchParams(window.location.search);
        
        for (let param of PARAMS_TO_REMOVE) {
            if (urlParams.has(param)) {
                return true;
            }
        }
        
        return false;
    }

    /**
     * Update canonical link tag
     */
    function updateCanonicalTag() {
        const canonicalURL = getCanonicalURL();
        let canonicalLink = document.querySelector('link[rel="canonical"]');
        
        if (!canonicalLink) {
            canonicalLink = document.createElement('link');
            canonicalLink.rel = 'canonical';
            document.head.appendChild(canonicalLink);
        }
        
        canonicalLink.href = canonicalURL;
    }

    /**
     * Redirect to clean URL if parameters exist
     * This prevents indexing of parameter URLs
     */
    function redirectToCanonical() {
        if (hasParametersToRemove()) {
            const cleanURL = getCanonicalURL();
            
            // Use replaceState to update URL without reload
            // This maintains user experience while fixing SEO
            if (window.history && window.history.replaceState) {
                window.history.replaceState({}, document.title, cleanURL);
                updateCanonicalTag();
            }
        }
    }

    /**
     * Initialize canonical enforcement
     */
    function init() {
        // Always ensure canonical tag is correct
        updateCanonicalTag();
        
        // Redirect to clean URL if needed
        redirectToCanonical();
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
