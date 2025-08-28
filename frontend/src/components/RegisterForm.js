import React from 'react';
import { useNavigate } from 'react-router-dom';

function RegisterForm() {
  const navigate = useNavigate();

  const handleRegister = () => {
    // Здесь должна быть реальная логика регистрации, обращающаяся к API
    // Сейчас — лишь имитация:
    alert('Регистрация (имитация)');
    navigate('/'); // Возврат на страницу авторизации
  };

  return (
    <div>
      <h1>Регистрация</h1>
      <button onClick={handleRegister}>Зарегистрироваться</button>
    </div>
  );
}

export default RegisterForm;
