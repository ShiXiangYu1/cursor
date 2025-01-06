document.addEventListener('DOMContentLoaded', () => {
    const imageInput = document.getElementById('imageInput');
    const originalImage = document.getElementById('originalImage');
    const compressedImage = document.getElementById('compressedImage');
    const originalSize = document.getElementById('originalSize');
    const compressedSize = document.getElementById('compressedSize');
    const quality = document.getElementById('quality');
    const qualityValue = document.getElementById('qualityValue');
    const downloadBtn = document.getElementById('downloadBtn');
    const previewContainer = document.querySelector('.preview-container');

    let originalFile = null;

    // 监听文件上传
    imageInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (!file) return;
        
        originalFile = file;
        previewContainer.style.display = 'block';
        
        // 显示原始图片和大小
        const reader = new FileReader();
        reader.onload = (e) => {
            originalImage.src = e.target.result;
            originalSize.textContent = `原始大小: ${(file.size / 1024).toFixed(2)} KB`;
            compressImage();
        };
        reader.readAsDataURL(file);
    });

    // 监听质量滑块变化
    quality.addEventListener('input', (e) => {
        qualityValue.textContent = `${e.target.value}%`;
        compressImage();
    });

    // 压缩图片
    function compressImage() {
        if (!originalFile) return;

        const img = new Image();
        img.src = originalImage.src;
        
        img.onload = () => {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');

            // 保持原始宽高比
            canvas.width = img.width;
            canvas.height = img.height;

            // 绘制图片
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

            // 压缩并显示
            canvas.toBlob((blob) => {
                const url = URL.createObjectURL(blob);
                compressedImage.src = url;
                compressedSize.textContent = `压缩后大小: ${(blob.size / 1024).toFixed(2)} KB`;
                downloadBtn.disabled = false;
                
                // 更新下载按钮
                downloadBtn.onclick = () => {
                    const link = document.createElement('a');
                    link.href = url;
                    link.download = `compressed_${originalFile.name}`;
                    link.click();
                };
            }, 'image/jpeg', quality.value / 100);
        };
    }
}); 