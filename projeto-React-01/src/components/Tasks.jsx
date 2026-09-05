import { ChevronRightIcon, TrashIcon } from "lucide-react";
import { useNavigate } from "react-router-dom";
import Button from "./Button";

function Tasks({ OnTaskClick, tasks, DeleteTask }) {
  const navigate = useNavigate();

  function onDetailClick(task) {
    const query = new URLSearchParams();
    query.set("title", task.title);
    query.set("descrition", task.descrition);
    navigate(`/task?${query.toString()} `);
  }

  return (
    <ul className="space-y-4 p-10 bg-slate-200 rounded-md shadow  ">
      {tasks.map((task) => (
        <li key={task.id} className="flex rounded-md gap-2 ">
          <button
            onClick={() => OnTaskClick(task.id)}
            className={`bg-slate-400 w-full text-left text-white p-2 rounded-md flex ${task.iscompleted && "line-through"}`}
          >
            {task.title}
          </button>
          <Button onClick={() => onDetailClick(task)}>
            <ChevronRightIcon />
          </Button>
          <Button onClick={() => DeleteTask(task.id)}>
            <TrashIcon />
          </Button>
        </li>
      ))}
    </ul>
  );
}

export default Tasks;
