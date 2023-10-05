---

# Mailer Service

Простой сервис на FastAPI для отправки электронных писем через SMTP.

## Запуск

## Сборка и запуск с Docker:

```bash
docker build -t mailer-service .
docker run -p 8000:8000 -e SMTP_HOST=your_smtp_server.com -e SMTP_PORT=587 -e SMTP_USER=your_email@example.com -e SMTP_PASSWORD=your_password mailer-service
```

## API Endpoints

- **POST /send_email**: Отправляет электронное письмо.

  Тело запроса:

  ```json
  {
    "to": "recipient@example.com",
    "subject": "Your Subject Here",
    "message": "Your Message Here"
  }
  ```

  Ответ:

  ```json
  {
    "message": "Email sent successfully"
  }
  ```

## Тестирование

Для запуска тестов выполните:

```bash
pytest app/tests/
```

## Модели

### EmailPayload

Модель данных для отправки электронных писем.

- `to`: Адрес получателя. (Обязательное поле)
- `subject`: Тема письма. (Обязательное поле)
- `message`: Текст сообщения. (Обязательное поле)

## Безопасность

Учетные данные SMTP передаются через переменные окружения, что позволяет исключить их сохранение в коде и обеспечить большую безопасность.

---

