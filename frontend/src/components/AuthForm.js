import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function AuthForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username === 'testuser' && password === 'testpass') {
      localStorage.setItem('isLoggedIn', true);
      navigate('/courses');
    } else {
      // Перенаправление на регистрацию
      navigate('/register'); 
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* ... (форма авторизации - без изменений) ... */}
    </form>
  );
}

export default AuthForm;
