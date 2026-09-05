import Tasks from "./components/Tasks";
import AddTasks from "./components/AddTasks";
import { useEffect, useState } from "react";
import { v4 } from "uuid";
function App() {
  const [tasks, setTasks] = useState(
    JSON.parse(localStorage.getItem("tasks")) || [],
  );

  // useEffect(() => {
  //   const FetchFalse = async () => {
  //     const response = await fetch("url de uma api........;.......");

  //     const dados = response.json();
  //     setTasks(dados);
  //   };
  //   // SE EUY QUISER CHAMAR A API  PARA AS TAREFAS,,,,.....
  //     FetchFalse();
  // });

  useEffect(() => {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  }, [tasks]);

  function OnTaskClick(TaksId) {
    const newTask = tasks.map((task) => {
      if (task.id === TaksId) {
        return { ...task, iscompleted: !task.iscompleted };
      }
      return task;
    });
    setTasks(newTask);
  }

  function DeleteTask(deleteId) {
    const TaskDelete = tasks.filter((task) => task.id != deleteId);
    setTasks(TaskDelete);
  }
  function onTaskSubmit(title, descrition) {
    const newTask = {
      id: v4(),
      title: title,
      descrition: descrition,
      iscompleted: false,
    };
    title = "";
    descrition = "";
    setTasks([...tasks, newTask]);
  }

  return (
    <div className="w-screen min-h-screen bg-slate-500 flex  justify-center p-6">
      <div className="w-500px space-y-4">
        <h1 className="text-3xl text-slate-100 font-bold text-center">
          Gerenciador de Tarefas
        </h1>
        <AddTasks onTaskSubmit={onTaskSubmit} />
        <Tasks
          tasks={tasks}
          OnTaskClick={OnTaskClick}
          DeleteTask={DeleteTask}
        />
      </div>
    </div>
  );
}
export default App;
