// Main JavaScript file for Online School Diary

// Check authentication on page load
document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('token');
    const currentPath = window.location.pathname;
    
    // Public pages that don't require authentication
    const publicPages = ['/', '/login'];
    
    if (!token && !publicPages.includes(currentPath)) {
        window.location.href = '/';
    }
    
    // Verify token is not expired
    if (token && !publicPages.includes(currentPath)) {
        try {
            const payload = JSON.parse(atob(token.split('.')[1]));
            const exp = payload.exp * 1000; // Convert to milliseconds
            
            if (Date.now() >= exp) {
                localStorage.removeItem('token');
                window.location.href = '/';
            }
        } catch (error) {
            console.error('Invalid token format');
            localStorage.removeItem('token');
            window.location.href = '/';
        }
    }
});

// Logout function
function logout() {
    localStorage.removeItem('token');
    window.location.href = '/';
}

// API helper function
async function apiRequest(endpoint, options = {}) {
    const token = localStorage.getItem('token');
    
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    };
    
    const mergedOptions = {
        ...defaultOptions,
        ...options,
        headers: {
            ...defaultOptions.headers,
            ...options.headers
        }
    };
    
    try {
        const response = await fetch(endpoint, mergedOptions);
        
        if (response.status === 401) {
            // Unauthorized - redirect to login
            localStorage.removeItem('token');
            window.location.href = '/';
            return null;
        }
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Request failed');
        }
        
        return await response.json();
    } catch (error) {
        console.error('API request error:', error);
        throw error;
    }
}

// Show toast notification
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `alert alert-${type} position-fixed top-0 end-0 m-3`;
    toast.style.zIndex = '9999';
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// Format date to Russian locale
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('ru-RU', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

// Format time
function formatTime(timeString) {
    return timeString;
}

// Get current user info from token
function getCurrentUser() {
    const token = localStorage.getItem('token');
    if (!token) return null;
    
    try {
        const payload = JSON.parse(atob(token.split('.')[1]));
        return {
            username: payload.sub,
            role: payload.role
        };
    } catch (error) {
        console.error('Error parsing token:', error);
        return null;
    }
}

// Validate form
function validateForm(formId) {
    const form = document.getElementById(formId);
    return form.checkValidity();
}

// Export functions
window.logout = logout;
window.apiRequest = apiRequest;
window.showToast = showToast;
window.formatDate = formatDate;
window.formatTime = formatTime;
window.getCurrentUser = getCurrentUser;
window.validateForm = validateForm;
