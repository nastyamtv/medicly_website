document.getElementById('send-btn').addEventListener('click', function () {
    const userInput = document.getElementById('user-input').value.trim();
    if (!userInput) return; // Перевірка на порожній запит

    // Відображення повідомлення користувача
    const chatBox = document.getElementById('chat-box');
    const userMessage = document.createElement('div');
    userMessage.className = 'chat-message user';
    userMessage.innerText = userInput;
    chatBox.appendChild(userMessage);
    chatBox.scrollTop = chatBox.scrollHeight;

    // Очищення поля вводу
    document.getElementById('user-input').value = '';

    // Відправка запиту на сервер
    fetch('/mediclybot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        body: JSON.stringify({ message: userInput }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error('Server error: ' + response.status);
            }
            return response.json();
        })
        .then((data) => {
            // Додавання відповіді бота до чату
            const botMessage = document.createElement('div');
            botMessage.className = 'chat-message bot';
            botMessage.innerText = data.reply || 'No response from bot.';
            chatBox.appendChild(botMessage);
            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch((error) => {
            // Обробка помилок
            const errorMessage = document.createElement('div');
            errorMessage.className = 'chat-message bot';
            errorMessage.innerText = 'An error occurred. Please try again.';
            chatBox.appendChild(errorMessage);
            chatBox.scrollTop = chatBox.scrollHeight;
            console.error('Error:', error);
        });
});
