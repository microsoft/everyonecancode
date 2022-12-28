const imageApiUrl = import.meta.env.VITE_IMAGE_API_URL || "";
const faceApiKey = import.meta.env.VITE_FACE_API_KEY || "";
const speechApiKey = import.meta.env.VITE_SPEECH_API_KEY || "";
const faceApiEndpoint = import.meta.env.VITE_FACE_API_ENDPOINT || "";

export { imageApiUrl, faceApiKey, faceApiEndpoint, speechApiKey };
