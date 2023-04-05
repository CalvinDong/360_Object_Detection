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