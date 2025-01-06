let translatePopup = null;

// 创建翻译弹窗
function createPopup() {
  translatePopup = document.createElement('div');
  translatePopup.className = 'translate-popup';
  document.body.appendChild(translatePopup);
}

// 显示翻译结果
function showTranslation(text, x, y) {
  if (!translatePopup) {
    createPopup();
  }
  
  translatePopup.style.left = `${x}px`;
  translatePopup.style.top = `${y}px`;
  translatePopup.style.display = 'block';
  translatePopup.textContent = '翻译中...';
  
  // 调用谷歌翻译API（这里使用免费的API示例）
  fetch(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh&dt=t&q=${encodeURIComponent(text)}`)
    .then(response => response.json())
    .then(data => {
      const translation = data[0][0][0];
      translatePopup.textContent = translation;
    })
    .catch(error => {
      translatePopup.textContent = '翻译失败';
    });
}

// 监听选中文本事件
document.addEventListener('mouseup', (e) => {
  const selectedText = window.getSelection().toString().trim();
  
  if (selectedText) {
    const x = e.pageX;
    const y = e.pageY + 10;
    showTranslation(selectedText, x, y);
  } else if (translatePopup) {
    translatePopup.style.display = 'none';
  }
});

// 点击其他地方关闭弹窗
document.addEventListener('click', (e) => {
  if (translatePopup && !translatePopup.contains(e.target)) {
    translatePopup.style.display = 'none';
  }
}); 