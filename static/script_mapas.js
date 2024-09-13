document.addEventListener('DOMContentLoaded', () => {
    const markers = document.querySelectorAll('.marker');
    const tooltip = document.getElementById('tooltip');

    markers.forEach(marker => {
        marker.addEventListener('mouseover', () => {
            const info = marker.getAttribute('data-info');
            tooltip.innerHTML = info;
            tooltip.style.display = 'block';
            tooltip.style.top = marker.offsetTop - tooltip.offsetHeight - 10 + 'px';
            tooltip.style.left = marker.offsetLeft + 'px';
        });

        marker.addEventListener('mouseout', () => {
            tooltip.style.display = 'none';
        });
    });
});
