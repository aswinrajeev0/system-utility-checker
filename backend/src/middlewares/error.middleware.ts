import { NextFunction, Request, Response } from "express";
import { ERROR_MESSAGES, HTTP_STATUS } from "../shared/constants"; 
import { ZodError } from "zod";

export const errorHandler = (
    err: any,
    req: Request,
    res: Response,
    next: NextFunction
) => {
    let statusCode: number = HTTP_STATUS.INTERNAL_SERVER_ERROR;
    let message: string = ERROR_MESSAGES.INTERNAL_SERVER_ERROR;
    let errors: any[] | null = null;

    if (err instanceof ZodError) {
        statusCode = HTTP_STATUS.BAD_REQUEST;
        message = ERROR_MESSAGES.VALIDATION_FAILED;
        errors = err.issues.map(error => ({
            field: error.path.join("."),
            message: error.message
        }));
    }

    console.error(err)
    res.status(statusCode).json({
        success: false,
        statusCode,
        message,
        errors,
    });
};
