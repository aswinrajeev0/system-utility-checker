import { Router } from "express";
import { createReport, getReports, getReportsCSV } from "../controllers/controller";
import mongoose from "mongoose";
import { HTTP_STATUS } from "../shared/constants";

const router = Router();

router.route("/report")
    .post(createReport)
    .get(getReports);

router.get("/report/csv", getReportsCSV)

router.get("/health", (req, res, next) => {
    const dbStatus = mongoose.connection.readyState === 1 ? "UP" : "DOWN";

    res.status(HTTP_STATUS.OK).json({
        status: "UP",
        database: dbStatus,
        timestamp: new Date().toISOString(),
    });
})

export default router;