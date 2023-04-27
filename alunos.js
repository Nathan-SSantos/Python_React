import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Alunos() {
  const [cpf, setCpf] = useState('');
  const [nome, setNome] = useState('');
  const [curso, setCurso] = useState('');
  const [periodo, setPeriodo] = useState('');
  const [alunos, setAlunos] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/alunos/')
      .then(response => {
        setAlunos(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  function adicionarAluno(event) {
    event.preventDefault();
    axios.post('http://localhost:5000/alunos/', { cpf, nome, curso, periodo })
      .then(response => {
        setAlunos([...alunos, response.data]);
        setCpf('');
        setNome('');
        setCurso('');
        setPeriodo('');
      })
      .catch(error => {
        console.error(error);
      });
  }

  return (
    <div className="App">
      <h1>Adicionar Aluno</h1>
      <form onSubmit={adicionarAluno}>
        <label>
          CPF:
          <input type="text" value={cpf} onChange={(e) => setCpf(e.target.value)} />
        </label>
        <label>
          Nome:
          <input type="text" value={nome} onChange={(e) => setNome(e.target.value)} />
        </label>
        <label>
          Curso:
          <input type="text" value={curso} onChange={(e) => setCurso(e.target.value)} />
        </label>
        <label>
          Período:
          <input type="text" value={periodo} onChange={(e) => setPeriodo(e.target.value)} />
        </label>
        <button type="submit">Adicionar</button>
      </form>
      <h1>Lista de Alunos</h1>
      <table>
        <thead>
          <tr>
            <th>CPF
        </tr>
        <tr>
          <th>Nome</th>
          <th>Curso</th>
          <th>Período</th>
        </tr>
      </thead>
      <tbody>
        {alunos.map(aluno => (
          <tr key={aluno.cpf}>
            <td>{aluno.nome}</td>
            <td>{aluno.curso}</td>
            <td>{aluno.periodo}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
