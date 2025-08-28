import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await axios.get('http://localhost:8000/courses/', {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }
        });
        console.log('Полученные данные:', response.data);
        setCourses(response.data.courses);
        setLoading(false);
      } catch (err) {
        console.error('Ошибка при получении курсов:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchCourses();
  }, []);

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div>Ошибка: {error}</div>;

  return (
    <div className="container">
      <h1 className="page-title">Список курсов</h1>
      <div className="grid">
        {courses.map((course) => (
          <div key={course.id} className="card">
            <h2>{course.title}</h2>
            <p>{course.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
