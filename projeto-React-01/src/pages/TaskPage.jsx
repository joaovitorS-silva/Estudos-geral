import { ChevronLeftIcon } from "lucide-react";
import { useNavigate, useSearchParams } from "react-router-dom";

function TaskPage() {
  const [SearchParams] = useSearchParams();
  const title = SearchParams.get("title");
  const description = SearchParams.get("descrition");

  const navigate = useNavigate();

  function BackPage() {
    navigate(-1);
  }
  return (
    <div className="w-screen min-h-screen bg-slate-500  p-6">
      <div className=" w-full  max-w-[500px] mx-auto space-y-4">
        <div className="   relative mb-6">
          <button
            onClick={BackPage}
            className=" absolute left-0 top-0 bottom-0 text-slate-100"
          >
            <ChevronLeftIcon />
          </button>
          <h1 className="text-3xl text-slate-100 font-bold  text-center">
            Detalhes da Tarefa
          </h1>
        </div>
        <div className=" bg-slate-200 p-4 rounded-md">
          <h2 className="  text-xl font-bold text-slate-600 break-words">{title}</h2>
          <p className=" break-words text-slate-600">{description}</p>
        </div>
      </div>
    </div>
  );
}
export default TaskPage;
