import dotenv from 'dotenv'
import express from "express";
import rateLimit from 'express-rate-limit';
import morgan from "morgan"
import connectDB from './config/db';
import router from './routes/router';
import { errorHandler } from './middlewares/error.middleware';

dotenv.config();
const PORT = process.env.PORT
connectDB();

const app = express();

app.use(morgan("dev"))
app.use(express.json());
app.use(rateLimit({
    windowMs: 15 * 60 * 1000,
    max: 1000
}));

app.use("/api/", router)

app.use(errorHandler)

app.listen(PORT, () => {
    console.log("Server is running on port", PORT);
});