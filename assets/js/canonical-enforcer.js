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
            
            // For search engines, we need a proper redirect
            // Check if we should use server redirect or client-side
            if (window.location.search.includes('src=')) {
                // Use meta refresh for search engines
                let metaRefresh = document.querySelector('meta[http-equiv="refresh"]');
                if (!metaRefresh) {
                    metaRefresh = document.createElement('meta');
                    metaRefresh.setAttribute('http-equiv', 'refresh');
                    metaRefresh.content = `0; url=${cleanURL}`;
                    document.head.appendChild(metaRefresh);
                } else {
                    metaRefresh.content = `0; url=${cleanURL}`;
                }
                
                // Also add noindex meta tag if not present
                let noindexTag = document.querySelector('meta[name="robots"][content*="noindex"]');
                if (!noindexTag) {
                    noindexTag = document.createElement('meta');
                    noindexTag.name = 'robots';
                    noindexTag.content = 'noindex, follow';
                    document.head.appendChild(noindexTag);
                }
                
                // Update canonical tag
                updateCanonicalTag();
                
                // Redirect after a short delay to allow meta tags to be processed
                setTimeout(() => {
                    window.location.href = cleanURL;
                }, 100);
            } else {
                // Use replaceState for non-critical parameters
                if (window.history && window.history.replaceState) {
                    window.history.replaceState({}, document.title, cleanURL);
                    updateCanonicalTag();
                }
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
