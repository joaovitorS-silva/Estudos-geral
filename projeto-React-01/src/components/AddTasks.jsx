import { useState } from "react";
import Inputs from "./Inputs";

function AddTask({ onTaskSubmit }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  console.log({ title, description });
  return (
    <div className=" break-words space-y-4 p-10 bg-slate-200 rounded-md shadow  flex flex-col ">
      <Inputs
        type="text"
        placeholder="Digite o titulo da tarefa"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
      />
      <Inputs
        type="text"
        placeholder="digite a Descrição"
        value={description}
        onChange={(event) => setDescription(event.target.value)}
      />
      <button
        onClick={() => {
          if (!title.trim() || !description.trim()) {
            return alert("Preencha os Campos");
          }
          {
            setTitle("");
          }
          {
            setDescription("");
          }
          {
            onTaskSubmit(title, description);
          }
        }}
        className="bg-slate-400 text-white px-4 py-2 rounded-md font-medium"
      >
        Adicionar
      </button>
    </div>
  );
}
export default AddTask;
