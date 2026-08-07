let currentCategory = null;

// Get all category buttons
const categoryButtons = document.querySelectorAll('.category-btn');
const resultSection = document.getElementById('resultSection');
const resultText = document.getElementById('resultText');
const generateAgainBtn = document.getElementById('generateAgainBtn');
const resetBtn = document.getElementById('resetBtn');
const loading = document.getElementById('loading');
const categoriesSection = document.querySelector('.categories');

// Add click listeners to category buttons
categoryButtons.forEach(button => {
    button.addEventListener('click', () => {
        const category = button.dataset.category;
        generateIdea(category);
    });
});

// Generate Again button
generateAgainBtn.addEventListener('click', () => {
    if (currentCategory) {
        generateIdea(currentCategory);
    }
});

// Reset button
resetBtn.addEventListener('click', () => {
    resultSection.style.display = 'none';
    categoriesSection.style.display = 'block';
    currentCategory = null;
});

// Generate idea function
async function generateIdea(category) {
    currentCategory = category;
    
    // Show loading state
    categoriesSection.style.display = 'none';
    resultSection.style.display = 'none';
    loading.style.display = 'flex';

    try {
        const response = await fetch(`/api/generate/${category}`);
        const data = await response.json();

        if (response.ok) {
            // Simulate a slight delay for effect
            setTimeout(() => {
                loading.style.display = 'none';
                resultText.textContent = data.idea;
                resultSection.style.display = 'block';
            }, 300);
        } else {
            loading.style.display = 'none';
            resultText.textContent = 'Something went wrong. Try again!';
            resultSection.style.display = 'block';
        }
    } catch (error) {
        console.error('Error:', error);
        loading.style.display = 'none';
        resultText.textContent = 'Connection error. Try again!';
        resultSection.style.display = 'block';
    }
          }
