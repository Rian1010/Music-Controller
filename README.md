# Music Controller 
## Setup
### First commands
- `sudo pip3 install django djangorestframework`

- `django-admin startproject music_controller`

- `django-admin startapp api`

### frontend 
- After creating the frontend django app, use `npm init -y`
- React webpack: `npm i webpack webpack -cli --save-dev`
- Babel: `npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev`
- React: `npm i react react-dom --save-dom`
- Materialize: `npm install @material-ui/core`
- For async and await: `npm install @babel/plugin-proposal-class-properties`
- React Routers: `npm install react-router-dom`
- Material icons: `npm install @material-ui/icons`

### In `babel.config.json`: 
```json
{
    "presets": [
        [
            "@babel/preset-env",
            {
                "targets": {
                    "node": "10"
                }
            }
        ],
        "@babel/preset-react"
    ],
    "plugins": ["@babel/plugin-proposal-class-properties"]
}
```

### In `webpack.config.js`:
```javascript
const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "./static/frontend"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("production"),
      },
    }),
  ],
};
```

### In `package.json`:
- under `"scripts"`, change `"test": "echo \"Error: no test specified\" && exit 1"` to `"dev": "webpack --mode development --watch"` and under it, add `"build": "webpack --mode production"`

### Project
- Create `music_controller/frontend/src/index.js`
- After setting up the urls, and all frontend things, run `npm run dev`