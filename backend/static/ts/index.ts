function getCookie(name: string): string | null {
    let cookieValue: string | null = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.getElementById('generateBlogButton')?.addEventListener('click', async () => {
    const youtubeLinkElement = document.getElementById('youtubeLink') as HTMLInputElement;
    const loadingIndicator = document.getElementById('loading-circle');
    const blogContent = document.getElementById('blogContent');
    const blogTitle = document.getElementById('blogTitle');

    if (youtubeLinkElement && loadingIndicator && blogContent && blogTitle) {
        const youtubeLink = youtubeLinkElement.value;

        if (youtubeLink) {
            loadingIndicator.style.display = 'block';
            loadingIndicator.classList.remove("hidden");
            blogContent.innerHTML = '';
            blogTitle.innerHTML = '';

            const endpointUrl = '/generate-blog';

            try {
                const response = await fetch(endpointUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken || ''
                    },
                    body: JSON.stringify({ link: youtubeLink })
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();

                blogContent.innerHTML = data.content;
                blogTitle.innerHTML = data.blog_title;
                loadingIndicator.classList.add("hidden");
            } catch (error) {
                alert('An error occurred while generating the blog post. Please try again later.');
                loadingIndicator.classList.add("hidden");
            } finally {
                loadingIndicator.style.display = 'none';
            }
        } else {
            alert('Please enter a valid YouTube video link.');
        }
    } else {
        alert('Required elements are missing in the DOM.');
    }
});