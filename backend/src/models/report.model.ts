import { Schema, model, Document } from "mongoose";

export interface IReport extends Document {
    machine_id: string;
    os_type: string;
    disk_encryption: boolean;
    os_update: boolean;
    antivirus: boolean;
    sleep_settings: boolean;
    createdAt?: Date;
    updatedAt?: Date;
}

const reportSchema = new Schema<IReport>(
    {
        machine_id: { type: String, required: true, trim: true },
        os_type: {type: String, required: true},
        disk_encryption: { type: Boolean, required: true },
        os_update: { type: Boolean, required: true },
        antivirus: { type: Boolean, required: true },
        sleep_settings: { type: Boolean, required: true },
    },
    { timestamps: true }
);

const Report = model<IReport>("Report", reportSchema);

export default Report;
