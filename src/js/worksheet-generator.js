// Worksheet Generator JavaScript
// Handles all three generation modes: Standard, Practice Test, Custom Builder

// Topic data by unit
const TOPICS_BY_UNIT = {
    '1.0': [
        { value: 'Introduction to Statistics', type: 'Intro' },
        { value: 'Representing Data Graphically', type: 'Graphing' },
        { value: 'Summarizing Quantitative Data', type: 'Intro' },
        { value: 'Modeling Data Distributions', type: 'Intro' }
    ],
    '2.0': [
        { value: 'What Are Solutions?', type: 'Intro' },
        { value: 'Equations', type: 'Intro' },
        { value: 'Inputs and Outputs', type: 'Intro' },
        { value: 'Property of Equality (add/subtract)', type: 'Intro' },
        { value: 'Property of Equality (mult/div)', type: 'Intro' },
        { value: 'Solving Multi-Step Equations', type: 'Intro' },
        { value: 'Linear Equations', type: 'Intro' },
        { value: 'Linear Equation Word Problems', type: 'Intro' },
        { value: 'Solving Equations with Variables on Both Sides', type: 'Intro' }
    ],
    '3.0': [
        { value: 'One-Step Inequalities', type: 'Graphing' }
    ],
    '4.0': [
        { value: 'Points on a Coordinate Plane', type: 'Graphing' },
        { value: 'Line on a Coordinate Plane', type: 'Graphing' },
        { value: 'Slope-Intercept Form', type: 'Graphing' },
        { value: 'Point-Slope Form', type: 'Graphing' },
        { value: 'Standard Form', type: 'Graphing' }
    ],
    '5.0': [
        { value: 'Systems of Equations', type: 'Intro' },
        { value: 'Systems of Equations', type: 'Graphing' }
    ],
    '11.0': [
        { value: 'Using Vertex Form', type: 'Graphing' }
    ]
};

let customSpecCount = 0;

// Tab switching
function showTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.remove('active');
    });

    // Show selected tab
    document.getElementById(`${tabName}-tab`).classList.add('active');
    event.target.classList.add('active');
}

// Update topics dropdown based on selected unit
function updateTopics() {
    const unitSelect = document.getElementById('unit');
    const topicSelect = document.getElementById('topic');
    const unit = unitSelect.value;

    topicSelect.innerHTML = '<option value="">Select topic...</option>';

    if (unit && TOPICS_BY_UNIT[unit]) {
        topicSelect.disabled = false;
        TOPICS_BY_UNIT[unit].forEach(topic => {
            const option = document.createElement('option');
            option.value = `${topic.value}|${topic.type}`;
            option.textContent = topic.value;
            topicSelect.appendChild(option);
        });
    } else {
        topicSelect.disabled = true;
    }
}

// Update spiral review topics
function updateSpiralTopics() {
    const unitSelect = document.getElementById('spiralUnit');
    const topicSelect = document.getElementById('spiralTopic');
    const unit = unitSelect.value;

    topicSelect.innerHTML = '<option value="">Select topic...</option>';

    if (unit && TOPICS_BY_UNIT[unit]) {
        topicSelect.disabled = false;
        TOPICS_BY_UNIT[unit].forEach(topic => {
            const option = document.createElement('option');
            option.value = `${topic.value}|${topic.type}`;
            option.textContent = topic.value;
            topicSelect.appendChild(option);
        });
    } else {
        topicSelect.disabled = true;
    }
}

// Update practice test form based on test type
function updatePracticeForm() {
    const testType = document.getElementById('testType').value;

    // Hide all fields
    document.getElementById('unitReviewFields').style.display = 'none';
    document.getElementById('cumulativeFields').style.display = 'none';
    document.getElementById('spiralFields').style.display = 'none';
    document.getElementById('problemCountField').style.display = 'block';

    // Show relevant fields
    if (testType === 'unit') {
        document.getElementById('unitReviewFields').style.display = 'block';
    } else if (testType === 'cumulative') {
        document.getElementById('cumulativeFields').style.display = 'block';
    } else if (testType === 'spiral') {
        document.getElementById('spiralFields').style.display = 'block';
        document.getElementById('problemCountField').style.display = 'none';
    }
}

// Show status message
function showStatus(message, type = 'success') {
    const statusDiv = document.getElementById('statusMessage');
    statusDiv.className = `status-message status-${type} show`;
    statusDiv.textContent = message;

    // Auto-hide after 5 seconds for success/error
    if (type !== 'loading') {
        setTimeout(() => {
            statusDiv.classList.remove('show');
        }, 5000);
    }
}

// Standard worksheet form submission
document.getElementById('standardForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const unit = document.getElementById('unit').value;
    const topicData = document.getElementById('topic').value.split('|');
    const topic = topicData[0];
    const topicType = topicData[1];
    const difficulty = document.getElementById('difficulty').value;
    const numProblems = document.getElementById('numProblems').value;
    const customTitle = document.getElementById('worksheetTitle').value;

    if (!unit || !topic) {
        showStatus('Please select both unit and topic', 'error');
        return;
    }

    showStatus('Generating worksheet...', 'loading');

    try {
        const response = await fetch('/api/generate-worksheet', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                unit: parseFloat(unit),
                topic,
                topicType,
                difficulty,
                numProblems: parseInt(numProblems),
                customTitle
            })
        });

        const result = await response.json();

        if (result.success) {
            showStatus(`Worksheet generated successfully! Saved to: ${result.path}`, 'success');
            // Trigger download
            window.location.href = result.downloadUrl;
        } else {
            showStatus(`Error: ${result.error}`, 'error');
        }
    } catch (error) {
        showStatus(`Error generating worksheet: ${error.message}`, 'error');
    }
});

// Practice test form submission
document.getElementById('practiceForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const testType = document.getElementById('testType').value;
    const difficultyMix = document.getElementById('difficultyMix').value;

    let requestData = {
        testType,
        difficultyMix
    };

    if (testType === 'unit') {
        requestData.unit = parseFloat(document.getElementById('reviewUnit').value);
        requestData.numProblems = parseInt(document.getElementById('testProblems').value);
    } else if (testType === 'cumulative') {
        const checkboxes = document.querySelectorAll('#cumulativeFields input[type="checkbox"]:checked');
        if (checkboxes.length === 0) {
            showStatus('Please select at least one unit', 'error');
            return;
        }
        requestData.units = Array.from(checkboxes).map(cb => parseFloat(cb.value));
        requestData.numProblems = parseInt(document.getElementById('testProblems').value);
    } else if (testType === 'spiral') {
        const topicData = document.getElementById('spiralTopic').value.split('|');
        if (!topicData[0]) {
            showStatus('Please select unit and topic', 'error');
            return;
        }
        requestData.unit = parseFloat(document.getElementById('spiralUnit').value);
        requestData.topic = topicData[0];
        requestData.topicType = topicData[1];
        requestData.problemsPerLevel = parseInt(document.getElementById('spiralProblemsPerLevel').value);
    }

    showStatus('Generating practice test...', 'loading');

    try {
        const response = await fetch('/api/generate-practice-test', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestData)
        });

        const result = await response.json();

        if (result.success) {
            showStatus(`Practice test generated successfully! Saved to: ${result.path}`, 'success');
            window.location.href = result.downloadUrl;
        } else {
            showStatus(`Error: ${result.error}`, 'error');
        }
    } catch (error) {
        showStatus(`Error generating practice test: ${error.message}`, 'error');
    }
});

// Custom worksheet builder
function addCustomSpec() {
    customSpecCount++;
    const container = document.getElementById('customSpecs');

    const row = document.createElement('div');
    row.className = 'custom-spec-row';
    row.id = `spec-${customSpecCount}`;
    row.innerHTML = `
        <div>
            <label style="font-size: 0.875rem; margin-bottom: 0.25rem; display: block;">Unit</label>
            <select class="spec-unit" onchange="updateCustomTopics(${customSpecCount})">
                <option value="">Select...</option>
                <option value="1.0">Unit 1</option>
                <option value="2.0">Unit 2</option>
                <option value="3.0">Unit 3</option>
                <option value="4.0">Unit 4</option>
                <option value="5.0">Unit 5</option>
                <option value="11.0">Unit 11</option>
            </select>
        </div>
        <div>
            <label style="font-size: 0.875rem; margin-bottom: 0.25rem; display: block;">Topic</label>
            <select class="spec-topic" disabled>
                <option value="">Select unit first...</option>
            </select>
        </div>
        <div>
            <label style="font-size: 0.875rem; margin-bottom: 0.25rem; display: block;">Difficulty</label>
            <select class="spec-difficulty">
                <option value="easy">Easy</option>
                <option value="medium" selected>Medium</option>
                <option value="hard">Hard</option>
                <option value="challenge">Challenge</option>
            </select>
        </div>
        <div>
            <label style="font-size: 0.875rem; margin-bottom: 0.25rem; display: block;">Problems</label>
            <input type="number" class="spec-problems" value="5" min="1" max="20" style="padding: 0.5rem;">
        </div>
        <div>
            <label style="font-size: 0.875rem; margin-bottom: 0.25rem; display: block;">&nbsp;</label>
            <button type="button" class="btn btn-danger btn-small" onclick="removeCustomSpec(${customSpecCount})">
                Remove
            </button>
        </div>
    `;

    container.appendChild(row);
}

function removeCustomSpec(id) {
    const row = document.getElementById(`spec-${id}`);
    if (row) {
        row.remove();
    }
}

function updateCustomTopics(specId) {
    const row = document.getElementById(`spec-${specId}`);
    const unitSelect = row.querySelector('.spec-unit');
    const topicSelect = row.querySelector('.spec-topic');
    const unit = unitSelect.value;

    topicSelect.innerHTML = '<option value="">Select topic...</option>';

    if (unit && TOPICS_BY_UNIT[unit]) {
        topicSelect.disabled = false;
        TOPICS_BY_UNIT[unit].forEach(topic => {
            const option = document.createElement('option');
            option.value = `${topic.value}|${topic.type}`;
            option.textContent = topic.value;
            topicSelect.appendChild(option);
        });
    } else {
        topicSelect.disabled = true;
    }
}

async function generateCustomWorksheet() {
    const title = document.getElementById('customTitle').value;

    if (!title) {
        showStatus('Please enter a worksheet title', 'error');
        return;
    }

    const rows = document.querySelectorAll('.custom-spec-row');
    if (rows.length === 0) {
        showStatus('Please add at least one topic', 'error');
        return;
    }

    const specs = [];
    for (const row of rows) {
        const unit = row.querySelector('.spec-unit').value;
        const topicData = row.querySelector('.spec-topic').value.split('|');
        const topic = topicData[0];
        const topicType = topicData[1];
        const difficulty = row.querySelector('.spec-difficulty').value;
        const problems = parseInt(row.querySelector('.spec-problems').value);

        if (!unit || !topic) {
            showStatus('Please complete all fields in each row', 'error');
            return;
        }

        specs.push({
            unit: parseFloat(unit),
            topic,
            topicType,
            difficulty,
            numProblems: problems
        });
    }

    showStatus('Generating custom worksheet...', 'loading');

    try {
        const response = await fetch('/api/generate-custom', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                title,
                specs
            })
        });

        const result = await response.json();

        if (result.success) {
            showStatus(`Custom worksheet generated successfully! Saved to: ${result.path}`, 'success');
            window.location.href = result.downloadUrl;
        } else {
            showStatus(`Error: ${result.error}`, 'error');
        }
    } catch (error) {
        showStatus(`Error generating custom worksheet: ${error.message}`, 'error');
    }
}

// Initialize with one custom spec row
if (document.getElementById('custom-tab')) {
    addCustomSpec();
}
