document.addEventListener('DOMContentLoaded', (event) => {
    // Create doodle-style icons
    const icons = document.querySelectorAll('.icon');
    icons.forEach(icon => {
        const annotation = RoughNotation.annotate(icon, { type: 'circle', color: '#FFD93D', padding: 5 });
        annotation.show();
    });

    // Age Distribution Chart
    const ageData = [
        {
            x: ['18-24', '25-34', '35-44', '45-54', '55+'],
            y: [15, 30, 25, 20, 10],
            type: 'bar',
            marker: {
                color: ['#FF6B6B', '#4ECDC4', '#FFD93D', '#45B7D1', '#F38181']
            }
        }
    ];
    const ageLayout = {
        title: 'Age Distribution of TechTrends Customers',
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: '#2C3E50' }
    };
    Plotly.newPlot('ageDist', ageData, ageLayout);

    // Income vs Purchase Amount Scatter Plot
    const incomeData = [
        {
            x: [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
            y: [500, 700, 1000, 1200, 1500, 1800, 2000, 2500],
            mode: 'markers',
            type: 'scatter',
            marker: {
                color: '#4ECDC4',
                size: 10,
                line: {
                    color: '#FF6B6B',
                    width: 2
                }
            }
        }
    ];
    const incomeLayout = {
        title: 'Income vs Purchase Amount',
        xaxis: {title: 'Income'},
        yaxis: {title: 'Purchase Amount'},
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: '#2C3E50' }
    };
    Plotly.newPlot('incomePurchase', incomeData, incomeLayout);

    // Animate signature
    const signature = document.querySelector('.signature');
    setInterval(() => {
        signature.style.animation = 'none';
        signature.offsetHeight; // Trigger reflow
        signature.style.animation = null;
    }, 3000);
});