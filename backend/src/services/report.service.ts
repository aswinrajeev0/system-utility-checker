import Report from "../models/report.model"
import { ReportFilterDTO, ReportResponse } from "../shared/types";
import { toReportResponse } from "../utils/mapper";
import { PayloadDTO } from "../utils/validations"

export const createReportService = async (payload: PayloadDTO): Promise<ReportResponse> => {
    const report = await Report.create(payload);
    return toReportResponse(report)
}

export const getReportsService = async(filter: ReportFilterDTO): Promise<ReportResponse[]> => {
    const reports = await Report.find(filter).sort({createdAt: -1});
    return reports.map(report => toReportResponse(report));
}