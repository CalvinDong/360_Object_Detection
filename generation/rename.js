// Just looping through a folder and renaming everything numerically from 0 - what ever number 

const fs = require('fs');
const path = require('path');

const folder_path = '../Datasets/Backgrounds'
const folder = fs.readdirSync(folder_path);
const target_length = folder.length.toString().length
for (let i = 0; i < folder.length; i++){
  let p = path.join(folder_path, folder[i])
  let length = i.toString().length
  let mime_type = folder[i].substring(folder[i].indexOf('.') + 1)
  let name = i.toString().padStart(target_length, '0')

  fs.rename(p, `${folder_path}/${name}.${mime_type.toLowerCase()}` , err => {
    if (err) {
      console.error(err);
    }
    // done
  });
}

