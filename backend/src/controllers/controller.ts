import { NextFunction, Request, Response } from "express";
import { payloadSchema, reportFilterSchema } from "../utils/validations";
import { createReportService, getReportsService } from "../services/report.service";
import { HTTP_STATUS } from "../shared/constants";
import { ReportFilterDTO } from "../shared/types";

export const createReport = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
        const payload = payloadSchema.parse(req.body);
        await createReportService(payload);
        res.status(HTTP_STATUS.CREATED).json({
            success: true
        })
    } catch (error) {
        next(error)
    }
}

export const getReports = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
        const { os_type, machine_id, disk_encryption, os_update, antivirus, sleep_settings, from, to } = req.query;

        reportFilterSchema.parse(req.query);

        const filter: ReportFilterDTO = {};
        if (os_type) filter.os_type = os_type.toString();
        if (machine_id) filter.machine_id = machine_id.toString();
        if (disk_encryption !== undefined) filter.disk_encryption = disk_encryption === "true";
        if (os_update !== undefined) filter.os_update = os_update === "true";
        if (antivirus !== undefined) filter.antivirus = antivirus === "true";
        if (sleep_settings !== undefined) filter.sleep_settings = sleep_settings === "true";

        if (from || to) {
            filter.createdAt = {};
            if (from) filter.createdAt.$gte = new Date(from as string);
            if (to) filter.createdAt.$lte = new Date(to as string);
        }

        const reports = await getReportsService(filter)

        res.status(HTTP_STATUS.OK).json({
            success: true,
            reports
        })

    } catch (error) {
        next(error)
    }
}