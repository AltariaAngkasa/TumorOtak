const dropArea = document.getElementById('dropArea');
const imageUpload = document.getElementById('imageUpload');

dropArea.addEventListener('click', () => imageUpload.click());

dropArea.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropArea.classList.add('hover');
});

dropArea.addEventListener('dragleave', () => {
  e.preventDefault();
  dropArea.classList.remove('hover');
});

dropArea.addEventListener('drop', (e) => {
  e.preventDefault();
  dropArea.classList.remove('hover');

  if (e.dataTransfer.files.length > 0) {
    const file = e.dataTransfer.files[0];

    // SOLUSI: masukkan file ke input melalui DataTransfer (disupport semua browser modern)
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    imageUpload.files = dataTransfer.files;

    dropArea.innerHTML = `📄 ${file.name}`;
  }
});



// Menangani file yang dipilih secara manual (tanpa drag-drop)
imageUpload.addEventListener('change', () => {
  if (imageUpload.files.length > 0) {
    const file = imageUpload.files[0];
    dropArea.innerHTML = `📄 ${file.name}`;
  }
});
