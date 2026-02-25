document.getElementById('add-task-btn').addEventListener('click', function() {
  const taskInput = document.getElementById('task-input');
  const taskText = taskInput.value.trim();
  if (taskText !== '') {
    addTask(taskText);
    taskInput.value = '';
  }
});

document.getElementById('theme-toggle-btn').addEventListener('click', function() {
  document.body.classList.toggle('dark-theme');
});

function addTask(text) {
  const taskList = document.getElementById('task-list');
  const li = document.createElement('li');
  const span = document.createElement('span');
  span.className = 'task-text';
  span.textContent = text;

  const deleteBtn = document.createElement('button');
  deleteBtn.className = 'delete-btn';
  deleteBtn.textContent = 'Delete';
  deleteBtn.addEventListener('click', function() {
    taskList.removeChild(li);
  });

  li.appendChild(span);
  li.appendChild(deleteBtn);
  taskList.appendChild(li);
}
