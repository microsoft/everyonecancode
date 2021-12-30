const imageApiUrl = process.env.VUE_APP_IMAGE_API_URL || "";
const faceApiKey = process.env.VUE_APP_FACE_API_KEY || "";
const speechApiKey = process.env.VUE_APP_SPEECH_API_KEY || "";
const faceApiEndpoint = process.env.VUE_APP_FACE_API_ENDPOINT || "";

export { imageApiUrl, faceApiKey, faceApiEndpoint, speechApiKey };
