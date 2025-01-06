document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');

    try {
        // 隐藏加载指示器（如果有的话）
        function hideLoader() {
            const loader = document.getElementById('loader');
            if (loader) {
                loader.style.display = 'none';
            }
        }

        // 更新日期
        function updateDate() {
            const dateElement = document.getElementById('date');
            if (!dateElement) {
                console.error('Date element not found');
                return;
            }
            const now = new Date();
            dateElement.textContent = now.toLocaleDateString('zh-CN', { 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric' 
            });
        }

        // 图片上传
        const imageUpload = document.getElementById('image-upload');
        if (imageUpload) {
            imageUpload.addEventListener('change', function(event) {
                const file = event.target.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        const img = new Image();
                        img.onload = function() {
                            const canvas = document.createElement('canvas');
                            const ctx = canvas.getContext('2d');
                            
                            const targetSize = 100;
                            let newWidth, newHeight;
                            
                            if (img.width > img.height) {
                                newWidth = targetSize;
                                newHeight = (img.height / img.width) * targetSize;
                            } else {
                                newHeight = targetSize;
                                newWidth = (img.width / img.height) * targetSize;
                            }
                            
                            canvas.width = targetSize;
                            canvas.height = targetSize;
                            
                            ctx.fillStyle = '#FFFFFF';
                            ctx.fillRect(0, 0, targetSize, targetSize);
                            
                            const xOffset = (targetSize - newWidth) / 2;
                            const yOffset = (targetSize - newHeight) / 2;
                            ctx.drawImage(img, xOffset, yOffset, newWidth, newHeight);
                            
                            const resizedImage = canvas.toDataURL('image/jpeg', 0.8);
                            
                            const profileImage = document.getElementById('profile-image');
                            profileImage.src = resizedImage;
                            profileImage.style.width = `${targetSize}px`;
                            profileImage.style.height = `${targetSize}px`;
                            
                            document.getElementById('image-container').style.display = 'block';
                            document.getElementById('upload-button-container').style.display = 'none';
                        };
                        img.src = e.target.result;
                    }
                    reader.readAsDataURL(file);
                }
            });
        } else {
            console.error('Image upload element not found');
        }

        // 图片轮播
        const carousel = document.querySelector('.carousel');
        if (!carousel) {
            console.error('Carousel element not found');
            return;
        }
        const images = ['gallery1.jpg', 'gallery2.jpg', 'gallery3.jpg'];
        let currentSlide = 0;

        function loadImages() {
            carousel.innerHTML = '';
            images.forEach((image, index) => {
                const img = document.createElement('img');
                img.src = `images/${image}`;
                img.alt = `图片${index + 1}`;
                img.style.left = `${index * 100}%`;
                carousel.appendChild(img);
            });
            showSlide(0);
        }

        function showSlide(n) {
            const slides = document.querySelectorAll('.carousel img');
            if (slides.length === 0) {
                console.error('No slides found');
                return;
            }
            currentSlide = (n + slides.length) % slides.length;
            carousel.style.transform = `translateX(-${currentSlide * 100}%)`;
        }

        const prevButton = document.querySelector('.prev');
        const nextButton = document.querySelector('.next');
        if (prevButton && nextButton) {
            prevButton.addEventListener('click', () => showSlide(currentSlide - 1));
            nextButton.addEventListener('click', () => showSlide(currentSlide + 1));
        } else {
            console.error('Prev or Next button not found');
        }

        function autoPlay() {
            showSlide(currentSlide + 1);
        }

        // 初始化
        updateDate();
        loadImages();
        setInterval(updateDate, 60000);
        setInterval(autoPlay, 5000);

        // 隐藏加载指示器
        hideLoader();

        console.log('All functions initialized successfully');
    } catch (error) {
        console.error('An error occurred during initialization:', error);
        // 即使出错也隐藏加载指示器
        hideLoader();
    }
});