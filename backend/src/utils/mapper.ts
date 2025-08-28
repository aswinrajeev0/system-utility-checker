import { ObjectId } from "mongoose";
import { IReport } from "../models/report.model";
import { ReportResponse } from "../shared/types";

export const toReportResponse = (report: IReport): ReportResponse => {
    return {
        machine_id: report.machine_id,
        os_type: report.os_type,
        disk_encryption: report.disk_encryption,
        os_update: report.os_update,
        antivirus: report.antivirus,
        sleep_settings: report.sleep_settings,
        createdAt: report.createdAt as Date,
        updatedAt: report.updatedAt as Date,
        id: (report._id as ObjectId).toString()
    }
}