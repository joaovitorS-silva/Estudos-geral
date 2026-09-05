import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import TaskPage from "./pages/TaskPage.jsx";

const rota = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
  },
  {
    path: "/task",
    element: <TaskPage/>
  }
]);

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <RouterProvider router={rota}></RouterProvider>
  </StrictMode>,
);
