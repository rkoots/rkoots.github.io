let allTools = [];
let filteredTools = [];

document.addEventListener('DOMContentLoaded', () => {
    allTools = tools;
    filteredTools = [...allTools];
    renderTools();
    setupEventListeners();
});

function setupEventListeners() {
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', debounce(handleSearch, 300));
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function handleSearch(e) {
    const query = e.target.value.toLowerCase().trim();
    
    if (!query) {
        filteredTools = [...allTools];
        renderTools();
        return;
    }

    showRocketLoader();

    setTimeout(() => {
        filteredTools = allTools.filter(tool => {
            const nameMatch = tool.name.toLowerCase().includes(query);
            const descMatch = tool.description.toLowerCase().includes(query);
            const keywordMatch = tool.keywords.some(kw => kw.toLowerCase().includes(query));
            
            return nameMatch || descMatch || keywordMatch;
        });

        hideRocketLoader();
        renderTools();
    }, 800);
}

function renderTools() {
    const grid = document.getElementById('toolsGrid');
    const noResults = document.getElementById('noResults');
    const resultsInfo = document.getElementById('resultsInfo');

    grid.innerHTML = '';

    if (filteredTools.length === 0) {
        grid.style.display = 'none';
        noResults.style.display = 'block';
        resultsInfo.innerHTML = '';
        return;
    }

    grid.style.display = 'grid';
    noResults.style.display = 'none';
    resultsInfo.innerHTML = `<span>Found <strong>${filteredTools.length}</strong> AI tool${filteredTools.length !== 1 ? 's' : ''}</span>`;

    filteredTools.forEach((tool, index) => {
        const card = createToolCard(tool, index);
        grid.appendChild(card);
    });
}

function createToolCard(tool, index) {
    const card = document.createElement('div');
    card.className = 'tool-card';
    card.style.animationDelay = `${index * 0.05}s`;

    const icon = getIconForTool(tool.name);

    const keywordTags = tool.keywords
        .slice(0, 3)
        .map(kw => `<span class="keyword-tag">${kw}</span>`)
        .join('');

    card.innerHTML = `
        <div class="tool-icon">
            ${icon}
        </div>
        <div class="tool-content">
            <h3 class="tool-title">${tool.name}</h3>
            <p class="tool-description">${tool.description}</p>
            <div class="tool-keywords">
                ${keywordTags}
            </div>
            <a href="${tool.url}" target="_blank" rel="noopener noreferrer" class="tool-link" onclick="showRocketLoaderOnClick(event)">
                <i class="fas fa-external-link-alt"></i> Visit Tool
            </a>
        </div>
    `;

    return card;
}

function getIconForTool(toolName) {
    const name = toolName.toLowerCase();

    if (name.includes('video')) return '🎬';
    if (name.includes('image') || name.includes('photo')) return '🖼️';
    if (name.includes('text') || name.includes('article')) return '📝';
    if (name.includes('code') || name.includes('compiler')) return '💻';
    if (name.includes('pdf')) return '📄';
    if (name.includes('audio') || name.includes('tts') || name.includes('speech')) return '🔊';
    if (name.includes('qr')) return '📱';
    if (name.includes('password')) return '🔐';
    if (name.includes('encrypt') || name.includes('decrypt')) return '🔒';
    if (name.includes('url') || name.includes('shortener')) return '🔗';
    if (name.includes('base64')) return '🔢';
    if (name.includes('json') || name.includes('xml') || name.includes('sql')) return '⚙️';
    if (name.includes('barcode')) return '📊';
    if (name.includes('anime') || name.includes('cartoon') || name.includes('pixar')) return '🎨';
    if (name.includes('painting') || name.includes('drawing')) return '🖌️';
    if (name.includes('filter')) return '✨';
    if (name.includes('generator')) return '⚡';
    if (name.includes('converter')) return '🔄';
    if (name.includes('editor')) return '✏️';
    if (name.includes('remover')) return '🗑️';
    if (name.includes('upscaler') || name.includes('enhance')) return '📈';
    if (name.includes('puzzle') || name.includes('game')) return '🎮';
    if (name.includes('mind map') || name.includes('diagram')) return '🗺️';
    if (name.includes('chinese') || name.includes('calendar')) return '🏮';
    if (name.includes('lookup') || name.includes('search')) return '🔍';
    if (name.includes('parser')) return '📥';
    if (name.includes('mirror')) return '🪞';
    if (name.includes('plotter') || name.includes('graph')) return '📉';
    if (name.includes('headshot') || name.includes('profile')) return '👤';
    if (name.includes('outfit') || name.includes('fashion')) return '👗';
    if (name.includes('pet')) return '🐾';
    if (name.includes('character')) return '🎭';
    if (name.includes('beard') || name.includes('hair')) return '💇';
    if (name.includes('tattoo')) return '🎯';
    if (name.includes('teeth') || name.includes('smile')) return '😁';
    if (name.includes('emoji')) return '😊';
    if (name.includes('action figure') || name.includes('doll')) return '🧸';
    if (name.includes('yearbook')) return '📚';
    if (name.includes('ghibli')) return '🌸';
    if (name.includes('spongebob') || name.includes('meme')) return '😄';
    if (name.includes('line drawing')) return '✏️';
    if (name.includes('retro') || name.includes('ps2')) return '🕹️';

    return '🤖';
}

function showRocketLoaderOnClick(event) {
    event.preventDefault();
    const url = event.currentTarget.href;
    
    showRocketLoader();
    
    setTimeout(() => {
        window.open(url, '_blank');
        hideRocketLoader();
    }, 1500);
}

function showRocketLoader() {
    const loader = document.getElementById('rocketLoader');
    const overlay = document.getElementById('overlay');
    
    loader.classList.add('active');
    overlay.classList.add('active');
}

function hideRocketLoader() {
    const loader = document.getElementById('rocketLoader');
    const overlay = document.getElementById('overlay');
    
    loader.classList.remove('active');
    overlay.classList.remove('active');
}
