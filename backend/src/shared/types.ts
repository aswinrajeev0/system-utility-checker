export type ReportFilterDTO = {
    os_type?: string;
    machine_id?: string;
    disk_encryption?: boolean;
    os_update?: boolean;
    antivirus?: boolean;
    sleep_settings?: boolean;
    createdAt?: {
        $gte?: Date;
        $lte?: Date;
    };
};

export type ReportResponse = {
    os_type: string;
    machine_id: string;
    disk_encryption: boolean;
    os_update: boolean;
    antivirus: boolean;
    sleep_settings: boolean;
    createdAt: Date;
    updatedAt: Date;
    id: string;
}