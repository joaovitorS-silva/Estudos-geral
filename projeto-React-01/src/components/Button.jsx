function Button(props) {
  return (


    <button {...props} className="bg-slate-400 p-2 text-white rounded-md ">
{props.children}
    </button>

  );
}

export default Button;
