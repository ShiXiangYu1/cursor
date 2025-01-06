// 初始化变量
let startTime;
let elapsedTime = 0;
let timerInterval;

// 获取DOM元素
const timeDisplay = document.querySelector('.time-display');
const startBtn = document.getElementById('startBtn');
const pauseBtn = document.getElementById('pauseBtn');
const resetBtn = document.getElementById('resetBtn');

// 格式化时间显示
function formatTime(ms) {
    const hours = Math.floor(ms / 3600000);
    const minutes = Math.floor((ms % 3600000) / 60000);
    const seconds = Math.floor((ms % 60000) / 1000);
    
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

// 开始计时
function startTimer() {
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        timeDisplay.textContent = formatTime(elapsedTime);
    }, 10);
    
    startBtn.classList.add('hidden');
    pauseBtn.classList.remove('hidden');
}

// 暂停计时
function pauseTimer() {
    clearInterval(timerInterval);
    startBtn.classList.remove('hidden');
    pauseBtn.classList.add('hidden');
}

// 重置计时
function resetTimer() {
    clearInterval(timerInterval);
    elapsedTime = 0;
    timeDisplay.textContent = '00:00:00';
    startBtn.classList.remove('hidden');
    pauseBtn.classList.add('hidden');
}

// 添加事件监听器
startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pauseTimer);
resetBtn.addEventListener('click', resetTimer); 