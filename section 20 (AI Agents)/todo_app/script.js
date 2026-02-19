document.getElementById('add-todo').addEventListener('click', addTodo);

function addTodo() {
    const todoInput = document.getElementById('todo-input');
    const todoText = todoInput.value;
    if (todoText === '') return;

    const li = document.createElement('li');
    li.textContent = todoText;
    li.addEventListener('click', toggleDone);

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.addEventListener('click', deleteTodo);
    li.appendChild(deleteButton);

    document.getElementById('todo-list').appendChild(li);
    todoInput.value = '';
}

function toggleDone(event) {
    event.target.classList.toggle('done');
}

function deleteTodo(event) {
    const li = event.target.parentElement;
    li.remove();
}
