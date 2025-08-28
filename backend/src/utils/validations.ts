import { z } from 'zod'

export const payloadSchema = z.object({
    machine_id: z.string().trim(),
    os_type: z.string().trim(),
    disk_encryption: z.boolean(),
    os_update: z.boolean(),
    antivirus: z.boolean(),
    sleep_settings: z.boolean()
})

export type PayloadDTO = z.infer<typeof payloadSchema>

export const reportFilterSchema = z.object({
    os_type: z.string().optional(),
    machine_id: z.string().optional(),
    disk_encryption: z.boolean().optional(),
    os_update: z.boolean().optional(),
    antivirus: z.boolean().optional(),
    sleep_settings: z.boolean().optional(),
    from: z.string()
        .refine(val => !isNaN(Date.parse(val)), {
            message: "Invalid date format",
        })
        .transform(val => new Date(val))
        .optional(),
    to: z.string()
        .refine(val => !isNaN(Date.parse(val)), {
            message: "Invalid date format",
        })
        .transform(val => new Date(val))
        .optional(),
});