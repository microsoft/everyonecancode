module.exports = {
  publicPath: process.env.PUBLIC_PATH
    ? `/${process.env.PUBLIC_PATH}`
    : '/'
}
