// Toggle navigation menu
document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.querySelector('nav');
    const navLinks = document.querySelectorAll('nav li');
  
    navLinks.forEach((link) => {
      link.addEventListener('click', () => {
        navToggle.classList.toggle('active');
      });
    });
  });
  
  // Stock data filtering
  const stockData = document.getElementById('stock-data');
  const filterInput = document.getElementById('filter-input');
  
  filterInput.addEventListener('input', () => {
    const filterValue = filterInput.value.toLowerCase();
    const stockCards = document.querySelectorAll('.stock-card');
  
    stockCards.forEach((card) => {
      const stockName = card.querySelector('h2').textContent.toLowerCase();
      if (stockName.includes(filterValue)) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  });
  
  // Portfolio performance metrics
  const portfolioData = document.getElementById('portfolio-data');
  const portfolioCards = document.querySelectorAll('.portfolio-card');
  
  portfolioCards.forEach((card) => {
    const returnRate = card.querySelector('.return-rate');
    const riskLevel = card.querySelector('.risk-level');
  
    // Calculate portfolio performance metrics
    const portfolioReturn = Math.random() * 10; // Replace with actual data
    const portfolioRisk = Math.random() * 5; // Replace with actual data
  
    returnRate.textContent = `${portfolioReturn}%`;
    riskLevel.textContent = `${portfolioRisk}%`;
  });