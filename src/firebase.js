// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD20al4hF4c3HaksHmTLaQikjvRi4Lacj8",
  authDomain: "skillsyncs-26a99.firebaseapp.com",
  projectId: "skillsyncs-26a99",
  storageBucket: "skillsyncs-26a99.appspot.com",
  messagingSenderId: "954505800713",
  appId: "1:954505800713:web:b05dedfdcca49903095cd8",
  measurementId: "G-RKWKH6MHLT"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth }