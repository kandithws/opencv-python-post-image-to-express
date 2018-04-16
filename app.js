var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var multer  = require('multer')
var storage =   multer.diskStorage({
    destination: function (req, file, callback) {
      callback(null, './uploads');
    },
    filename: function (req, file, callback) {
      var imageUrl = file.fieldname + '-' + Date.now()+'.jpg';
      callback(null, imageUrl);
    }
  });
  var upload = multer({ storage : storage });

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
//app.use(bodyParser.text({ type: 'text/html' }))

app.get('/', function(req, res) {
    res.send('Hello World!');
});

app.post('/api/publish_license', upload.single('image'), function (req, res){
    
    console.log('Hello World!!!');
    var data = JSON.parse(req.body.json); // will get as raw string
    console.log(req.headers)
    console.log(req.headers.authorization)
    console.log('Publish License Plate API Request: ' + JSON.stringify(data));
    console.log('Publish License Plate API Request: ' + req.body.json);
    console.log('Saving image at: ' + req.file.path);
    res.send(JSON.stringify({status: 'FOUND'}) );
})

app.listen(3000, () => console.log('Example app listening on port 3000!'));