// system packages
const fs = require('fs');
const path = require('path');
const os = require('os');

// basic helpers
const async = require('async');
const _ = require('lodash');

// drawing utilities
const { createCanvas, loadImage, CanvasRenderingContext2D } = require('canvas');
const floodfill = require('@roboflow/floodfill')(CanvasRenderingContext2D);

// for writing annotations
var Handlebars = require('handlebars');
var vocTemplate = Handlebars.compile(fs.readFileSync(__dirname + "/voc.tmpl", "utf-8"));


// how many images we want to create
const IMAGES_TO_GENERATE = 5000;
// how many to generate at one time
const CONCURRENCY = Math.max(1, os.cpus().length - 1);

// approximate aspect ratio of our phone camera
// scaled to match the input of CreateML models
const CANVAS_WIDTH = 3840;
const CANVAS_HEIGHT = 1920;

// the most objects you want in your generated images
const MAX_OBJECTS = 20;

// where to store our images
const OUTPUT_DIR = path.join(__dirname, "output");

// location of jpgs on your filesystem (validation set from here: https://www.figure-eight.com/dataset/open-images-annotated-with-bounding-boxes/)
const OPEN_IMAGES = path.join(os.homedir(), "OpenImages");
// text file of good candidate images (I selected these for size & no fruit content)
//const BACKGROUNDS = fs.readFileSync(__dirname + "/OpenImages.filtered.txt", "utf-8").split("\n");

// location of folders containing jpgs on your filesystem (clone from here: https://github.com/Horea94/Fruit-Images-Dataset)
const FRUITS = path.join("/Users/calvindong/Documents/Repos/360_Object_Detection/Datasets/fruits-360/Training");

//---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// get class names
const folders = _.filter(fs.readdirSync(FRUITS), function(filename) {
  // filter out hidden files like .DS_STORE
  return filename.indexOf('.') != 0;
});

var classes = _.map(folders, function(folder) {
  // This dataset has some classes like "Apple Golden 1" and "Apple Golden 2"
  // We want to combine these into just "Apple" so we only take the first word
  return folder.split(" ")[0];
});

// for each class, get a list of images
const OBJECTS = {};
_.each(folders, function(folder, i) {
  var cls = classes[i]; // get the class name

  var objs = [];
  objs = _.filter(fs.readdirSync(path.join(FRUITS, folder)), function(filename) {
      // only grab jpg images
      return filename.match(/\.jpe?g/);
  });

  objs = _.map(objs, function(image) {
      // we need to know which folder this came from
      return path.join(folder, image);
  });
  
  if(!OBJECTS[cls]) {
      OBJECTS[cls] = objs;
  } else {
      // append to existing images
      _.each(objs, function(obj) {
          OBJECTS[cls].push(obj);
      });
  }
});

// when we randomly select a class, we want them equally weighted
classes = _.uniq(classes);

console.log(classes.length)
fruit = []
classes.map( x => {
  fruit.push(x)
})

console.log(fruit)

if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR);